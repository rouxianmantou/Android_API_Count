#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import re

tar_path = sys.argv[1]
print(tar_path)

# 读取文件加载排除的API
cur_excluded_api_list = []
with open('excluded_api_list', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        cur_excluded_api_list.append(line.strip("\n"))
    f.close()
print("目前需要排除的Android API数量为（黑名单模式排除）：", len(cur_excluded_api_list))
print("可以自行修改和添加excluded_api_list中的内容。")
print("统计路径为：" + tar_path + "下的内容")
print("*************************************************************************")
print("*************************************************************************")
print("START START START START START START START START START START START START START START START")

# 标记已经出现的API
cur_appeared_api_list = []

# 需要排除的Package Name
cur_package_name_list = []
find_package_name = []

cur_excluded_api_count = 0

java_pattern = re.compile(
    r'^[a-zA-Z_\$\u4e00-\u9fa5][\w_\$\u4e00-\u9fa5]+\.java$')

package_name_pattern = re.compile(r'\"[\w_\$\.]+\"')

for home, dirs, files in os.walk(tar_path):
    for filename in files:
        if(filename == "AndroidManifest.xml"):
            manifest_fullname = os.path.join(home, filename)
            with open(manifest_fullname, mode='r', encoding='UTF-8') as manifest_obj:
                try:
                    for line in manifest_obj:
                        if('package="' in line):
                            find_package_name += re.findall(
                                package_name_pattern, line)

                    manifest_obj.close()
                except UnicodeDecodeError:
                    print('UnicodeDecodeError error')
                    continue
    for m in range(0, len(find_package_name)):
        cur_package_name_list.append(find_package_name[m].strip('\"'))
    find_package_name = []

print("当前package name list : ", cur_package_name_list)
print("*************************************************************************")

for home, dirs, files in os.walk(tar_path):
    for filename in files:
        if(re.match(java_pattern, filename) != None):
            fullname = os.path.join(home, filename)
            with open(fullname, mode='r', encoding='UTF-8') as file_obj:
                try:
                    for line in file_obj:
                        # 开始读import
                        if(line.startswith('import')):
                            is_need_show = True
                            for i in range(0, len(cur_excluded_api_list)):
                                if(line.startswith('import ' + cur_excluded_api_list[i]) or line.startswith('import static ' + cur_excluded_api_list[i])):
                                    is_need_show = False
                                    break
                            for k in range(0, len(cur_package_name_list)):
                                if(line.startswith('import ' + cur_package_name_list[k]) or line.startswith('import static ' + cur_package_name_list[k])):
                                    is_need_show = False
                                    break
                            for j in range(0, len(cur_appeared_api_list)):
                                if(line.startswith('import ' + cur_appeared_api_list[j]) or line.startswith('import static ' + cur_appeared_api_list[j])):
                                    is_need_show = False
                                    break
                            if(is_need_show):
                                cur_excluded_api_count += 1
                                print(line, end='')
                    file_obj.close()
                except UnicodeDecodeError:
                    print('UnicodeDecodeError error')
                    continue

print("*************************************************************************")
print("本包引用的3rd-party库的数量为（估计，可能与实际数量有出入）: ", cur_excluded_api_count)
print("END END END END END END END END END END END END END END END END END END END END")
