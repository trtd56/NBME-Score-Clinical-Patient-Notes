# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785), char-F1=0.672645961766973|
|[roberta-base 0.9508]|[roberta-base 0.799]|char-F1=0.6689833520418732|
|[bert-large-uncased 0.9607]|[bert-large-uncased 0.829]|char-F1=0.6687693274319445|
|[nakamas_preprocessing 0.9591]|[nakamas_preprocessing 0.824]|nakamaさんの前処理, char-F1=0.6713626297362645|
|[roberta-large 0.9605]|[roberta-large 0.837]|char-F1=0.6701872630210779|
|[ReduceLROnPlateau ]|[ReduceLROnPlateau ]|early stoppingをf1 scoreで|

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
[roberta-base 0.9508]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87293546
[roberta-base 0.799]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87343942
[bert-large-uncased 0.9607]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87343891
[bert-large-uncased 0.829]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87346757
[nakamas_preprocessing 0.9591]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87349915
[nakamas_preprocessing 0.824]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87352776
[roberta-large 0.9605]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87353216
[roberta-large 0.837]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87355488
[ReduceLROnPlateau ]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87357727
[ReduceLROnPlateau ]:xxx

## やりたいことメモ
- debertaが効きそう？: https://huggingface.co/docs/transformers/model_doc/deberta
- 後処理
- scheduler: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay
- seq len 512がよいかも
- OOFの分析
