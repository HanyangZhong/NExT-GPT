1.从百度云盘下载audiocap的数据集，可以不用全下
2.将所有音频文件放到同一个文件夹下
3.运行check_files.py 将过小的文件删除，可能是已损坏文件
4.基于llava格式，运行format_llava_json.py 记得更改路径地址  最后生成出用于执行的json文件格式
4.基于NExT-GPT格式，运行format_nextgpt_json.py 记得更改路径地址  最后生成出用于执行的json文件格式