# -*- coding: utf-8 -*-
"""NBME Train by pytorch

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19k8p-73U-u37NRvShyLyKTfaL-FNOxYf
"""

!nvidia-smi

from google.colab import drive
drive.mount('/content/drive')

!pip install -U wandb transformers sentencepiece 1> log

!cp -r ./drive/MyDrive/Study/NBME/data/deberta-v2-3-fast-tokenizer .

with open("./drive/MyDrive/Study/config/wandb.txt", "r") as f:
    for line in f:
        wandb_key = line.replace("\n", "")

!wandb login {wandb_key}

# The following is necessary if you want to use the fast tokenizer for deberta v2 or v3
import shutil
from pathlib import Path

transformers_path = Path("/usr/local/lib/python3.7/dist-packages/transformers")

input_dir = Path("./deberta-v2-3-fast-tokenizer")

convert_file = input_dir / "convert_slow_tokenizer.py"
conversion_path = transformers_path/convert_file.name

if conversion_path.exists():
    conversion_path.unlink()

shutil.copy(convert_file, transformers_path)
deberta_v2_path = transformers_path / "models" / "deberta_v2"

for filename in ['tokenization_deberta_v2.py', 'tokenization_deberta_v2_fast.py', "deberta__init__.py"]:
    if str(filename).startswith("deberta"):
        filepath = deberta_v2_path/str(filename).replace("deberta", "")
    else:
        filepath = deberta_v2_path/filename
    if filepath.exists():
        filepath.unlink()

    shutil.copy(input_dir/filename, filepath)

import os
import gc
import dill
import random
import ast
import itertools

import numpy as np
import pandas as pd

from tqdm.auto import tqdm
from sklearn.preprocessing import  LabelEncoder
from sklearn.metrics import f1_score

from matplotlib import pyplot as plt
from transformers import AutoTokenizer, AutoConfig, AutoModel
from transformers import get_cosine_schedule_with_warmup
from transformers import AdamW

import wandb
import pickle

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import Dataset, DataLoader
from transformers.models.deberta_v2 import DebertaV2TokenizerFast
from sklearn.model_selection import StratifiedKFold

device = torch.device("cuda")
scaler = torch.cuda.amp.GradScaler()

os.environ["TOKENIZERS_PARALLELISM"] = "true"

class GCF:
    EXP_NAME = 'fold_4'
 
    PREPROCESSING_DIR = "./drive/MyDrive/Study/NBME/data/preprocessed"
    PSEUDO_DIR = "./drive/MyDrive/Study/NBME/data/pseudo"
    PSEUDO_v2_DIR = "./drive/MyDrive/Study/NBME/data/pseudo_relabel_v2"
    OUTPUT_DIR = f"./drive/MyDrive/Study/NBME/data/output/{EXP_NAME}"
    
    MODEL_NAME = 'microsoft/deberta-v3-large'
    TOKENIZER = DebertaV2TokenizerFast.from_pretrained(MODEL_NAME)
    CONFIG = AutoConfig.from_pretrained(MODEL_NAME)
    SEQUENCE_LENGTH = 384
    
    LR = 2e-5
    WEIGHT_DECAY = 0.01
    
    SEED = 0
    N_FOLDS = 4
    BS = 4
    ACCUMULATE = 1
    N_EPOCHS = 5
    WARM_UP_RATIO = 0.0
    
    NOT_WATCH_PARAM = ["TOKENIZER", "CONFIG", "INPUT_PATH", "PREPROCESSING_DIR", 'NOT_WATCH_PARAM']
    
GCF.TOKENIZER.save_pretrained('nbme_tokenizer')
GCF.CONFIG.save_pretrained('nbme_tokenizer')
!mkdir -p {GCF.OUTPUT_DIR}

def set_seed(seed=GCF.SEED):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

sequences = np.load(open(f"{GCF.PREPROCESSING_DIR}/sequences.npy",'rb'))
masks = np.load(open(f"{GCF.PREPROCESSING_DIR}/masks.npy",'rb'))
type_ids = np.load(open(f"{GCF.PREPROCESSING_DIR}/token_ids.npy",'rb'))
labels = np.load(open(f"{GCF.PREPROCESSING_DIR}/labels.npy",'rb'))

