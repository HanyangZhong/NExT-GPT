# RobotGPT
 Use NEXT-GPT to add other multi modal ability
 ![87d226193dfe9d894651013c31d4c01](https://github.com/HanyangZhong/NExT-GPT/assets/119017394/84ea71b8-0b08-49fe-8324-097b5a89a028)

# The current progress 
## Pretrain
### Image encoder
The dataset is CC3M,  the same as the LLaVA ones.  
Dataset web: [LLaVA pretrain Images Json](https://huggingface.co/datasets/liuhaotian/LLaVA-CC3M-Pretrain-595K)  
Images:    
```
链接：https://pan.baidu.com/s/1eQbfEK07DaKo2HzdFXwN7A 
提取码：pu68 
--来自百度网盘超级会员V7的分享
```
### Audio encoder
The audio dataset is audiocaps.  
Audio Dataset:   
```
链接：https://pan.baidu.com/s/1TQgvo056Vejj-Y95dqoZpQ 
提取码：88xc 
--来自百度网盘超级会员V7的分享
```
Detail setting for Json file: /pretrain/audiocap_setup.zip  
In check_files.py, it would be suggested to set files at least larger than 100k.  
That can help reducing dataset problem.

### Depth encoder
The RGBD dataset is washington-RGBD.  
RGBD Dataset:   
```
https://paperswithcode.com/dataset/washington-rgb-d
```

## Finetuning
Not tested yet

## Cli inference
Not finished testing yet
