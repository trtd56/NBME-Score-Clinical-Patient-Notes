# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785)|
|[Bio_ClinicalBERT_]|[Bio_ClinicalBERT_]|医療系用語での事前学習1|

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
[Bio_ClinicalBERT_]:
[Bio_ClinicalBERT_]:

## やりたいことメモ
- RoBERTa
- large model
- 医療系モデルの利用
- debertaが効きそう？: https://www.kaggle.com/nbroad/qa-ner-hybrid-train-nbme/notebook
- 後処理
- OOFの分析