train_df = pd.read_csv(f"{GCF.PREPROCESSING_DIR}/train_preprocessed.csv")
pn_num_folds = train_df['fold']

print(labels.shape)

pseudo_sequences_v1 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v1.npy",'rb'))
pseudo_masks_v1 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v1.npy",'rb'))
pseudo_type_ids_v1 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v1.npy",'rb'))
pseudo_labels_v1 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v1.npy",'rb'))
labels_check_mc_dropout_v1 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v1.npy','rb'))
pn_num_and_case_num_v1 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v1.npy','rb'))
print(pseudo_labels_v1.shape)

pseudo_sequences_v2 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v2.npy",'rb'))
pseudo_masks_v2 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v2.npy",'rb'))
pseudo_type_ids_v2 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v2.npy",'rb'))
pseudo_labels_v2 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v2.npy",'rb'))
labels_check_mc_dropout_v2 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v2.npy','rb'))
pn_num_and_case_num_v2 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v2.npy','rb'))

print(pseudo_labels_v2.shape)


pseudo_sequences_v3 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v3.npy",'rb'))
pseudo_masks_v3 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v3.npy",'rb'))
pseudo_type_ids_v3 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v3.npy",'rb'))
pseudo_labels_v3 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v3.npy",'rb'))
labels_check_mc_dropout_v3 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v3.npy','rb'))
pn_num_and_case_num_v3 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v3.npy','rb'))

print(pseudo_labels_v3.shape)

pseudo_sequences_v4 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v4.npy",'rb'))
pseudo_masks_v4 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v4.npy",'rb'))
pseudo_type_ids_v4 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v4.npy",'rb'))
pseudo_labels_v4 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v4.npy",'rb'))
labels_check_mc_dropout_v4 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v4.npy','rb'))
pn_num_and_case_num_v4 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v4.npy','rb'))

print(pseudo_labels_v4.shape)

pseudo_sequences_v5 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v5.npy",'rb'))
pseudo_masks_v5 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v5.npy",'rb'))
pseudo_type_ids_v5 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v5.npy",'rb'))
pseudo_labels_v5 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v5.npy",'rb'))
labels_check_mc_dropout_v5 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v5.npy','rb'))
pn_num_and_case_num_v5 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v5.npy','rb'))

print(pseudo_labels_v5.shape)

pseudo_sequences_v6 = np.load(open(f"{GCF.PSEUDO_DIR}/sequences_pseudo_v6.npy",'rb'))
pseudo_masks_v6 = np.load(open(f"{GCF.PSEUDO_DIR}/masks_pseudo_v6.npy",'rb'))
pseudo_type_ids_v6 = np.load(open(f"{GCF.PSEUDO_DIR}/token_ids_pseudo_v6.npy",'rb'))
pseudo_labels_v6 = np.load(open(f"{GCF.PSEUDO_DIR}/labels_pseudo_v6.npy",'rb'))
labels_check_mc_dropout_v6 = np.load(open(f'{GCF.PSEUDO_DIR}/labels_check_mc_dropout_v6.npy','rb'))
pn_num_and_case_num_v6 = np.load(open(f'{GCF.PSEUDO_DIR}/pn_num_and_case_num_v6.npy','rb'))

print(pseudo_labels_v6.shape)

pseudo_sequences = np.vstack([pseudo_sequences_v1, pseudo_sequences_v2, pseudo_sequences_v3, pseudo_sequences_v4, pseudo_sequences_v5, pseudo_sequences_v6])
pseudo_masks = np.vstack([pseudo_masks_v1, pseudo_masks_v2, pseudo_masks_v3, pseudo_masks_v4, pseudo_masks_v5, pseudo_masks_v6])
pseudo_type_ids = np.vstack([pseudo_type_ids_v1, pseudo_type_ids_v2, pseudo_type_ids_v3, pseudo_type_ids_v4, pseudo_type_ids_v5, pseudo_type_ids_v6])
pseudo_labels = np.vstack([pseudo_labels_v1, pseudo_labels_v2, pseudo_labels_v3, pseudo_labels_v4, pseudo_labels_v5, pseudo_labels_v6])
labels_check_mc_dropout = np.vstack([labels_check_mc_dropout_v1, labels_check_mc_dropout_v2,
                                     labels_check_mc_dropout_v3, labels_check_mc_dropout_v4, labels_check_mc_dropout_v5, labels_check_mc_dropout_v6])
