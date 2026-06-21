---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:9000
- loss:ContrastiveLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: How can I locate a person using a cell phone number?
  sentences:
  - Is it possible to determine a persons location by the cell phone number? Why?
  - How do I gain weight as a teenager?
  - How do I overcome my pornography addiction?
- source_sentence: Why Supreme Court directed all cinema halls across the country
    to play the National Anthem before the start of a film?
  sentences:
  - Will BYJU's learning app is good enough to help me with the SEBA board as well
    as my NEET preparation?
  - Is PlayStation 4 region free?
  - What's your stand on the recent Supreme Court's order about national anthem in
    cinema halls?
- source_sentence: What are some good ways to insult a Dartmouth student?
  sentences:
  - How do animals communicate?
  - What makes some students unable to fit in at Dartmouth?
  - Currently, which field of engineering has more scope in India?
- source_sentence: How can I get free music on my iPod?
  sentences:
  - Which human race is most evolved?
  - How do I get free music on an iPod without having to use the internet?
  - How can I be flawless while recording my first song?
- source_sentence: What does the Barnard College look for in a student?
  sentences:
  - What are some good puzzle games for kids on Linux?
  - The girl I like knows I like her. Sometimes she flirts with me, and sometimes
    she ignores me. Why does she do that?
  - What does Barnard College really look for in a student?
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
- cosine_accuracy_threshold
- cosine_f1
- cosine_f1_threshold
- cosine_precision
- cosine_recall
- cosine_ap
- cosine_mcc
model-index:
- name: SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: binary-classification
      name: Binary Classification
    dataset:
      name: Validation
      type: Validation
    metrics:
    - type: cosine_accuracy
      value: 0.822
      name: Cosine Accuracy
    - type: cosine_accuracy_threshold
      value: 0.7902286052703857
      name: Cosine Accuracy Threshold
    - type: cosine_f1
      value: 0.7871581450653983
      name: Cosine F1
    - type: cosine_f1_threshold
      value: 0.7764662504196167
      name: Cosine F1 Threshold
    - type: cosine_precision
      value: 0.714902807775378
      name: Cosine Precision
    - type: cosine_recall
      value: 0.8756613756613757
      name: Cosine Recall
    - type: cosine_ap
      value: 0.8138673020094486
      name: Cosine Ap
    - type: cosine_mcc
      value: 0.6451591942414411
      name: Cosine Mcc
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'What does the Barnard College look for in a student?',
    'What does Barnard College really look for in a student?',
    'The girl I like knows I like her. Sometimes she flirts with me, and sometimes she ignores me. Why does she do that?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.9747, 0.0582],
#         [0.9747, 1.0000, 0.0797],
#         [0.0582, 0.0797, 1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Binary Classification

* Dataset: `Validation`
* Evaluated with [<code>BinaryClassificationEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.BinaryClassificationEvaluator)

| Metric                    | Value      |
|:--------------------------|:-----------|
| cosine_accuracy           | 0.822      |
| cosine_accuracy_threshold | 0.7902     |
| cosine_f1                 | 0.7872     |
| cosine_f1_threshold       | 0.7765     |
| cosine_precision          | 0.7149     |
| cosine_recall             | 0.8757     |
| **cosine_ap**             | **0.8139** |
| cosine_mcc                | 0.6452     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 9,000 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                        | sentence_1                                                                        | label                                                          |
  |:---------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type     | string                                                                            | string                                                                            | float                                                          |
  | modality | text                                                                              | text                                                                              |                                                                |
  | details  | <ul><li>min: 7 tokens</li><li>mean: 15.09 tokens</li><li>max: 42 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 15.32 tokens</li><li>max: 57 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.38</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                         | sentence_1                                                         | label            |
  |:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------|:-----------------|
  | <code>How did the term "private dick" for a private investigator originate?</code> | <code>How can I get a private investigator license in NY?</code>   | <code>0.0</code> |
  | <code>Do you regret your divorce?</code>                                           | <code>Have you ever regretted your divorce?</code>                 | <code>1.0</code> |
  | <code>From where is the earth getting energy to rotate and revolve?</code>         | <code>What will the sun do to the earth in 1 billion years?</code> | <code>0.0</code> |
* Loss: [<code>ContrastiveLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#contrastiveloss) with these parameters:
  ```json
  {
      "distance_metric": "SiameseDistanceMetric.COSINE_DISTANCE",
      "margin": 0.5,
      "size_average": true
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 1
- `per_device_eval_batch_size`: 64
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 64
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch | Step | Validation_cosine_ap |
|:-----:|:----:|:--------------------:|
| 1.0   | 141  | 0.8139               |


### Training Time
- **Training**: 1.0 minutes

### Framework Versions
- Python: 3.11.0
- Sentence Transformers: 5.6.0
- Transformers: 5.12.1
- PyTorch: 2.12.1
- Accelerate: 1.14.0
- Datasets: 5.0.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### ContrastiveLoss
```bibtex
@inproceedings{hadsell2006dimensionality,
    author={Hadsell, R. and Chopra, S. and LeCun, Y.},
    booktitle={2006 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR'06)},
    title={Dimensionality Reduction by Learning an Invariant Mapping},
    year={2006},
    volume={2},
    number={},
    pages={1735-1742},
    doi={10.1109/CVPR.2006.100}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->