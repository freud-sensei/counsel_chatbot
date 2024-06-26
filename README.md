---
license: cc-by-nc-sa-4.0
base_model: skt/kogpt2-base-v2
tags:
- generated_from_trainer
model-index:
- name: counsel_chatbot
  results: []
widget:
- text: "질문: 어제 잠을 거의 못 자서 피곤해. 답변:"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# counsel_chatbot

This model is a fine-tuned version of [skt/kogpt2-base-v2](https://huggingface.co/skt/kogpt2-base-v2) on the None dataset.

## Model description

* 한국어 심리상담 데이터를 이용해 Ko-GPT2를 fine-tuning하여 만든 심리상담 모형입니다.
* 입력을 하실 땐 '질문: [실제 질문] 답변:'의 형태로 질문하시기 바랍니다.
* Colab의 메모리 한계 상 훈련을 장시간 할 수 없었습니다. 모형이 엉뚱하거나 이상한 답을 할 수 있습니다. 귀엽게 봐 주세요.
* 참고로 전 이 프로젝트를 마무리한 뒤, 아직 인공지능을 파인튜닝하는 것은 너무 큰 비용 및 시간이 소요된다는 것을 깨달았어요. 그래서 요즘은 이쪽 말고 프롬프트 엔지니어링을 파고 있습니다.

## Training and evaluation data

AI Hub의 <감성 대화 말뭉치>를 사용했습니다.
https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=86

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