pseudo_case_num = np.vstack([pn_num_and_case_num_v1, pn_num_and_case_num_v2,
                                     pn_num_and_case_num_v3, pn_num_and_case_num_v4, pn_num_and_case_num_v5, pn_num_and_case_num_v6])[:, 1]
print(pseudo_labels.shape)

def pseudo_to_target(pred):
    if pred == 1:
        return 1
    elif pred == 0:
        return 0
    else:
        return -1

new_labels = []
for p, l in zip(labels_check_mc_dropout, pseudo_labels):
    new_label = np.array([-1 if i == -1 else pseudo_to_target(j) for i, j in zip(l, p)])
    new_labels.append(new_label)
new_labels = np.stack(new_labels)

print(new_labels.shape)

is_posi = [l[l != -1].sum() > 0 for l in new_labels]

pseudo_sequences = pseudo_sequences[is_posi, :]
pseudo_masks = pseudo_masks[is_posi, :]
pseudo_type_ids = pseudo_type_ids[is_posi, :]
pseudo_labels = new_labels[is_posi, :]
pseudo_case_num = pseudo_case_num[is_posi]

print(pseudo_labels.shape)

n_pseudo_data = pseudo_labels.shape[0]

kf = StratifiedKFold(n_splits=GCF.N_FOLDS, random_state=GCF.SEED, shuffle=True)
splits = list(kf.split(X=pseudo_case_num , y=pseudo_case_num))
pseudo_fold_index = [train_idx for train_idx, valid_idx in splits]
pseudo_fold_index

class NBMEDataset(Dataset):
    def __init__(self, sequences, mask, type_ids, target):
        self.sequences = sequences
        self.mask = mask
        self.type_ids = type_ids
        self.target = target
        
    def __len__(self):
        return len(self.sequences)
    
    def __getitem__(self, item):
        sequences = self.sequences[item, :]
        mask = self.mask[item, :]
        type_ids = self.type_ids[item, :]
        target = self.target[item, :]
        d = {
            "sequences": torch.tensor(sequences).long(),
            "mask": torch.tensor(mask).long(),
            "type_ids": torch.tensor(type_ids).long(),
            "target" : torch.tensor(target).float(),
        }
        return d

class NBMEModel(nn.Module):
    
    def __init__(self):
        super(NBMEModel, self).__init__()
        self.transformer = AutoModel.from_pretrained(
            GCF.MODEL_NAME, 
            output_hidden_states=True
        )
        self.fc_dropout = nn.Dropout(0.2)
        self.classifier = nn.Linear(GCF.CONFIG.hidden_size, 1)
        
        self._init_weights(self.classifier)
    
    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            module.weight.data.normal_(mean=0.0, std=GCF.CONFIG.initializer_range)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            module.weight.data.normal_(mean=0.0, std=GCF.CONFIG.initializer_range)
            if module.padding_idx is not None:
                module.weight.data[module.padding_idx].zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)
            
    def forward(self, input_ids, attention_mask, token_type_ids, target=None, pseudo=None):
        outputs = self.transformer(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )
        h = outputs['last_hidden_state']
        h = self.fc_dropout(h)
        h = self.classifier(h)
        h = h.squeeze(-1)
        if target is not None:
            loss = nn.BCEWithLogitsLoss(reduction="none")(h, target)
            if pseudo is not None:
                mask = (target - (torch.ones(attention_mask.shape).to(device) * pseudo.unsqueeze(1))) >= 0
            else:
                mask = target != -1
            loss = torch.masked_select(loss, mask).mean()
        else:
            loss = 0
        loss = loss / GCF.ACCUMULATE
        return loss, h

