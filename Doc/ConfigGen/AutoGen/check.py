import os
import sys
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

def check(table):
    nrows = table.nrows
    ncols = table.ncols
    config = table.cell_value(0, 0)
    if config == "":
        return False
    # TODO
    # for c in range(0, ncols):
    #     #第3行是属性 第4行是数据类型
    #     propName = table.cell_value(3, c)
    #     propType = table.cell_value(4, c)
    #     if propName == "" or propType == "":
    #         continue #跳过空列
    #     if propType == "ignore":
    #         continue

def checkAll(excelPath):
    excel = xlrd.open_workbook(excelPath)
    allSheetNames = excel.sheet_names()
    for name in allSheetNames:
        exports = name.split("_")
        if len(exports) > 1:
            if str(exports[1]) == "noexport":
                continue
        table = excel.sheet_by_name(name)
        if not check(table):
            return False
        print("check done " + name)
        
if __name__ == '__main__':
    try:
        checkAll(sys.argv[1])
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
