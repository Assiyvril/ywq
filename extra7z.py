import py7zr
import os


ROOT_DIR = 'D:\\wbtest'


def get_7z_file_path(root_dir):
    # 遍历文件夹，返回所有 7z 文件的绝对路径
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.7z'):
                file_list.append(os.path.join(root, file))
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


if __name__ == '__main__':
    file_list = get_7z_file_path(ROOT_DIR)
    extract_7z_file(file_list)
