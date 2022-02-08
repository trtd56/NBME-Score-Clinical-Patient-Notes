# 実験

|CV|LB|memo|
|--|--|--|
|[baseline 0.9542]|[baseline 0.790]|通常BERT, CVはaverageが良さそう(maxで0.785), char-F1=0.672645961766973|
|[Bio_ClinicalBERT 0.8910]|[Bio_ClinicalBERT 0.000]|医療系用語での事前学習1, early stoppingが早すぎたかも|
|[Bio_Discharge_Summary_BERT 0.9012]||医療系用語での事前学習2|
|[BiomedNLP-PubMedBERT 0.9369]|[BiomedNLP-PubMedBERT 0.667]|医療系用語での事前学習3, early stoppingのpatience=5, char-F1=0.6942331204362533|
|[roberta-base 0.9298]|[roberta-base ]|RoBERTa, char-F1=0.6996532260181073|

[baseline 0.9542]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87207206
[baseline 0.790]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87259061
[Bio_ClinicalBERT 0.8910]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87261640
[Bio_ClinicalBERT 0.000]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87264263
[Bio_Discharge_Summary_BERT 0.9012]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87265088
[BiomedNLP-PubMedBERT 0.9369]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87270044
[BiomedNLP-PubMedBERT 0.667]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87275267
[roberta-base 0.9298]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87293546
[roberta-base ]:xxx


## やりたいことメモ
- large model
- debertaが効きそう？: https://www.kaggle.com/nbroad/qa-ner-hybrid-train-nbme/notebook
- 後処理
- linear scheduler
- seq len 512がよいかも
- OOFの分析
- 医療BERT: https://huggingface.co/emilyalsentzer