def train_loop(model, train_dloader, optimizer, scheduler):
    lrs, losses = [], []
    model.train()
    global_step = 0
    for idx, d in tqdm(enumerate(train_dloader), total=len(train_dloader)):
        with torch.cuda.amp.autocast(): 
            loss, _ = model(
                d['sequences'].to(device),
                d['mask'].to(device),
                d['type_ids'].to(device),
                d['target'].to(device),
            )
        scaler.scale(loss).backward()
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1000)
        if global_step % GCF.ACCUMULATE == 0:
            scaler.step(optimizer) 
            scaler.update() 
            optimizer.zero_grad()
            scheduler.step()

        lr = np.array([param_group["lr"] for param_group in optimizer.param_groups]).mean()
        lrs.append(lr.item())
        losses.append(loss.item())
        global_step += 1
    return losses, lrs


def valid_loop(model, valid_dloader):
    losses, predicts = [], []
    model.eval()
    for idx, d in tqdm(enumerate(valid_dloader), total=len(valid_dloader)):
        with torch.no_grad():
            loss, pred = model(d['sequences'].to(device), d['mask'].to(device), d['type_ids'].to(device), d['target'].to(device))
            losses.append(loss.item())
            predicts.append(pred.cpu().sigmoid())
    predicts = torch.vstack(predicts)
    valid_loss = np.mean(losses)
    
    return valid_loss, predicts

# https://www.kaggle.com/theoviel/evaluation-metric-folds-baseline#Metric
    
def micro_f1(preds, truths):
    """
    Micro f1 on binary arrays.

    Args:
        preds (list of lists of ints): Predictions.
        truths (list of lists of ints): Ground truths.

    Returns:
        float: f1 score.
    """
    # Micro : aggregating over all instances

    preds = np.concatenate(preds)
    truths = np.concatenate(truths)

    return f1_score(truths, preds)

def spans_to_binary(spans, length=None):
    """
    Converts spans to a binary array indicating whether each character is in the span.

    Args:
        spans (list of lists of two ints): Spans.

    Returns:
        np array [length]: Binarized spans.
    """
    length = np.max(spans) if length is None else length
    binary = np.zeros(length)
    for start, end in spans:
        binary[start:end] = 1
    
    return binary

def span_micro_f1(preds, truths):
    """
    Micro f1 on spans.

    Args:
        preds (list of lists of two ints): Prediction spans.
        truths (list of lists of two ints): Ground truth spans.

    Returns:
        float: f1 score.
    """
        
    bin_preds = []
    bin_truths = []
    
    for pred, truth in zip(preds, truths):
        if not len(pred) and not len(truth):
            continue

        length = max(np.max(pred) if len(pred) else 0, np.max(truth) if len(truth) else 0)
        bin_preds.append(spans_to_binary(pred, length))
        bin_truths.append(spans_to_binary(truth, length))
        
    return micro_f1(bin_preds, bin_truths)

def decode_location(locations):
    for x in ["[","]","'"]:
        locations = locations.replace(x,'')
    locations = locations.replace(',',';')
    locations = locations.split(";")
    res = []
    for location in locations:
        if location:
            x,y = location.split()
            res.append([int(x),int(y)])
    return sorted(res,key=lambda x:x[0])

def decode_position(pos):
    return ";".join([" ".join(np.array(p).astype(str)) for p in pos])

def create_labels_for_scoring(df):
    # example: ['0 1', '3 4'] -> ['0 1; 3 4']
    df['location_for_create_labels'] = [ast.literal_eval(f'[]')] * len(df)
    for i in range(len(df)):
        lst = df.loc[i, 'location']
        if lst:
            new_lst = ';'.join(lst)
            df.loc[i, 'location_for_create_labels'] = ast.literal_eval(f'[["{new_lst}"]]')
    # create labels
    truths = []
    for location_list in df['location_for_create_labels'].values:
        truth = []
        if len(location_list) > 0:
            location = location_list[0]
            for loc in [s.split() for s in location.split(';')]:
                start, end = int(loc[0]), int(loc[1])
                truth.append([start, end])
        truths.append(truth)
    return truths


def get_char_probs(texts, predictions, tokenizer):
    results = [np.zeros(len(t)) for t in texts]
    for i, (text, prediction) in enumerate(zip(texts, predictions)):
        encoded = tokenizer(text, 
                            add_special_tokens=True,
                            return_offsets_mapping=True)
        for idx, (offset_mapping, pred) in enumerate(zip(encoded['offset_mapping'], prediction)):
            start = offset_mapping[0]
            end = offset_mapping[1]
            results[i][start:end] = pred
    return results


