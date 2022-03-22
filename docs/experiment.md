# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|deberta_v3|[train27]|[infer27]|0.8794|0.881||
|pseudo_mcdrop|[train29]|[infer29]|0.8878|0.885||
|pseudo_mcdrop|[train29]|[infer29.1]|0.8900|0.887|先頭文字の後処理|
|pseudo_mcdrop|[train29]|[infer29.2]|0.8900||先頭文字の後処理, 0.5以上を先に計算, 2個以上|
|pseudo_mcdrop|[train29]|[infer29.3]|0.8900||先頭文字の後処理, 0.5以上を先に計算, 3個以上|
|pseudo_mcdrop|[train29]|[infer29.4]|0.8900||先頭文字の後処理, 0.5以上を先に計算, 4個以上|
|v6_sampling|[train35]|[infer35]|0.8974|0.883||
|v6_sampling|[train35]|[infer35.6]|0.8974|0.877|max_pool|
|v6_sampling|[train35]|[infer35.7]|0.8974|0.883|0.5以上を先に計算, 2個以上|
|v6_sampling|[train35]|[infer35.8]|0.8974|0.883|0.5以上を先に計算, 3個以上|
|v6_sampling|[train35]|[infer35.9]|0.8974|0.881|0.5以上を先に計算, 4個以上|
|v6_sampling|[train35]|[infer35.10]|0.8974|0.877|0.5以上を先に計算, 1個以上|
|v6_sampling|[train35]|[infer35.11]|0.8997|0.886|先頭文字の後処理|
|v6_sampling|[train35]||0.8919||先頭文字+同じ単語の後処理|
|v6_sampling|[train35]|[infer35.12]|0.8996|0.885|先頭文字+1個飛ばしの連結の後処理|
|v6_sampling|[train35]|[infer35.13]||0.884|先頭文字+2個飛ばしの連結の後処理|
|v6_sampling|[train35]||0.6323||先頭文字+trainに無い単語除外の後処理|
|v6_sampling|[train35]|[infer35.14]|0.8997|0.885|thr=0.52(0.5より0.00002改善)|
|v2_relabel_2nd|[train36]|[infer36]|0.8868|0.884|fold-4, 3epochまで|
|v2_relabel_3rd|[train37]|[infer37]|0.8903|0.882|fold-4, 3epochまで|
|v2_relabel_3rd|[train37]|[infer37.1]||0.877|fold-0|
|v2_relabel_3rd|[train37]|[infer37.2]||0.876|fold-1|
|v2_relabel_3rd|[train37]|[infer37.3]||0.873|fold-2|
|harf_of_2nd|[train38]||||めちゃ低い|
|random_sample|[train39]|[infer39]|0.8905|0.883||
|random_sample|[train39]|[infer39.1]|0.8927|0.886||
|fold_4|[train40]|[infer40]|0.8933|0.885|ここから後処理デフォルト, 後処理なし0.8910|
|epoch6|[train41]|[infer41]||0.886|fold-4 3epoch, 後処理なし0.8924|
|accum_2|[train42]|[infer42]|0.8931|0.886|ここからvalidも後処理|
|warmup5|[train43]|[infer43]|0.8952|||
|clip2000|[train44]|[infer44]||||

[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88683264
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=88894891
[infer29.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=90405444
[infer29.2]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90909168
[infer29.3]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90909717
[infer29.4]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90909977
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=89943923
[infer35.6]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90243712
[infer35.7]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90260146
[infer35.8]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90318169
[infer35.9]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch/notebook?scriptVersionId=90328111
[infer35.10]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90338922
[infer35.11]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90397794
[infer35.12]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90540873
[infer35.13]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90541014
[infer35.14]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90541211
[train36]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/4c29f4dd4c82c92162b997ef37dbbd9cd9131e50/src/nbme_train_by_pytorch.py
[infer36]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90041987
[train37]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/d5c9be3756ac8bd91aa97fef23493aa074c1e808/src/nbme_train_by_pytorch.py
[infer37]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90170833
[infer37.1]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138567
[infer37.2]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138620
[infer37.3]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90138713
[train38]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/bab8b2d4a4668853b556b2b5850c42e9684cba4c/src/nbme_train_by_pytorch.py
[train39]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/d172d5ee7532d3440d995ed8cee5093e303f0f0a/src/nbme_train_by_pytorch.py
[infer39]:https://www.kaggle.com/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90330363
[infer39.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90409030
[train40]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/edc2ed5691f842ae8769f33dd1010a817e6a5eca
[infer40]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90438527
[train41]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/8e0d68fb0c02c591b8835976a3b0e0a33d459424/src/nbme_train_by_pytorch.py
[infer41]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90626258
[train42]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/378fb66e64ce11bd0476e99781dac98e1485e36a/src/nbme_train_by_pytorch.py
[infer42]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90674931
[train43]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9fca0a49d0589619d2b71b17dd9a1b68b51c0ef2/src/nbme_train_by_pytorch.py
[infer43]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/edit/run/90909977
[train44]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/24b4fd78f6658d2da95588835ee52e6afcc2f71d/src/nbme_train_by_pytorch.py
[infer44]:xxx

## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
