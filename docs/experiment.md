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
|pseudo_relabel|[train26]|[infer26]|0.8691|0.868||
|pseudo_relabel|[train26]|[infer26.1]||0.866|thr=0.6|
|deberta_v3|[train27]|[infer27]|0.8794|0.881||
|deberta_v3|[train27]|[infer27.1]|0.8795|0.880|thr=0.54|
|v3_pseudo_50|[train28]|[infer28]|0.8819|0.882|fold-3, 4epochまで|
|pseudo_mcdrop|[train29]|[infer29]||||

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
[train26]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/b1c8ddeef5aa930142ff482116a39fde5b99cebc/src/nbme_train_by_pytorch.py
[infer26]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=88600070
[infer26.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88600175
[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88683264
[infer27.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=88683503
[train28]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/3149c94b3cbb86227803ce8313ed9b9449e86dc9/src/nbme_train_by_pytorch.py
[infer28]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88787914
[train29]:xxx
[infer29]:xxx

## やりたいことメモ
- 後処理
  - yearとかはまとめられそう
- ヘッダーだけ先に学習
- case_num
  - ごとにモデルをつくる
  - 別特徴で

## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