def get_results(char_probs, th=0.5):
    results = []
    for char_prob in char_probs:
        result = np.where(char_prob >= th)[0] + 1
        result = [list(g) for _, g in itertools.groupby(result, key=lambda n, c=itertools.count(): n - next(c))]
        result = [f"{min(r)} {max(r)}" for r in result]
        result = ";".join(result)
        results.append(result)
    return results


def get_predictions(results):
    predictions = []
    for result in results:
        prediction = []
        if result != "":
            for loc in [s.split() for s in result.split(';')]:
                start, end = int(loc[0]), int(loc[1])
                prediction.append([start, end])
        predictions.append(prediction)
    return predictions

def get_score(y_true, y_pred):
    score = span_micro_f1(y_true, y_pred)
    return score

def get_optimizer_params(model):
    param_optimizer = list(model.named_parameters())
    no_decay = ["bias", "LayerNorm.bias", "LayerNorm.weight"]
    optimizer_parameters = [
        {'params': [p for n, p in model.transformer.named_parameters() if not any(nd in n for nd in no_decay)],
         'lr': GCF.LR, 'weight_decay': GCF.WEIGHT_DECAY},
        {'params': [p for n, p in model.transformer.named_parameters() if any(nd in n for nd in no_decay)],
         'lr': GCF.LR, 'weight_decay': 0.0},
        {'params': [p for n, p in model.named_parameters() if "transformer" not in n],
         'lr': GCF.LR, 'weight_decay': 0.0}
    ]
    return optimizer_parameters

