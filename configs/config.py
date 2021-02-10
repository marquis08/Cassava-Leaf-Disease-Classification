import os
import cv2
import albumentations as A
abs_path = os.path.dirname(__file__)

import psutil
n_jobs = psutil.cpu_count()


args = {
    "SEED":42,
    "n_folds":10,
    "epochs":100, 
    "num_classes":5,
    "input_size":512,
    "batch_size":64,
    "infer_batch_size":64,
    "infer_model_path":'',
    "infer_best_model_name":'',
    "num_workers":n_jobs,
    "model":"vit_small_patch16_224", # tf_efficientnet_b2_ns, vit_base_patch16_384, vit_small_patch16_224 "vit_small_patch16_224"
    "optimizer":"AdamW",
    "scheduler":"warmup",
    "lr":0.00025,   # 0.00025
    "weight_decay":0.0,
    "center_pad":True,
    "train_augments":'random_crop, horizontal_flip, vertical_flip, random_rotate, random_grayscale',
    "valid_augments":'horizontal_flip, vertical_flip',
    "augment_ratio":0.5,
    "masking_type":None,
    "max_mask_num":3,
    "label_smoothing":True,
    "label_smoothing_ratio":0.1,
    "pretrained":True,
    "lookahead":False,
    "k_param":5,
    "alpha_param":0.5,
    "patience":3,
    "albu": False,
    "clahe":True,
    "fp16": True,
    "grayscale": False,
    "DEBUG":False
}
