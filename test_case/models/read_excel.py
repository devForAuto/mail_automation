# -*- coding: utf-8 -*-
"""

@file: read_excel.py

@time: 2017/9/20 16:17

@desc:

"""
import xlrd


def read_xlsx():
    file = 'F:\mail_automation\data\maildata.xlsx'
    data = xlrd.open_workbook(file)
    print(data.sheet_names())
    j = 0
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    rowNum = nrows - 1
    for i in range(rowNum):
        j += 1
        values = table.row_values(j)
        print(values)
        return values
read_xlsx()

