import xlwt
import xlrd
from xlutils.copy import copy


def creat_excel(file_path):
    """
    创建文件
    :param file_path:
    :return:
    """
    value = [["商品名", "商品地址", "价格", "已拼", "正在拼", "商品评价"], ]
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("拼多多商品数据")  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(file_path)  # 保存工作簿


def write_excel_xls_append(path, value):
    # 获取需要写入数据的行数
    index = len(value)
    # 打开工作簿
    workbook = xlrd.open_workbook(path)
    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()
    # 获取工作簿中所有表格中的的第一个表格
    worksheet = workbook.sheet_by_name(sheets[0])
    # 获取表格中已存在的数据的行数
    rows_old = worksheet.nrows
    # 将xlrd对象拷贝转化为xlwt对象
    new_workbook = copy(workbook)
    # 获取转化后工作簿中的第一个表格
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            # 追加写入数据，注意是从i+rows_old行开始写入
            new_worksheet.write(i + rows_old, j, value[i][j])
            # 保存工作簿
    new_workbook.save(path)
    print("xls格式表格写入数据成功！")
