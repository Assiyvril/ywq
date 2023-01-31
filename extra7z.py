import time

import py7zr
import os
import shutil


ROOT_DIR = r'D:\BaiduNetdiskDownload\wb'
TARGET_DIR = r'E:\wb'


def get_7z_file_path(root_dir):
    # 遍历文件夹，返回所有 7z 文件的绝对路径
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.7z'):
                file_list.append(os.path.join(root, file))
                print('find -', file)
    return file_list


def extract_7z_file(file_list):
    # 解压 7z 文件至新建文件名的文件夹
    for file in file_list:
        with py7zr.SevenZipFile(file, 'r', password='tuhuohuo.pw') as z:
            z.extractall(path=os.path.join(os.path.dirname(file), os.path.splitext(os.path.basename(file))[0]))
            print(f'解压完成 {file}')
        # 解压完成后删除 7z 文件
        os.remove(file)
        print(f'删除完成 {file}')


# 查找所有包含 "BoBo" 的文件夹
def find_bobo_dir(root_dir):
    # 遍历根目录下所有文件夹和子文件夹，返回所有包含 "BoBo" 的文件夹
    dir_list = []
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            if 'BoBo' in dir:
                dir_list.append(os.path.join(root, dir))
                print('find -', dir)
    return dir_list


# 将包含 "BoBo" 的文件夹移动到目标目录, 并统计花费时间
def move_bobo_dir(dir_list, target_dir):
    for dir in dir_list:
        time_start = time.time()
        try:
            shutil.move(dir, target_dir)
            print(f'移动完成 {dir}')
            time_end = time.time()
            print(f'花费时间 {time_end - time_start}')
        except PermissionError:
            print('有文件移动失败， 权限问题', str(dir))
            time_end = time.time()
            print(f'花费时间 {time_end - time_start}')
            continue


# 将 Target 目录下所有文件夹重命名，删掉 ”[BoBoSocks袜啵啵]“ 字符串
# def rename_dir(target_dir):
#     for root, dirs, files in os.walk(target_dir):
#         for dir in dirs:
#             new_dir = dir.replace('[BoBoSocks袜啵啵]', '')
#             os.rename(os.path.join(root, dir), os.path.join(root, new_dir))
#             print(f'重命名完成 {dir} -> {new_dir}')


if __name__ == '__main__':
    dir_list = find_bobo_dir(ROOT_DIR)
    move_bobo_dir(dir_list, TARGET_DIR)
    # rename_dir(TARGET_DIR)
