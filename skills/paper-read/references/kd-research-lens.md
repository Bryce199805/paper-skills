# Knowledge Distillation Research Lens

Use this lens for papers related to knowledge distillation, model compression, representation learning, transfer learning, teacher-student learning, alignment, or heterogeneous architectures.

If the paper is not related to KD, keep this section short and state the weak or absent connection.

## KD Relevance

Ask:

- Is this paper directly about `knowledge distillation`?
- If not, can its method transfer to KD?
- Does it involve teacher-student learning, representation alignment, model compression, cross-architecture transfer, cross-modal transfer, or privileged information?

## Heterogeneous KD

Analyze:

- Are teacher and student architectures different?
- Is there a `capacity gap`?
- Is there an `architecture gap`?
- Is there a `modality gap`?
- Is there feature dimension, spatial resolution, or semantic-level mismatch?
- How does the method handle representation mismatch?
- Does it use adapter, projection head, attention transfer, intermediate feature matching, relation graph, or contrastive objective?

## Logits Distillation

Check:

- Does it use soft targets, logits, or probability distributions?
- How is temperature set?
- Is KL divergence or another distribution matching loss used?
- Does it exploit `dark knowledge`?
- Does it address teacher overconfidence or noisy teacher predictions?

## Feature Distillation

Check:

- Which feature layers are matched?
- How are teacher and student feature dimensions aligned?
- Is the loss L2, cosine, attention map, channel-wise matching, spatial-wise matching, or another objective?
- Does it distinguish low-level, mid-level, and high-level features?
- Is there a feature semantics mismatch?

## Relation Distillation

Check:

- Does it distill sample-sample, pixel-pixel, region-region, channel, or token relations?
- How is the relation constructed?
- Is the relation loss scalable?
- Is relation matching more suitable than direct feature matching for heterogeneous models?
- Can it mitigate architecture mismatch?

## Transferable Ideas

Summarize:

- Which idea can be reused for heterogeneous KD?
- Which module, loss, or alignment design is reusable?
- Can the idea be reformulated as logits, feature, or relation distillation?
- Is it suitable for classification, detection, segmentation, dense prediction, multimodal learning, or 3D vision?
- What new hypothesis could it inspire?