all_scores = []
oof = np.zeros(labels.shape)
for fold in range(GCF.N_FOLDS):
    #if fold in [0,1,2,3]:
    #    print(f'### skip Fold-{fold} ###')
    #    continue
    print(f'### start Fold-{fold} ###')
    set_seed()
    
    valid_sequences = sequences[pn_num_folds == fold, :]
    valid_masks = masks[pn_num_folds == fold, :]
    valid_type_ids = type_ids[pn_num_folds == fold, :]
    valid_labels = labels[pn_num_folds == fold,:]
    valid_dset = NBMEDataset(valid_sequences, valid_masks, valid_type_ids, valid_labels)
    valid_dloader = DataLoader(valid_dset, batch_size=GCF.BS,
                               pin_memory=True, shuffle=False, drop_last=False, num_workers=os.cpu_count())

    #train_sequences = np.vstack([sequences[pn_num_folds != fold, :], pseudo_sequences[pseudo_fold_index[fold], :]])
    #train_masks = np.vstack([masks[pn_num_folds != fold, :], pseudo_masks[pseudo_fold_index[fold], :]])
    #train_type_ids = np.vstack([type_ids[pn_num_folds != fold, :], pseudo_type_ids[pseudo_fold_index[fold], :]])
    #train_labels = np.vstack([labels[pn_num_folds != fold, :], pseudo_labels[pseudo_fold_index[fold], :]])
    #train_dset = NBMEDataset(train_sequences, train_masks, train_type_ids, train_labels)
    #train_dloader = DataLoader(train_dset, batch_size=GCF.BS,
    #                           pin_memory=True, shuffle=True, drop_last=True, num_workers=os.cpu_count(),
    #                           worker_init_fn=lambda x: set_seed())

    pseudo_idx = np.array(random.sample(range(n_pseudo_data), 6000))
    train_sequences = np.vstack([sequences[pn_num_folds != fold, :], pseudo_sequences[pseudo_idx, :]])
    train_masks = np.vstack([masks[pn_num_folds != fold, :], pseudo_masks[pseudo_idx, :]])
    train_type_ids = np.vstack([type_ids[pn_num_folds != fold, :], pseudo_type_ids[pseudo_idx, :]])
    train_labels = np.vstack([labels[pn_num_folds != fold, :], pseudo_labels[pseudo_idx, :]])
    train_dset = NBMEDataset(train_sequences, train_masks, train_type_ids, train_labels)
    train_dloader = DataLoader(train_dset, batch_size=GCF.BS,
                               pin_memory=True, shuffle=True, drop_last=True, num_workers=os.cpu_count(),
                               worker_init_fn=lambda x: set_seed())

    model = NBMEModel()
    model.to(device)
    
    wandb.init(
        project="NBME",
        config={k: v for k, v in dict(vars(GCF)).items() if k[:2] != "__" and k not in GCF.NOT_WATCH_PARAM},
        entity='trtd56',
        name=f"{GCF.EXP_NAME}_f{fold}",
    )
    wandb.config.update({'fold': fold, 'exp_name': GCF.EXP_NAME})
    wandb.watch(model)

    optimizer = AdamW(get_optimizer_params(model), lr=GCF.LR, weight_decay=GCF.WEIGHT_DECAY)
    max_train_steps = GCF.N_EPOCHS * len(train_dloader) // GCF.ACCUMULATE
    warmup_steps = int(max_train_steps * GCF.WARM_UP_RATIO)
    scheduler = get_cosine_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=max_train_steps
    )

    if os.path.exists(f"{GCF.OUTPUT_DIR}/checkpoint.bin"):
        print('load prev model')
        checkpoint = torch.load(f"{GCF.OUTPUT_DIR}/checkpoint.bin") 
        model.load_state_dict(checkpoint["model"])
        optimizer.load_state_dict(checkpoint["optimizer"])
        scheduler.load_state_dict(checkpoint["scheduler"])
        random.setstate(checkpoint["random"])
        np.random.set_state(checkpoint["np_random"])
        torch.set_rng_state(checkpoint["torch"])
        torch.random.set_rng_state(checkpoint["torch_random"])
        torch.cuda.set_rng_state(checkpoint["cuda_random"])
        is_load = True
        best_score = 0.8941
        del checkpoint
    else:
        is_load = False
        best_score = 0
    torch.cuda.empty_cache()
    gc.collect()
    
    train_losses, train_lrs = [], []
    for epoch in range(GCF.N_EPOCHS):
        #if is_load and epoch < 4:
        #    print(f'skip epoch-{epoch}')
        #    continue
        _losses, _lrs = train_loop(model, train_dloader, optimizer, scheduler)
        valid_loss, valid_predicts = valid_loop(model, valid_dloader)
        
        predictions = oof[train_df['fold'] == fold]
        valid_texts = train_df[train_df['fold'] == fold]['pn_history']
        valid_df = train_df[train_df['fold'] == fold].reset_index(drop=True)
        valid_df['location'] = valid_df['location'].apply(ast.literal_eval)
        valid_labels = create_labels_for_scoring(valid_df)
        char_probs = get_char_probs(valid_texts, valid_predicts, GCF.TOKENIZER)
        results = get_results(char_probs, th=0.5)
        preds = get_predictions(results)
        f1score = get_score(valid_labels, preds)
        
        print(f"epoch-{epoch}: valid_loss={valid_loss}, valid_f1_score={f1score}")
        train_losses += _losses
        train_lrs += _lrs
        oof[pn_num_folds == fold, :] = valid_predicts
        if best_score < f1score:
            print('save best model')
            best_score = f1score
            if is_load:
                torch.save(model.state_dict(), f"{GCF.OUTPUT_DIR}/nbme_f{fold}_best_model_rerun.bin")
            else:
                torch.save(model.state_dict(), f"{GCF.OUTPUT_DIR}/nbme_f{fold}_best_model.bin")
                
        wandb.log({
                "train_loss": np.mean(_losses),
                "valid_loss": valid_loss,
                "valid_score": f1score,
                "valid_best_score": best_score,
                "learning_rate": np.mean(_lrs),
        })

        checkpoint = {
            "model": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "scheduler": scheduler.state_dict(),
            "random": random.getstate(),
            "np_random": np.random.get_state(),
            "torch": torch.get_rng_state(),
            "torch_random": torch.random.get_rng_state(),
            "cuda_random": torch.cuda.get_rng_state(),
        }
        torch.save(checkpoint, f"{GCF.OUTPUT_DIR}/checkpoint.bin")

        # train dataの再サンプリング
        pseudo_idx = np.array(random.sample(range(n_pseudo_data), 6000))
        train_sequences = np.vstack([sequences[pn_num_folds != fold, :], pseudo_sequences[pseudo_idx, :]])
        train_masks = np.vstack([masks[pn_num_folds != fold, :], pseudo_masks[pseudo_idx, :]])
        train_type_ids = np.vstack([type_ids[pn_num_folds != fold, :], pseudo_type_ids[pseudo_idx, :]])
        train_labels = np.vstack([labels[pn_num_folds != fold, :], pseudo_labels[pseudo_idx, :]])
        train_dset = NBMEDataset(train_sequences, train_masks, train_type_ids, train_labels)
        train_dloader = DataLoader(train_dset, batch_size=GCF.BS,
                                pin_memory=True, shuffle=True, drop_last=True, num_workers=os.cpu_count(),
                                worker_init_fn=lambda x: set_seed())
            
    plt.plot(train_losses);plt.show()
    plt.plot(train_lrs);plt.show()

    os.remove(f"{GCF.OUTPUT_DIR}/checkpoint.bin")
    del checkpoint
    torch.cuda.empty_cache()
    gc.collect()
    wandb.finish()

    
    #break #only one fold

