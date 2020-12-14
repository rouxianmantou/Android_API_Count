#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import re

#读取当前已知的api文件
current_known_api_list = []
with open('sdkApi.txt','r',encoding='UTF-8') as f:
    for line in f.readlines():
         current_known_api_list.append(line.strip("\n"))
print("目前参与统计Android API大类数量为：",len(current_known_api_list))
print("添加和修改sdkApi.txt时，请注意不要添加重复类和大类下的小类")
print("统计路径为："+ os.getcwd() + '/target')
print("*************************************************************************")
print("*************************************************************************")
print("START START START START START START START START START START START START START START START")

#标记已经出现的API
appeared_api_list=[]

#标记api大类中，出现的API个数
#无用的列表
appeared_api_cnt=[0]*len(current_known_api_list)

#统计所有已知API个数
appeared_all_cnt=0

#记录未被计数的API,以供手动检查
api_not_included=[]

for i in range(0,len(current_known_api_list)):
    appeared_api_cnt[i]=0 


java_pattern = re.compile(r'^[a-zA-Z_\$\u4e00-\u9fa5][\w_\$\u4e00-\u9fa5]+\.java$')

for home, dirs, files in os.walk(os.getcwd() + '/target'):
    for filename in files:
        if(re.match(java_pattern,filename)!=None):
            fullname = os.path.join(home, filename)
            with open(fullname ,mode='r',encoding='UTF-8') as file_obj:
                try:
                    for line in file_obj:
                        if(line.startswith('import')):
                            is_other_api=True
                            for i in range(0,len(current_known_api_list)):
                                if(line.startswith('import ' + current_known_api_list[i])):
                                    is_other_api=False
                                    need_add_api=True
                                    for j in range(0,len(appeared_api_list)):
                                        if(line==appeared_api_list[j]):
                                            need_add_api=False
                                    if(need_add_api):
                                        appeared_api_list.append(line)
                                        appeared_api_cnt[i] += 1
                                        appeared_all_cnt += 1
                                # api_not_included.append()
                            if(is_other_api):
                                need_add_other_api=True
                                for k in range(0,len(api_not_included)):
                                    if(line==api_not_included[k]):
                                        need_add_other_api=False
                                if(need_add_other_api):
                                    api_not_included.append(line)
                                    print(line)
                    file_obj.close()        
                except UnicodeDecodeError:
                    print('UnicodeDecodeError error')
                    continue


print("*************************************************************************")
print('总共已知的Android API数量（请注意以上为统计在内的import）: ', appeared_all_cnt)
print("END END END END END END END END END END END END END END END END END END END END")
