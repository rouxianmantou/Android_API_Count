#!/bin/sh

lib_list_path=`pwd`/count_lib_list
result_path=`pwd`/result_stars.txt
token_path=`pwd`/github_token

github_token=`cat $token_path`
github_base_url="https://api.github.com/repos/"

echo "" > $result_path

cat $lib_list_path | awk '{print $0}' | while read line
do
    tar_url=$github_base_url$line
    echo $tar_url
    echo $tar_url","`python3 count_star.py $tar_url $github_token` >> $result_path
done