#wandb.finish()

oof = np.zeros(labels.shape)
for fold in range(GCF.N_FOLDS):
    print(fold)
    set_seed()
    
    valid_sequences = sequences[pn_num_folds == fold, :]
    valid_masks = masks[pn_num_folds == fold, :]
    valid_type_ids = type_ids[pn_num_folds == fold, :]
    valid_labels = labels[pn_num_folds == fold,:]
    
    valid_dset = NBMEDataset(valid_sequences, valid_masks, valid_type_ids, valid_labels)
    valid_dloader = DataLoader(valid_dset, batch_size=GCF.BS,
                               pin_memory=True, shuffle=False, drop_last=False, num_workers=os.cpu_count())
    
    model = NBMEModel()
    model.to(device)
    if fold in [-1]:
        model.load_state_dict(torch.load(f'{GCF.OUTPUT_DIR}/nbme_f{fold}_best_model_rerun.bin'))
    else:
        model.load_state_dict(torch.load(f'{GCF.OUTPUT_DIR}/nbme_f{fold}_best_model.bin'))
    
    valid_loss, valid_predicts = valid_loop(model, valid_dloader)
    oof[pn_num_folds == fold, :] = valid_predicts

    torch.cuda.empty_cache()
    gc.collect()

np.save(open(f"{GCF.OUTPUT_DIR}/oof.npy",'wb'), oof)

scores = []
for fold in range(GCF.N_FOLDS):
    print("Fold", fold)
    predictions = oof[train_df['fold'] == fold]
    valid_texts = train_df[train_df['fold'] == fold]['pn_history']
    valid_df = train_df[train_df['fold'] == fold].reset_index(drop=True)
    valid_df['location'] = valid_df['location'].apply(ast.literal_eval)
    valid_labels = create_labels_for_scoring(valid_df)
    char_probs = get_char_probs(valid_texts, predictions, GCF.TOKENIZER)
    results = get_results(char_probs, th=0.5)
    preds = get_predictions(results)
    score = get_score(valid_labels, preds)
    scores.append(score)
    print(score)
    
print('CV', np.mean(scores))

def optim_thr(thr):
    scores = []
    for fold in range(GCF.N_FOLDS):
        predictions = oof[train_df['fold'] == fold]
        valid_texts = train_df[train_df['fold'] == fold]['pn_history']
        valid_df = train_df[train_df['fold'] == fold].reset_index(drop=True)
        valid_df['location'] = valid_df['location'].apply(ast.literal_eval)
        valid_labels = create_labels_for_scoring(valid_df)
        char_probs = get_char_probs(valid_texts, predictions, GCF.TOKENIZER)
        results = get_results(char_probs, th=thr)
        preds = get_predictions(results)
        score = get_score(valid_labels, preds)
        scores.append(score)
    return np.mean(scores)

for i in range(11):
    thr = round(i*0.02 + 0.4, 2)
    print(thr)
    s = optim_thr(thr)
    print('  ->', s)

