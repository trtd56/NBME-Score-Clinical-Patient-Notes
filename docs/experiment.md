# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|deberta_v3|[train27]|[infer27]|0.8794|0.881||
|pseudo_mcdrop|[train29]|[infer29]|0.8878|0.885||
|v6_sampling|[train35]|[infer35]|0.8974|0.883||
|v2_relabel_2nd|[train36]|[infer36]|0.8868|0.884|fold-4, 3epochまで|
|v2_relabel_3rd|[train37]|[infer37]||||
|v2_relabel_3rd|[train37]|[infer37.1]|||fold-0|
|v2_relabel_3rd|[train37]|[infer37.2]|||fold-1|
|v2_relabel_3rd|[train37]|[infer37.3]|||fold-2|

[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88683264
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88894891
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89943923
[train36]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/4c29f4dd4c82c92162b997ef37dbbd9cd9131e50/src/nbme_train_by_pytorch.py
[infer36]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90041987
[train37]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/d5c9be3756ac8bd91aa97fef23493aa074c1e808/src/nbme_train_by_pytorch.py
[infer37]:xxx
[infer37.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138567
[infer37.2]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138620
[infer37.3]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138713


## やりたいことメモ
- 後処理を考える
- case_numごとにモデルをつくる
- DeBERTa以外のモデル検討


## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
