nvidia-smi -l 1 or nvidia-smi
export CUDA_VISIBLE_DEVICES=2,3


modiule load miniconda3
module load python/3.7.7
conda activate base
conda activate obj_det



paths to outputs from training and testing
/import/c4dm-05/elona/3541_doremi/text-outputs/train-output
/import/c4dm-05/elona/3541_doremi/text-outputs/test-output
paths to checkpoints 
/import/c4dm-05/elona/3541_doremi/checkpoints
export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/
export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/object_detection
export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/slim

Naming conventions
1. Type: Faster-R-CNN
2. network type: inception 
3. number of classes
4. number of files
5. number of steps 
6. date of starting experiments


Experiments May 2023 - ared one for the Doremi v2 paper to check if the generated images help with detection. 

Training, test and validation and mappings data path:
/homes/es314/DV2-2023/train_validation_test_records

Minidirs:
mapping.json  mapping.txt  Stats_all_pages.csv  test.tfrecords  train.tfrecords  validate.tfrecords
Mappings of classes
/homes/es314/DV2-2023/train_validation_test_records/mapping.txt



export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/
export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/object_detection
export PYTHONPATH=$PYTHONPATH:/homes/es314/DOREMI/music_object_detector/research/object_detection
nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/train.py --logtostderr --train_dir=/import/c4dm-05/elona/may_2023_ex001/train --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config --checkpoint_dir=/import/c4dm-05/elona/may_2023_ex001/train > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001-2.txt &



Frozen data model used: 
/import/c4dm-05/elona/3541_doremi/frozen_data_models/faster_rcnn_inception_resnet_v2_atrous_coco_2018_01_28/model.ckpt

conda activate obj_det

pip install tensorflow==1.15.4
pip install pycocotools==2.0.0
pip install protobuf==3.6.0


ERROR: tensorflow-gpu 1.15.4 has requirement protobuf>=3.6.1, but you'll have protobuf 3.6.0 which is incompatible.
ERROR: tensorflow-gpu 1.15.4 has requirement tensorboard<1.16.0,>=1.15.0, but you'll have tensorboard 2.11.2 which is incompatible.
ERROR: tensorflow-gpu 1.15.4 has requirement tensorflow-estimator==1.15.1, but you'll have tensorflow-estimator 2.11.0 which is incompatible.
ERROR: tensorboard 2.11.2 has requirement protobuf<4,>=3.9.2, but you'll have protobuf 3.6.0 which is incompatible.
ERROR: requests 2.29.0 has requirement urllib3<1.27,>=1.21.1, but you'll have urllib3 2.0.2 which is incompatible.
ERROR: tensorflow 2.11.0 has requirement numpy>=1.20, but you'll have numpy 1.18.5 which is incompatible.
ERROR: tensorflow 2.11.0 has requirement protobuf<3.20,>=3.9.2, but you'll have protobuf 3.6.0 which is incompatible.

Config file: 

/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config

Training dir name and dir:
/import/c4dm-05/elona/may_2023_ex001/train

Test dir name and dir:
/import/c4dm-05/elona/may_2023_ex001/validate

nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/train.py \
    --logtostderr \
    --train_dir=/import/c4dm-05/elona/may_2023_ex001/train \
    --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config \
     > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001.txt &

nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/train.py --logtostderr --train_dir=/import/c4dm-05/elona/may_2023_ex001/train --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001.txt &
this was to step 7400

to continue training:

nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/train.py --logtostderr --train_dir=/import/c4dm-05/elona/may_2023_ex001/train --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config --checkpoint_dir=/import/c4dm-05/elona/may_2023_ex001/train > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001-2.txt &


Test

python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/eval.py 
--logtostderr 
--pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config 
--checkpoint_dir=/import/c4dm-05/elona/may_2023_ex001/train 
--eval_dir=/import/c4dm-05/elona/may_2023_ex001/validate 
> /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001_validate.txt &


nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/eval.py --logtostderr --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config --checkpoint_dir=/import/c4dm-05/elona/may_2023_ex001/train --eval_dir=/import/c4dm-05/elona/may_2023_ex001/validate > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001_validate.txt &


nohup python /homes/es314/DOREMI/music_object_detector/research/object_detection/legacy/eval.py --logtostderr --pipeline_config_path=/homes/es314/DV2-2023/Faster_R-CNN_inception-003.config --checkpoint_dir=/import/c4dm-05/elona/may_2023_ex001/train --eval_dir=/import/c4dm-05/elona/may_2023_ex001/validate > /import/c4dm-05/elona/may_2023_ex001/text-output/exp_001-2_validate.txt &
Server used: hepworth



tensorboard:

export PATH=$PATH:/homes/es314/miniconda3/envs/musicreco/bin

bash-4.2$ tensorboard --logdir=/import/c4dm-05/elona/may_2023_ex001/ --host localhost --port 8885


no module named nets:
