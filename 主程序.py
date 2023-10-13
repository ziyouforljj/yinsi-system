#作者 : 自游
#课题 ： 隐私系统

import os
import random


#选择保存路径
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

#定义常用系统专属文件夹
system_name_list = ['Program Files','Program Files (x86)','Temp','Users','SDKTemp','SnapPlugin','Microsoft']
system_name_path_list = []

#创建功能--创建隐藏文件夹
def 隐藏文件夹(path):
    os.mkdir(path)
    os.system('attrib +h ' + path)

#定义陷阱路径
url = '{}'.format(path)


#创建陷阱文件夹
for system_name in system_name_list:
    url = url + r'/Windows'
    if os.path.exists(url):
        print('名为 Windows 的文件夹已存在，请删除文件夹或更换路径！')
        break
    else:
        os.mkdir(url)
        for system_name in system_name_list:
            url0 = url + r'/{}'.format(system_name)
            隐藏文件夹(url0)
            system_name_path_list.append(url0)

print('文件夹生成成功！')

#复制文件
import shutil

def copy_file(source_path, destination_path):
    # 判断源文件是否存在
    if not os.path.exists(source_path):
        print("源文件不存在！")
        return

    # 判断目标路径是否存在，如果不存在则创建
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    try:
        # 使用shutil库的copy2函数进行复制
        shutil.copy2(source_path, destination_path)
        print("文件复制成功！")
    except shutil.Error as e:
        print(f"文件复制失败：{e}")
    except IOError as e:
        print(f"文件读取错误：{e}")

# 调用函数进行复制文件的操作
source_path = '.vhd'

#随机选取一个链接
destination_path = random.choice(system_name_path_list)

copy_file(source_path, destination_path)

print('保存文件路径：{}'.format(destination_path))



