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
|pseudo_mcdrop|[train29]|[infer29.2]|0.8900||fold-0|
|v6_sampling|[train35]|[infer35.11]|0.8997|0.886||
|v1_30_ratio||[infer63]|0.8868|0.885|0.885台ではMAX|
|fp_fn_mask|[train64]|[infer64]|0.8915|0.882||
|v1_warmup_01||[infer65]|0.8873|0.885|f0,2,3はv1_30_ratio|
|fp_mask||[infer66]|0.8885|0.885||
|fn_mask||[infer67]|0.887|0.882||
|g_checkpoint|[train68]||||bs=32|
|fpfn_mask_org|[train69]|[infer69]|0.8944|0.880||
|fpfn_mask_org|[train69]|[infer69.1]|0.8944|0.872|vote min 1|
|fpfn_mask_org|[train69]|[infer69.2]|0.8944|0.880|vote min 2|
|fpfn_mask_org|[train69]|[infer69.3]|0.8944|0.880|vote min 3|
|fpfn_mask_org|[train69]|[infer69.4]|0.8944|0.877|vote min 4|
|fpfn_mask_org|[train69]|[infer69.5]|0.8944||vote min 5|
|fpfn_mask_org|[train69]|[infer69.6]|0.8944|0.876|fold-0|
|fpfn_mask_org|[train69]|[infer69.7]|0.8944|0.875|fold-1|
|bs32_org|[train70]|[infer70]|0.8895|||
|org_mask|[train71]|[infer71]|0.8953|||
|org_mask|[train71]|[infer71.1]|0.8955||thr=0.3117460497755147|
|best_tune|[train72]|[infer72]||||

### org_mask thr
```
0.2
  -> 0.894895918757137
0.25
  -> 0.8952879279464
0.3
  -> 0.8953617183951295
0.35
  -> 0.8952783678393335
0.4
  -> 0.8953375681612645
0.45
  -> 0.895282423973357
0.5
  -> 0.8953180263710765
0.55
  -> 0.8951999512230477
0.6
  -> 0.8950334807152546
BEST: 0.8954874877510696
```
![image](https://user-images.githubusercontent.com/5457315/166129409-3c2342db-13c7-44a5-9691-0a4e06e2770f.png)
<img width="1552" alt="スクリーンショット 2022-05-01 11 19 18" src="https://user-images.githubusercontent.com/5457315/166129427-322fe923-b23c-41c1-a6cd-107668d8b764.png">


[train27]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/9d06cacd1faaf58d9a8190b51018f0acf5e64774/src/nbme_train_by_pytorch.py
[infer27]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=91502169
[train29]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/e5ecba1da4c146c100cec6b0c7f69ff27ef1cee4/src/nbme_train_by_pytorch.py
[infer29.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch/data?scriptVersionId=90405444
[infer29.2]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94391883
[train35]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/db94a53a6337f0ba5df97235b2097065959db48a/src/nbme_train_by_pytorch.py
[infer35.11]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=90397794
[infer63]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=93580935`
[train64]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/506a3bae787f21146407746a5060876f29562dd0
[infer64]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=93678090
[infer65]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=93835976
[infer66]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=93918045
[infer67]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94098938
[train68]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/29fde2e3cd3e8ae52b561c37bd57a1813031b1e7
[train69]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/bece9ec86119518685970bc6100d218d9116ddfd
[infer69]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94280402
[infer69.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94281250
[infer69.2]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94281296
[infer69.3]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94281510
[infer69.4]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94281771
[infer69.5]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94281829
[infer69.6]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94368929
[infer69.7]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94369192
[train70]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/ec5261326853320a7e2485ca133954b2fa00d28d
[infer70]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94444354
[train71]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/a0b2cbc5015acbd98a521955f39add6b0cdd72d8
[infer71]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94449446
[infer71.1]:https://www.kaggle.com/code/takamichitoda/nbme-infer-by-pytorch?scriptVersionId=94449491
[train72]:https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/1dfdc84ce2a535a8a854ba984390c6e5e604cb56
[infer72]:xxx


## past version
- [02/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/cc0ec36cf5afa1e8278340ac774806f4b3d43591/docs/experiment.md): train19まで
- [02/27](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/6e420a8282d95a2217b18d9c562dc9ee26e22e96/docs/experiment.md): train28まで
- [03/14](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/f3921bd422de3529fd3f3f2eff463072e9c0f503/docs/experiment.md): train35まで
- [03/24](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/33928885fa240ae2d3f18ed7eaf1bb337581b52f/docs/experiment.md): train44まで
- [03/29](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/blob/3160e171c2182ad4f2a020e34ba6d4bf637052f0/docs/experiment.md): train48まで
- [04/21](https://github.com/trtd56/NBME-Score-Clinical-Patient-Notes/tree/c21ae7e4d28e7f21da672139c054494c34cd57a4): train63まで
