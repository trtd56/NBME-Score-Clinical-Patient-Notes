# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785), char-F1=0.672645961766973|
|[roberta-base 0.9508]|[roberta-base 0.799]|char-F1=0.6689833520418732|
|[bert-large-uncased 0.9607]|[bert-large-uncased 0.829]|char-F1=0.6687693274319445|
|[nakamas_preprocessing 0.9591]|[nakamas_preprocessing 0.824]|nakamaさんの前処理, char-F1=0.6713626297362645|
|[roberta-large 0.9605]|[roberta-large 0.837]|char-F1=0.6701872630210779|
|[ReduceLROnPlateau 0.9645]|[ReduceLROnPlateau 0.851]|early stoppingをf1 scoreで, char-F1=0.6689132958966747|


[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061



|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|roberta-base|[train01]|[infer01]|0.7825|0.799||
|bert-large-uncased|[train02]|[infer02]|0.8178|0.829||
|nakamas_preprocessing|[train03]|[infer03]||0.824||
|roberta-large|[train04]|[infer04]||0.837||
|ReduceLROnPlateau|[train05]|[infer05]|0.8458|0.851||

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


## やりたいことメモ
- debertaが効きそう？: https://huggingface.co/docs/transformers/model_doc/deberta
- 後処理
- scheduler: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay
- seq len 512がよいかも
- OOFの分析
