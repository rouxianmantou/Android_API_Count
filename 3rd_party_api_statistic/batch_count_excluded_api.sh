#!/bin/sh  

abs_tar_path="/target"
abs_result_path="/result"

lib_path=`pwd`$abs_tar_path
result_path=`pwd`$abs_result_path

for find_dirs in ${lib_path}/*
do
    if [ -d $find_dirs ]
    then
    echo "START COUNTING $find_dirs"
    tar_basename=`basename $find_dirs`
    touch $result_path$abs_result_path"_"$tar_basename"_excluded".txt

        #第一行为文件夹名
    echo `basename $find_dirs` > $result_path$abs_result_path"_"$tar_basename"_excluded".txt

    python3 count_3rd_party_api.py $find_dirs >> $result_path$abs_result_path"_"$tar_basename"_excluded".txt
    fi
done
