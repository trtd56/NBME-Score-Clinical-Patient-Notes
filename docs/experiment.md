# 実験





|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|roberta-base|[train01]|[infer01]|0.7825|0.799||
|bert-large-uncased|[train02]|[infer02]|0.8178|0.829||
|nakamas_preprocessing|[train03]|[infer03]|0.8119|0.824|nakamaさんの前処理|
|roberta-large|[train04]|[infer04]|0.8280|0.837||
|ReduceLROnPlateau|[train05]|[infer05]|0.8458|0.851|early stoppingをf1で|
|preprocessing_fix|[train06]|[infer06]|||seq_l=448, 前処理の修正|

[train01]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87293546
[infer01]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87343942
[train02]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87343891
[infer02]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87346757
[train03]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87349915
[infer03]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87352776
[train04]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87353216
[infer04]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87355488
[train05]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87357727
[infer05]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87360960
[train06]:xxx
[infer06]:xxx



## やりたいことメモ
- debertaが効きそう？: https://huggingface.co/docs/transformers/model_doc/deberta
- 後処理
- scheduler: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay
- OOFの分析
  - アノテーションにばらつきがありそう
- BCEで予測
- feature_textの追加


## 過去

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785), char-F1=0.672645961766973|

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
