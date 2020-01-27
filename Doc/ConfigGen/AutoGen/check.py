import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

def check(table):
    print("TODO")

def checkAll(excelPath):
    excel = xlrd.open_workbook(excelPath)
    allSheetNames = excel.sheet_names()
    for name in allSheetNames:
        exports = name.split("_")
        if len(exports) > 1:
            if str(exports[1]) == "noexport":
                continue
        table = excel.sheet_by_name(name)
        check(table)
        print("check done " + name)
        
if __name__ == '__main__':
    try:
        checkAll(sys.argv[1])
        print("OK")
    except:
        traceback.print_exc()
        os.system("pause")
