# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785), char-F1=0.672645961766973|
|[roberta-base 0.9508]|[roberta-base 0.799]|char-F1=0.6689833520418732|
|[bert-large-uncased ]|[bert-large-uncased ]||

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
[roberta-base 0.9508]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87293546
[roberta-base 0.799]:xxx
[bert-large-uncased ]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87343891
[bert-large-uncased ]:xxx




## やりたいことメモ
- debertaが効きそう？: https://www.kaggle.com/nbroad/qa-ner-hybrid-train-nbme/notebook
- 後処理
- scheduler: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay
- seq len 512がよいかも
- OOFの分析
