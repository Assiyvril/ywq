import openpyxl


def write_excel(header_list, data_array, file_name, sheet_name, col_count):
    """
    写入excel
    :param header_list: 每一列的表头
    :param data_array: 数据集，多个列表组成的二维数组，每个列表是一列数据
    :param col_count: 列数
    :param file_name: 文件名
    :param sheet_name: sheet名
    :return: excel文件
    """
    col_count = col_count - 1
    wb = openpyxl.Workbook()
    ws = wb.create_sheet(sheet_name, 0)
    ws.append(header_list)

    wb.save(file_name)


def main():
    header = ['键数据_1', 'type_1', '键数据_2', 'type_2', '对应的 Bond Coeffs',
              '结果 Bond Coeffs_id']
    data = [
        ['2', '3'],
        ['b', 'c'],
        ['3', '2'],
        ['c', 'b'],
        ['to_2', 'to_3'],
        ['222', '333'],
    ]
    write_excel(header, data, 'test.xlsx', 'Bonds', 6)

if __name__ == '__main__':
    main()
