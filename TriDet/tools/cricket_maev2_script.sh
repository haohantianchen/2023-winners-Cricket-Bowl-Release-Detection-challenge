#!/bin/bash

echo "start training"
CUDA_VISIBLE_DEVICES=$1 python train.py ./configs/cricket_maev2.yaml --output train_mae
echo "start testing..."
CUDA_VISIBLE_DEVICES=$1 python eval.py ./configs/cricket_maev2.yaml ckpt/cricket_maev2_train_mae/epoch_039.pth.tar --saveonly
