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
|v1_30_ratio||[infer63]|0.8868|0.885|0.885台ではMAX|
|fp_fn_mask|[train64]|[infer64]||||


[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91502169
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=90405444
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35.11]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90397794
[infer63]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=93580935
[train64]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/506a3bae787f21146407746a5060876f29562dd0
[infer64]:xxx


## past version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
- [03/24](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/33928885fa240ae2d3f18ed7eaf1bb337581b52f/docs/experiment.md): train44まで
- [03/29](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/3160e171c2182ad4f2a020e34ba6d4bf637052f0/docs/experiment.md): train48まで
- [04/21](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/c21ae7e4d28e7f21da672139c054494c34cd57a4): train63まで
