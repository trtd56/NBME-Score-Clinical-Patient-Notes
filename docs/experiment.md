# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785)|
|[Bio_ClinicalBERT 0.8910]|[Bio_ClinicalBERT ]|医療系用語での事前学習1|
|[Bio_Discharge_Summary_BERT ]|[Bio_Discharge_Summary_BERT ]|医療系用語での事前学習2|
|[BiomedNLP-PubMedBERT ]|[BiomedNLP-PubMedBERT ]|医療系用語での事前学習3|

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
[Bio_ClinicalBERT 0.8910]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87261640
[Bio_ClinicalBERT ]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87264263
[Bio_Discharge_Summary_BERT ]:xxx
[Bio_Discharge_Summary_BERT ]:xxx
[BiomedNLP-PubMedBERT ]:xxx
[BiomedNLP-PubMedBERT ]:xxx

## やりたいことメモ
- RoBERTa
- large model
- debertaが効きそう？: https://www.kaggle.com/nbroad/qa-ner-hybrid-train-nbme/notebook
- 後処理
- OOFの分析
