# NBME-Score-Clinical-Patient-Notes

![header](https://user-images.githubusercontent.com/5457315/152741419-73b74026-5d9b-42e9-b4b2-1532ec1a9281.png)

## my links
- [competition page](https://www.kaggle.com/c/nbme-score-clinical-patient-notes/overview)
- [wandb](https://wandb.ai/trtd56/NBME?workspace=user-trtd56)
- [train in colab](https://colab.research.google.com/drive/19k8p-73U-u37NRvShyLyKTfaL-FNOxYf#scrollTo=biROVf6yriWY)
- [EDA in colab](https://colab.research.google.com/drive/1lYF89HHfHbhWGXG2Q_lKuTPCpgnj8o_9?usp=sharing)
- [drive](https://drive.google.com/drive/u/0/folders/1ty_XHbeev3OY1CxSJ4LmSlm00JzvNF_a)

## experiment

|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|deberta_v3|[train27]|[infer27]|0.8815|0.883||
|pseudo_mcdrop|[train29]|[infer29.1]|0.8900|0.887||
|v6_sampling|[train35]|[infer35.11]|0.8997|0.886||
|fixed_2nd_labels|[train49]|[infer49]|0.8858|0.884||
|pseudo10000|[train50]|[infer50]|0.8883|0.884||
|re_pseudo|[train51]|[infer51]|0.8844|0.884||
|v1_only|[train52]|[infer52]|0.8825|0.886||
|v1_accum2||[infer53]|0.8853|0.885||
|v1_accum2||[infer53.1]|0.8861|0.885|f0,4=re_pseudo, f1=tfidf_pseudo|
|v1_sift|[train54]||||時間とメモリ食うのでNG|
|v1_accum3|[train55]||||accum2とそんなに変わらない|
|tfidf_pseudo|[train56]||0.8846|0.884|fold-4途中|
|v1_lr5r5|||||良くない|
|v1_warmup5||[infer58]|0.8860|||
|v1_warmup5||[infer58.1]|0.8862||f4=re_pseudo|
|tfidf_v2|[train59]|[infer59]||||
|pseudo_ratio|[train60]|[infer60]||||


[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91502169
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=90405444
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35.11]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90397794
[train49]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/19670cbb3ca650f392c13d9bb7873afda2b4a022/src/nbme_train_by_pytorch.py
[infer49]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91546068
[train50]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/31ed76c44d587ba77aab2ee98c1a9713e492216e/src/nbme_train_by_pytorch.py
[infer50]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91729948
[train51]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/46bd7d43c6366bd30c24b0339ea0fd24c9217324/src/nbme_train_by_pytorch.py
[infer51]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91875795
[train52]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/d3baea5467c939cc55e36cf2d34f535dc2a3f60d/src/nbme_train_by_pytorch.py
[infer52]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91963204
[infer53]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=92048107
[infer53.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=92156921
[train54]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/fddddeb282728a164967890cd8b4e79e0dd9ec77/nbme_train_by_pytorch.py
[train55]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/fe690887384cdddd7bcbbfabe2583d70f10d788f/nbme_train_by_pytorch.py
[train56]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/15160e9d11454122e5e6132bd777268e139dfa9e/nbme_train_by_pytorch.py
[infer56]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=92224929
[infer58]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=92344058
[infer58.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=92336730
[train59]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/24c418741cd25072e269dec3543c30f88fb612a9/nbme_train_by_pytorch.py
[infer59]:xxx

## past version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
- [03/24](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/33928885fa240ae2d3f18ed7eaf1bb337581b52f/docs/experiment.md): train44まで
- [03/29](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/3160e171c2182ad4f2a020e34ba6d4bf637052f0/docs/experiment.md): train48まで
