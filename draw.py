import matplotlib.pyplot as plt
import os


# Path to the directory to be watched, gaussian software output file
# 高斯软件输出文件，监测变动
GAUSSIAN_OUTPUT_FILE = 'out4.txt'

# Image file name, the image file will be saved in the same directory as
# the output file and show
# 图片文件名，图片文件将保存在与输出文件相同的目录下并显示
IMAGE_FILE_NAME = 'ywq.png'

# The number of lines to begin
# 开始的行数
BEGIN_LINE = 0


def check_file(filename):
    """
    Check if the output file exists
    检查输出文件是否存在
    检查文件内容，有几段数据，默认从最后一段数据开始画图
    以 “ Step Temp Press TotEng Density ” 行作为依据
    """
    print('正在预检测高斯输出文件,请稍等...')
    is_exist = os.path.exists(filename)
    part_list = []
    if is_exist:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if 'Step Temp Press TotEng Density' in lines[i]:
                    part_list.append(i)
    part_count = len(part_list)
    if BEGIN_LINE:
        start_line_num = BEGIN_LINE
    else:
        start_line_num = part_list[-1] + 1
    print('预检测完成，共有{}段数据, 分别位于第 {} 行，（！！！注意：从0开始计数！！！）'.format(part_count, part_list))
    print('默认从第 {} 行开始画图, 当然，也可以自定义开始的行数'.format(start_line_num))

    return start_line_num


def draw():
    """
    Open the output file, read the data, and draw the graph
    打开输出文件，读取数据，画图
    """
    start_line_num = check_file(GAUSSIAN_OUTPUT_FILE)
    print(start_line_num)
    with open(GAUSSIAN_OUTPUT_FILE, 'r') as f:
        print('正在读取数据，请稍等...')
        lines = f.readlines()
        x_list = []
        y_list = []
        for line in lines[start_line_num:]:
            line = line.strip()
            if line == '':
                continue
            try:
                x = int(line.split()[0])
                y = float(line.split()[3])
                x_list.append(x)
                y_list.append(y)
            except Exception as e:
                continue
    print('数据读取完成，正在画图，请稍等...')
    # 画布大小
    plt.figure(figsize=(100, 60), dpi=40)
    ax = plt.gca()
    ax.xaxis.get_offset_text().set_fontsize(50)
    plt.tick_params(labelsize=60, labelcolor='green')
    plt.plot(x_list, y_list)
    plt.xlabel('Step', fontsize=55, fontweight='bold', color='red')
    plt.ylabel('TotEng', fontsize=55, fontweight='bold', color='red')
    plt.title('YWQ', fontsize=88)
    plt.savefig(IMAGE_FILE_NAME)
    print('画图完成，图片文件名为：{}'.format(IMAGE_FILE_NAME))
    plt.show()
    plt.close()
    return True


if __name__ == '__main__':
    draw()
