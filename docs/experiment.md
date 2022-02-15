# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|label_smooth|[train18]|[infer18]|0.8497|0.855||
|label_smooth|[train18]|[infer18.1]||0.855|PostProcessing|
|target_132|[train19]||0.8453|||
|case_tag|[train20]|||||

[train18]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87806343
[infer18]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87811578
[infer18.1]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87811741
[train19]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87812374
[train20]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87864209

## やりたいことメモ
- 後処理
  - アノテーションにばらつきがありそう
  - yearとかはまとめられそう
- Adamax, Nadam, lr=1e-4, smooth=0.2
- pytorchで実装(DeBERTaとか使いたい)
- LSTMのStacking

## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
