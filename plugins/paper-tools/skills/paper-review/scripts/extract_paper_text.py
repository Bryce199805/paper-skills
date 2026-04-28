#!/usr/bin/env python3
"""Extract local paper text for the paper-review skill.

The script has no required Python package dependencies. It uses system tools
(`pdftotext`, `pdfinfo`, `detex`) when available and automatically uses PyMuPDF
(`fitz`) for coordinate-aware PDF extraction if installed.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


TEXT_EXTENSIONS = {".txt", ".md", ".markdown"}


def run_command(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(args, text=True, capture_output=True, check=False)
    return proc.returncode, proc.stdout, proc.stderr


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def pdfinfo(path: Path) -> str:
    if not shutil.which("pdfinfo"):
        return "pdfinfo: missing"
    code, out, err = run_command(["pdfinfo", str(path)])
    if code != 0:
        return f"pdfinfo failed: {err.strip()}"
    keep = []
    for line in out.splitlines():
        if re.match(r"^(Title|Subject|Author|Creator|Producer|CreationDate|ModDate|Pages):", line):
            keep.append(line)
    return "\n".join(keep) if keep else "pdfinfo: no selected metadata"


def extract_pdf_pymupdf(path: Path, mode: str) -> tuple[str, list[str]]:
    import fitz  # type: ignore

    warnings: list[str] = []
    doc = fitz.open(str(path))
    pages: list[str] = []

    for page_index, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        text_blocks = []
        for block in blocks:
            x0, y0, x1, y1, text = block[:5]
            text = " ".join(str(text).split())
            if text:
                text_blocks.append((float(x0), float(y0), float(x1), float(y1), text))

        if not text_blocks:
            warnings.append(f"Page {page_index}: no text blocks extracted")
            pages.append(f"## Page {page_index}\n")
            continue

        width = float(page.rect.width)
        mid = width / 2.0

        if mode == "single-column":
            ordered = sorted(text_blocks, key=lambda b: (b[1], b[0]))
        elif mode == "two-column":
            left = [b for b in text_blocks if ((b[0] + b[2]) / 2.0) < mid]
            right = [b for b in text_blocks if ((b[0] + b[2]) / 2.0) >= mid]
            ordered = sorted(left, key=lambda b: (b[1], b[0])) + sorted(right, key=lambda b: (b[1], b[0]))
        else:
            left_count = sum(1 for b in text_blocks if ((b[0] + b[2]) / 2.0) < mid)
            right_count = len(text_blocks) - left_count
            if left_count >= 4 and right_count >= 4:
                left = [b for b in text_blocks if ((b[0] + b[2]) / 2.0) < mid]
                right = [b for b in text_blocks if ((b[0] + b[2]) / 2.0) >= mid]
                ordered = sorted(left, key=lambda b: (b[1], b[0])) + sorted(right, key=lambda b: (b[1], b[0]))
            else:
                ordered = sorted(text_blocks, key=lambda b: (b[1], b[0]))

        body = "\n\n".join(block[4] for block in ordered)
        pages.append(f"## Page {page_index}\n\n{body}")

    return "\n\n".join(pages), warnings


def split_layout_page(page_text: str, mode: str) -> tuple[str, str]:
    lines = page_text.splitlines()
    content_lines = [line.rstrip("\n") for line in lines if line.strip()]
    if mode == "raw-layout" or not content_lines:
        return page_text.strip(), "raw-layout"

    width = max(len(line) for line in content_lines)
    if mode == "single-column" or width < 70:
        return "\n".join(line.strip() for line in content_lines), "single-column"

    start = int(width * 0.35)
    end = int(width * 0.65)
    best_index = None
    best_score = -1

    for idx in range(start, end):
        score = 0
        for line in content_lines:
            window = line[max(0, idx - 3) : min(len(line), idx + 4)]
            left = line[:idx].strip()
            right = line[idx:].strip()
            if left and right and window.count(" ") >= max(3, len(window) - 1):
                score += 1
        if score > best_score:
            best_score = score
            best_index = idx

    threshold = max(4, int(len(content_lines) * 0.30))
    should_split = mode == "two-column" or (best_index is not None and best_score >= threshold)

    if not should_split or best_index is None:
        return "\n".join(line.strip() for line in content_lines), "layout-single-or-uncertain"

    left_lines: list[str] = []
    right_lines: list[str] = []
    for line in content_lines:
        left = line[:best_index].strip()
        right = line[best_index:].strip()
        if left:
            left_lines.append(left)
        if right:
            right_lines.append(right)

    merged = "\n".join(left_lines)
    if right_lines:
        merged += "\n\n" + "\n".join(right_lines)
    return merged.strip(), "two-column"


def extract_pdf_pdftotext(path: Path, mode: str) -> tuple[str, list[str]]:
    warnings: list[str] = []
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is not installed and PyMuPDF is unavailable")

    code, out, err = run_command(["pdftotext", "-layout", str(path), "-"])
    if code != 0:
        raise RuntimeError(f"pdftotext failed: {err.strip()}")

    raw_pages = out.split("\f")
    pages: list[str] = []
    uncertain = 0
    for index, raw_page in enumerate(raw_pages, start=1):
        if not raw_page.strip():
            continue
        body, detected = split_layout_page(raw_page, mode)
        if detected == "layout-single-or-uncertain":
            uncertain += 1
        pages.append(f"## Page {index}\n\n{body}")

    if uncertain:
        warnings.append(f"{uncertain} page(s): two-column detection uncertain; used layout order")
    return "\n\n".join(pages), warnings


def extract_pdf(path: Path, mode: str) -> tuple[str, list[str], str]:
    if mode != "raw-layout":
        try:
            text, warnings = extract_pdf_pymupdf(path, mode)
            return text, warnings, "PyMuPDF"
        except ImportError:
            pass
        except Exception as exc:
            fallback_warning = f"PyMuPDF extraction failed: {exc}"
            text, warnings = extract_pdf_pdftotext(path, mode)
            return text, [fallback_warning] + warnings, "pdftotext-layout"

    text, warnings = extract_pdf_pdftotext(path, mode)
    return text, warnings, "pdftotext-layout"


def extract_tex(path: Path) -> tuple[str, list[str], str]:
    if shutil.which("detex"):
        code, out, err = run_command(["detex", str(path)])
        if code == 0 and out.strip():
            return out, [], "detex"
        return read_text(path), [f"detex failed or returned empty output: {err.strip()}"], "raw-tex"
    return read_text(path), ["detex is not installed; raw LaTeX was read"], "raw-tex"


def quality_warnings(text: str, ext: str) -> list[str]:
    warnings: list[str] = []
    compact = re.sub(r"\s+", "", text)
    if len(compact) < 2000 and ext == ".pdf":
        warnings.append("PDF text is very short; the file may be scanned, image-heavy, or poorly parsed")
    if ext == ".pdf":
        warnings.append("Figures, tables, equations, and algorithm boxes may be incomplete or out of order")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract local paper text for paper-review.")
    parser.add_argument("path", help="Path to a .pdf, .tex, .md, or .txt paper file")
    parser.add_argument(
        "--mode",
        choices=["auto", "two-column", "single-column", "raw-layout"],
        default="auto",
        help="PDF column handling mode",
    )
    args = parser.parse_args()

    path = Path(args.path).expanduser().resolve()
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"error: not a file: {path}", file=sys.stderr)
        return 2

    ext = path.suffix.lower()
    warnings: list[str] = []
    metadata = ""

    try:
        if ext == ".pdf":
            metadata = pdfinfo(path)
            body, warnings, parser_name = extract_pdf(path, args.mode)
        elif ext == ".tex":
            body, warnings, parser_name = extract_tex(path)
        elif ext in TEXT_EXTENSIONS:
            body = read_text(path)
            parser_name = "direct-text"
        else:
            print(f"error: unsupported file extension: {ext}", file=sys.stderr)
            return 2
    except Exception as exc:
        print(f"error: extraction failed: {exc}", file=sys.stderr)
        return 1

    warnings.extend(quality_warnings(body, ext))

    print("# Extracted Paper Text")
    print()
    print(f"Source: {path}")
    print(f"File type: {ext.lstrip('.') or 'unknown'}")
    print(f"Parser: {parser_name}")
    if args.mode:
        print(f"Column mode: {args.mode}")
    if metadata:
        print()
        print("## Metadata")
        print()
        print(metadata)
    if warnings:
        print()
        print("## Extraction Warnings")
        print()
        for warning in warnings:
            print(f"- {warning}")
    print()
    print("## Content")
    print()
    print(body.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
