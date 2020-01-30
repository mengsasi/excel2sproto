import os
import sys
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import setting
import excel2Json

exportSprotoPath = setting.sprotoPath
exportJsonPath = setting.jsonPath
exportBytesPath = setting.bytesPath

def json2Bytes(table):
    config = table.cell_value(0, 0)
    configs = config + "s"
    
    #lua环境执行，lua脚本
    print("需要借助游戏中的Lua环境，生成bytes " + configs)

def exportAll(excelPath):
    #生成json
    excel2Json.exportAll(excelPath, exportJsonPath)

    excel = xlrd.open_workbook(excelPath)
    allSheetNames = excel.sheet_names()
    for name in allSheetNames:
        exports = name.split("_")
        if len(exports) > 1:
            if str(exports[1]) == "noexport":
                continue
        table = excel.sheet_by_name(name)
        json2Bytes(table)
        # print("generate bytes done " + name)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 1:
            print('excel2Bytes argv error')
            os.system("pause")
            
        excelPath = sys.argv[1]
        
        exportAll(excelPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
