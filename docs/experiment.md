# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|label_smooth|[train18]|[infer18]|0.8497|0.855||
|label_smooth|[train18]|[infer18.1]|0.8493|0.855|PostProcessing|
|target_132|[train19]||0.8453|||
|case_tag|[train20]||0.8399|||
|deberta|[train21]|[infer21]|0.8675|0.868|pytorch, GPU, wandbは無し|
|deberta|[train21]|[infer21.1]|0.8678|0.870|thr最適化(0.44)|
|sigmoid_fix|[train22]||||
|deberta-large|[train23]|[infer23]|0.8504|0.860||
|deberta-large|[train23]|[infer23.1]|0.8509|0.861|thr最適化(0.42)|
|focal_loss|[train24]|[infer24]|0.8672|0.865|
|split_text|[train25]|[infer25]|0.8677|0.867||

[train18]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87806343
[infer18]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87811578
[infer18.1]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87811741
[train19]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87812374
[train20]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87879975
[train21]:https://www.kaggle.com/takamichitoda/nbme-train-by-pytorch?scriptVersionId=88074775
[infer21]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=88283037
[infer21.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88283349
[train22]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=88294326
[train23]:https://www.kaggle.com/takamichitoda/nbme-train-by-pytorch?scriptVersionId=88296676
[infer23]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88338301
[infer23.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88338405
[train24]:https://www.kaggle.com/takamichitoda/nbme-train-by-pytorch?scriptVersionId=88344420
[infer24]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88371620
[train25]:https://www.kaggle.com/takamichitoda/nbme-train-by-pytorch?scriptVersionId=88379480
[infer25]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=88420325


## やりたいことメモ
- 後処理
  - yearとかはまとめられそう
- smooth, 1層, ヘッダーだけ先に学習
- case_num
  - ごとにモデルをつくる
  - 別特徴で

## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
