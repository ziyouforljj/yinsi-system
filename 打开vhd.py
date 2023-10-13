import os
def new_mkdir(path):
    os.mkdir(path)
    os.system('attrib +h ' + path)

new_mkdir(r"D:\ziyou")
new_mkdir(r"D:\ziyou\game")

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

#随机选取一个路径
destination_path = "D:\ziyou\game"

#保存
copy_file(source_path, destination_path)

#显示路径
print('保存文件路径：{}'.format(destination_path))



'''def vhd(pa):
    txt_text = "select vdisk file=d:\game.vhd\nattach vdisk\nexit".format(pa)
    bat_text = "diskpart /s {}/open-vhd.txt".format(pa)

    # 写入打开磁盘的txt文件
    file_txt = open(pa + r'/open-vhd.txt', 'w')
    file_txt.write(txt_text)
    file_txt.close()

    # 写入打开磁盘的bat文件
    file_bat = open('open-vhd.bat', 'w')
    file_bat.write(bat_text)
    file_bat.close()

vhd(path)'''