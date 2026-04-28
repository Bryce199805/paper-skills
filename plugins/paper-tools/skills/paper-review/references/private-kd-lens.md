# Private KD Review Lens

Use this only for the reviewer's private analysis and research inspiration. Do not include these points in formal reviewer comments unless they directly affect the paper's own claims, validity, novelty, or evidence.

## Private Research Relevance

Ask:

- Does the paper relate to `knowledge distillation`?
- Does it involve teacher-student learning, model compression, representation transfer, or alignment?
- Can its method inspire heterogeneous KD?
- Does it suggest useful ideas for logits, feature, or relation distillation?

## Heterogeneous KD Checks

For private analysis, check:

- teacher-student architecture mismatch
- `capacity gap`
- `architecture gap`
- `modality gap`
- feature dimension mismatch
- spatial resolution mismatch
- semantic level mismatch
- adapter or projection design
- relation modeling design
- contrastive or alignment objective

## Logits / Feature / Relation Lens

Logits:

- soft targets
- temperature
- KL divergence
- `dark knowledge`
- teacher overconfidence

Feature:

- intermediate feature matching
- channel/spatial alignment
- attention transfer
- semantics mismatch
- projection heads

Relation:

- sample-sample relation
- pixel-pixel relation
- region-region relation
- channel/token relation
- relation graph construction
- scalability of relation loss

## Boundary for Formal Comments

Do not write private inspiration as author-facing criticism.

Author-facing KD comments are appropriate only when, for example:

- the paper claims heterogeneous KD but only evaluates similar teacher-student architectures
- a proposed alignment loss is central but not justified or ablated
- relation distillation is claimed but relation construction is weak or unclear
- experiments do not support the KD-specific claim
