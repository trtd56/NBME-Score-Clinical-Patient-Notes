# 実験


|exp_name|train|infer|CV|LB|memo|
|--|--|--|--|--|--|
|roberta-base|[train01]|[infer01]|0.7825|0.799||
|bert-large-uncased|[train02]|[infer02]|0.8178|0.829||
|nakamas_preprocessing|[train03]|[infer03]|0.8119|0.824|nakamaさんの前処理|
|roberta-large|[train04]|[infer04]|0.8280|0.837||
|ReduceLROnPlateau|[train05]|[infer05]|0.8458|0.851|early stoppingをf1で|
|preprocessing_fix|[train06]|[infer06]|0.8431|0.849|seq_l=448, 前処理の修正|
|preprocessing_fix2|[train07]|[infer07]|0.8455|0.849|↑にバグがあったので修正|
|preprocessing_fix2|[train07]|[infer07.1]|0.8458|0.849|後処理(1文字, the)|
|bce_loss|[train08]||||ダメそう|
|add_feature_text|[train09]|[infer09]|0.8046|0.814|GPU, roberta-base|
|add_feature_text|[train09]|[infer09.1]|0.8046|0.790|GPU, roberta-base, CV max|
|add_feature_text|[train09]|[infer09.2]|0.8047|0.814|GPU, roberta-base, thr=0.48|
|deberta|[train10]||0.7100||GPU, fold-3まで|
|feature_text_tpu|[train11]|[infer11]|0.8311|0.832|roberta-large|
|feature_text_tpu|[train11]|[infer11.1]|0.8314|0.832|thr=0.44|
|cos_decay|[train12]|[infer12]|0.8264|||
|sigmoid group feat|[train13]||||wandbはreloadになっちゃってる, 全部empty labelに分類されてる|
|bce_v2|[train14]|||全部empty labelに分類されてる|
|softmx_group_2layer|[train15]||0.8233||
|earlystop_f1|[train16]||||

[train01]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87293546
[infer01]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87343942
[train02]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87343891
[infer02]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87346757
[train03]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87349915
[infer03]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87352776
[train04]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87353216
[infer04]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87355488
[train05]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87357727
[infer05]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87360960
[train06]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87387152
[infer06]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87428373
[train07]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87432030
[infer07]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87434887
[infer07.1]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87474982
[train08]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87439974
[train09]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-gpu?scriptVersionId=87518649
[infer09]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87564711
[infer09.1]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87565136
[infer09.2]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87566536
[train10]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-gpu?scriptVersionId=87567134
[train11]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87603438
[infer11]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87629479
[infer11.1]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87630021
[train12]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87641317
[infer12]:https://www.kaggle.com/takamichitoda/nbme-infer-transformer-on-gpu?scriptVersionId=87679004
[train13]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87768392
[train14]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87776040
[train15]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87780647
[train16]:https://www.kaggle.com/takamichitoda/nbme-train-transformer-on-tpu?scriptVersionId=87786562

## やりたいことメモ
- 後処理
- OOFの分析
  - アノテーションにばらつきがありそう
- 各ラベルでモデルを作る
  - yearとかはまとめられそう

