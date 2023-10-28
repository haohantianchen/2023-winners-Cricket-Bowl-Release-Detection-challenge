# Relative Boundary Modeling

[[Paper]](https://dl.acm.org/doi/10.1145/3606038.3616167) [[Challenge]](http://mmsports.multimedia-computing.de/mmsports2023/challenge.html)

Code for the paper: `Relative Boundary Modeling: A High-Resolution Cricket Bowl Release Detection Framework with I3D Features`

Tips: We have improved our approach by extracting video features using VideoMAEv2!

## Installation

1. Please ensure that you have installed PyTorch and CUDA.

2. Install the required packages by running the following command:

```shell
pip install  -r requirements.txt
```

3. Install NMS

```shell
cd ./TriDet/libs/utils
python setup.py install --user
cd ../..
```

4. Done! We are ready to get start!

## Data Preparation

- We used VideoMAEv2 to extract features from all the videos in the Cricket Bowl Release Dataset. You can directly use 
  the script we provided. To facilitate reproducing our results, we also provide the extracted features in .npy files
  (https://drive.google.com/drive/folders/1YHQCBtJZseZ0nW41hr2HakKkcx_wnbac?usp=drive_link).


- Please unpack the MAEv2 features into `./TriDet/data/maev2_factures`. 
  We provide processed annotation json file for the MAEv2 features in the `./TriDet/data/annotations` folder.

## Extract feature

Use `./VideoMAEv2/extract_tad_feature.py` to extract the feature of datasets, You can obtain the ckpt (.pth) file 
through a Google Drive link(https://drive.google.com/drive/folders/1tMHPU4yFVVRoGEmwIY3OCLqF-bbz_lf0?usp=drive_link). 
For example, to extract the feature of Cricket Bowl Release Dataset, running the following command:
```bash
python extract_tad_feature.py \
    --data_set THUMOS14 \
    --data_path YOUR_PATH/videos \
    --save_path YOUR_PATH/th14_vit_g_16_4 \
    --model vit_giant_patch14_224 \
    --ckpt_path YOUR_PATH/vit_g_hyrbid_pt_1200e_k710_ft.pth
```

## Quick Start

We provide a script that allow you to reproduce our results with just one click. These scripts are located in
the `./TriDet/tools` folder :

- cricket_maev2_script.sh

To easily reproduce our results, simply run the following command:

```shell
bash SCRIPT_PATH GPU_NUM
```

For example, if you want to train and eval our model on Cricket Bowl Release Dataset using the first GPU on you machine, you can
run:

```shell
bash TriDet/tools/cricket_maev2_script.sh 0
```

## Test

The command for test is

```shell
python eval.py ./configs/CONFIG_FILE PATH_TO_CHECKPOINT
```

## PKL2JSON and Post_processing

After running eval.py file, you will obtain a .pkl file. 

- Use `./tools/pkl2json.py` to convert the .pkl file into the JSON format required for submission.

- Use `./tools/post_processing.py` to achieve our post-processing operations.

Tips: Don't forget to modify the file paths.
