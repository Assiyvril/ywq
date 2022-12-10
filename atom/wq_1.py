"""
初始映射  line 360 start='Atom type, charge, xyz'
        end = 两空行 和 Bonds
        
        
健   line 76 start = 'Bond Coeffs'
    end = 两空行 Angle Coeffs
    
    line 551 start= 'Bonds'
    end = 1 空行 + Angles
    

角   line 128 start= Angle Coeffs
    end= 两空行 + dihedral coeffs

    line 750 start = Angles
    end = 两空行 + Dihedrals
    
二面角     line 216 start= dihedral coeffs
            end = 两空行+ Atom type, charge, xyz

          line 1119 start = Dihedrals
          end = end

"""
import openpyxl

def is_break_time(content_line):
    """
    判断何时break，尝试将第一个字符转为 int
    若不能转换， 则表示应该退出
    """
    try:
        int(content_line[0])
        return False
    except ValueError:
        return True


# 简单起见，多读取几次，省的计算优先级，并且兼容性更好


def write_excel(header_list, data_array, file_name, sheet_name):
    """
    写入excel
    :param header_list: 每一列的表头
    :param data_array: 数据集，多个列表组成的二维数组，每个列表是一列数据
    :return: excel文件
    """
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(sheet_name, 0)
    ws.append(header_list)
    for data_list in data_array:
        ws.append(data_list)
    wb.save(file_name)

def main():
    header = ['键数据_1', 'type_1', '键数据_2', 'type_2', '对应的 Bond Coeffs',
              'Bond Coeffs_id']
    data = [
        ['2', '3'],
        ['b', 'c'],
        ['3', '2'],
        ['c', 'b'],
        ['to_2', 'to_3'],
        ['222', '333'],
    ]
    write_excel(header, data, 'test.xlsx', 'Bonds')



def get_origin_map() -> dict:
    """

    :rtype: dict
    """
    with open('y6.txt', encoding='utf-8', mode='r') as file:
        content_line_list = file.readlines()
        origin_map_id_to_type = {}

        for content_line in content_line_list:
            if 'Atom' in content_line and 'type' in content_line and 'charge' in content_line and 'xyz' in content_line:
                print('Find!!!!!!!!!!')
                index = content_line_list.index(content_line)
                new_list = content_line_list[index + 1:]
                for new_line in new_list:
                    if not new_line:
                        continue
                    if is_break_time(content_line=new_line):
                        break

                    new_one_line_list = new_line.split('	')
                    atom_id = new_one_line_list[0]
                    atom_type = new_one_line_list[2]
                    origin_map_id_to_type[atom_id] = atom_type

                break
    return origin_map_id_to_type


def read_data(start_sign, result_index_list):
    """
    读取数据
    :param start_sign: 数据开始标志
    :param result_index_list: 每一行的结果索引，列表
    :return: 二维数组，每一行是一个列表，列表中是每一列的数据
    """
    """
    ps: 上面白写了，直接用此函数就行了
        思索再三，不忍丢弃
    """
    with open('y6.txt', encoding='utf-8', mode='r') as file:
        content_line_list = file.readlines()
        result_list = []
        for content_line in content_line_list:
            if start_sign in content_line:
                print('Find!!!!!!!!!!')
                index = content_line_list.index(content_line)
                new_list = content_line_list[index + 1:]
                for new_line in new_list:
                    if not new_line:
                        continue
                    if is_break_time(content_line=new_line):
                        break

                    new_one_line_list = new_line.split('	')
                    result_one_line_list = []
                    for result_index in result_index_list:
                        result_one_line_list.append(
                            new_one_line_list[result_index].split('\n')[0])
                    result_list.append(result_one_line_list)
                break
    return result_list


def find_bonds_result():
    origin_bonds_data_arry = read_data(
        start_sign='Bonds', result_index_list=[0, 1]
    )
    origin_bonds_coeffs_arry = read_data(
        start_sign='Bond Coeffs', result_index_list=[0, 4, 5]
    )

    origin_map_id_to_type: dict = get_origin_map()
    
    for origin_bonds_list in origin_bonds_data_arry:
        atom_id_1 = origin_bonds_list[0]
        atom_id_2 = origin_bonds_list[1]
        atom_type_1 = origin_map_id_to_type[atom_id_1]
        atom_type_2 = origin_map_id_to_type[atom_id_2]
        # 在coeffs中找到对应的类型id，由于列表不可哈希, 转换太繁琐，直接遍历
        for origin_bonds_coeffs_list in origin_bonds_coeffs_arry:
    return origin_bonds_data_arry, origin_bonds_coeffs_arry



bonds, bods_coeffs = find_bonds_result()
origin_map_id_to_type = get_origin_map()
print('---origin_map---', origin_map_id_to_type)
print('---Bonds---\n', bonds)
print('---Bonds Coeffs---\n', bods_coeffs)
