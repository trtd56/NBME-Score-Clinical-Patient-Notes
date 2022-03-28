# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|pseudo_mcdrop|[train29]|[infer29.1]|0.8900|0.887||
|v6_sampling|[train35]|[infer35.11]|0.8997|0.886||
|warmup5|[train43]|[infer43]|0.8952|0.886|fold-3まで|
|warmup5|[train43]|[infer43.1]|0.8940||all 5 fold|
|under_sample_samle|[train45]|[infer45]|0.8936|0.885||
|diff2000|[train46]||0.8799||fold-2が勾配消失|
|fold4_fix|[train47]|[infer47]|0.8924|0.883|fold-3 4 epochまで|
|pseudo_all|[train48]|[infer48]|0.8665|||

[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=90405444
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35.11]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90397794
[train43]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9fca0a49d0589619d2b71b17dd9a1b68b51c0ef2/src/nbme_train_by_pytorch.py
[infer43]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90917387
[infer43.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91272956
[train45]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/d52f5ab90564dae8a5bbc9e0640f475a0809bdb7/src/nbme_train_by_pytorch.py
[infer45]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91164988
[train46]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/b7e71e1a85ece787cb7dc94205fcbc2883a8bcc7/src/nbme_train_by_pytorch.py
[train47]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/2c286901f63e223ea1c8375ed4be399e34ceba78/src/nbme_train_by_pytorch.py
[infer47]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91355562
[train48]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/55abc1ea393f55b866b53f3891faa715df7924e2/src/nbme_train_by_pytorch_all_pseudo.py
[infer48]:xxx

## 気になること
- accumulation、1か3か
- ただ単純にデータ増やしたらよいか
- 周辺単語のロスをmask
- smoothing
- LSTM head
- pseudoを確率で与える
- pseudo allで学習した重みを読み込む

## 過去Version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
- [03/24](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/33928885fa240ae2d3f18ed7eaf1bb337581b52f/docs/experiment.md): train44まで
