# Android_API_Count

![GitHub last commit](https://img.shields.io/github/last-commit/rouxianmantou/Android_API_Count)

## 环境：Python3 / Bash

## 使用方法：
1. git clone https://github.com/rouxianmantou/Android_API_Count.git
2. cd Android_API_Count
3. 将要统计的包的**整体文件夹**放到 /[your path..]/Android_API_Count/target下
4. chmod +x batch_count.sh
5. ./batch_count.sh
6. 统计结果放在/result下，有单独模块的result_xxx.txt，也有结果集合参考result_all.txt
7. 单个统计输出如下图所示
8. 删除/[your path..]/Android_API_Count/target中的内容

![output_img](output_img.jpg)
___
## 批量下载和统计方法
1. 将要统计的github repo名称放到clone_lib_list中。如：gyf-dev/ImmersionBar
2. chmod +x clone_and_count_lib_in_target.sh
3. ./clone_and_count_lib_in_target.sh
4. 分别在/target和/result查看clone log，统计结果等信息。
___
## Tips and Tricks
1. 只统计.java文件，暂不支持.kt等文件。
2. 可以自行修改sdkApi.txt。
3. 部分log信息，统计结果等在下次统计时可能会被覆盖，请及时保存。