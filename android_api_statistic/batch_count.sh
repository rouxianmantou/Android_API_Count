#!/bin/sh  

abs_tar_path="/target"
abs_result_path="/result"

lib_path=`pwd`$abs_tar_path
result_path=`pwd`$abs_result_path
echo "" > $result_path/result_all.txt

for find_dirs in ${lib_path}/*
do
    if [ -d $find_dirs ]
    then
    echo "START COUNTING $find_dirs"
    tar_basename=`basename $find_dirs`
    touch $result_path$abs_result_path"_"$tar_basename.txt

    #第一行为文件夹名
    echo `basename $find_dirs` > $result_path$abs_result_path"_"$tar_basename.txt

    #开始统计
    python3 count_import.py $find_dirs >> $result_path$abs_result_path"_"$tar_basename.txt 

    #写入result_all.txt
    cat $result_path$abs_result_path"_"$tar_basename.txt | awk '{print $0}' | while read line
    do
    echo $line >> $result_path/result_all.txt
    done

    echo "" >> $result_path/result_all.txt
    echo "" >> $result_path/result_all.txt
    fi
done