#!/bin/sh
#请参考clone_lib_list的sample list
#e.g. gyf-dev/ImmersionBar 

abs_tar_path="/target"
abs_result_path="/result"

abs_list_path="/clone_lib_list"
result_path=`pwd`$abs_result_path

lib_path=`pwd`$abs_tar_path
clone_lib_list_path=`pwd`$abs_list_path

cd target
echo "" > $lib_path/git_clone_info.log
download_index=0

cat $clone_lib_list_path | awk '{print $0}' | while read line
do 
    download_index=`expr $download_index + 1`
    echo $download_index >> $lib_path/git_clone_info.log
    echo "START CLONE -> $line"
    echo "$line" >> $lib_path/git_clone_info.log

    # if ! `git clone https://github.com/"$line" --progress --depth 1 --single-branch`
    if ! `git clone https://github.com/"$line"`
    then
      echo "FAILED!!!!!!" >> $lib_path/git_clone_info.log
    else
      echo "OK!" >> $lib_path/git_clone_info.log
    fi
    echo "************************************************************************************************************************" >> git_clone_info.log
    echo "" >> git_clone_info.log
    echo "DONE CLONE -> $line"
    echo "************************************************************************************************************************"
done
cd ..

chmod +x batch_count_excluded_api.sh
./batch_count_excluded_api.sh