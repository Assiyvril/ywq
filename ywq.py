import os

def read_input_file(file_name):
    '''打开并读取文件'''

    with open(file_name, 'w') as file:
        lines = file.readlines()
        for line in lines:
            if 'iop' in line:
                print(line, 'IOP 所在位置：', lines.index(line))
                iop_index = lines.index(line)
                # 查找 IOP 字段，返回索引

                lines[iop_index] = 'iop(3/107=0x*1000000,3/108=0x*1000000)'
                file.writelines(lines)
                # 重新赋值
                return file_name+'中 IOP 的值已修改为 iop(3/107=0x*1000000,3/108=0x*000000)'
    return '未找到 IOP 字段，请检查文件内容的格式是否规整或呼叫静宇'

print(read_input_file('./f.gjf'))