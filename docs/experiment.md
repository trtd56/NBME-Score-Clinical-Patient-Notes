# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|deberta_v3|[train27]|[infer27]|0.8794|0.881||
|deberta_v3|[train27]|[infer27.1]|0.8795|0.880|thr=0.54|
|v3_pseudo_50|[train28]|[infer28]|0.8819|0.882|fold-3, 4epochまで|
|pseudo_mcdrop|[train29]|[infer29]|0.8878|0.885||
|pseudo_mcdrop|[train29]|[infer29.1]|0.8879|0.882|thr=0.6|
|pseudo_v2|[train30]|[infer30]|0.89280|0.881||
|pseudo_v2|[train30]|[infer30.1]|0.89290|0.880|thr=0.6|
|pseudo_v2|[train30]|[infer30.2]|0.89283|0.882|thr=0.48|
|pseudo_v2|[train30]|[infer30.3]|0.89277|0.882|thr=0.46|
|pseudo_v2|[train30]|[infer30.4]|0.89275|0.882|thr=0.44|
|pseudo_v2|[train30]|[infer30.5]|0.892624|0.882|thr=0.42|
|pseudo_v2|[train30]|[infer30.6]|0.892423|0.883|thr=0.40|
|pseudo_v2|[train30]|[infer30.7]||0.882|thr=0.38|
|pseudo_v2|[train30]|[infer30.8]||0.882|thr=0.36|
|pseudo_v2|[train30]|[infer30.9]||0.882|thr=0.34|
|pseudo_v2|[train30]|[infer30.10]||0.882|thr=0.32|
|pseudo_v3|[train31]|[infer31]|0.89483|||
|pseudo_v3|[train31]|[infer31.1]|0.89486||thr=0.48|
|pseudo_v3_sampling|[train32]|[infer32]||||

[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88683264
[infer27.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=88683503
[train28]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/3149c94b3cbb86227803ce8313ed9b9449e86dc9/src/nbme_train_by_pytorch.py
[infer28]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88787914
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88894891
[infer29.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88895387
[train30]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/651157065960402b2618939e88727770d7210801/src/nbme_train_by_pytorch.py
[infer30]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89065280
[infer30.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89065441
[infer30.2]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89076831
[infer30.3]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89077062
[infer30.4]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89077246
[infer30.5]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89077448
[infer30.6]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89078255
[infer30.7]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89148523
[infer30.8]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89149803
[infer30.9]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89150169
[infer30.10]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89150201
[train31]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/06cb1583ac097a90d983638dc54e737311c68f5a/src/nbme_train_by_pytorch.py
[infer31]:xxx
[infer31.1]:xxx
[train32]:xxx
[infer32]:xxx

## やりたいことメモ
- 後処理を考える
- case_numごとにモデルをつくる
- DeBERTa以外のモデル検討


## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
