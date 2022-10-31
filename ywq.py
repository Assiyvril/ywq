# @author: zjyu
# python 3.8.10
# coding: utf-8
import os
import time
import scipy


def read_input_file(file_name, x_value):
    # 打开并读取输入文件，修改 IOP字段的值

    with open(file_name, 'r+') as file:
        lines = file.readlines()

        for line in lines:
            if 'iop' in line:
                print(line, 'IOP 所在位置：', lines.index(line))
                iop_index = lines.index(line)
                # 查找 IOP 字段，返回索引
                lines[iop_index] = 'iop(3/107=' + x_value + ',3/108=' + x_value + ')'
                # 替换

                file.seek(0, 0)
                # 将指针移到开头

                file.writelines(lines)
                return file_name + '中 IOP 的值已修改为：' + lines[iop_index]

    return '未找到 IOP 字段，请检查文件内容的格式是否规整或呼叫静宇'


def define_x():
    # 定义 X 的值

    input_x = float(input('请输入指定的x值'))
    original_x = input_x * 100000
    str_x = str(int(original_x))
    x_value = '0' + str_x
    return x_value


def find_e(file_name):
    # 从输出文件中提取 e
    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:

def target_func(ez, eo, ho, ef, hf):
    fx = abs(ez-eo+ho) + abs(eo-ef+hf)
    return fx

