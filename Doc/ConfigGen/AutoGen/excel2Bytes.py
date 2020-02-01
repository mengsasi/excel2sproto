import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import setting
import excel2Json

def json2Bytes(table):
    config = table.cell_value(0, 0)
    configs = config + "s"
    
    #lua环境执行，lua脚本
    #方法一，在unity中生成bytes
    # print("需要借助游戏中的Lua环境，生成bytes " + configs)
    
    luaFile = config + "Gen"
    #方法二，用py调用sptotogen.exe生成bytes
    cmd = "start {0} \"-3rd\" \"{1}\" \"-p\" \"{2}\" \"-f\" \"{3}\"".format(
        setting.SprotoGenExe, 
        setting.SprotoGenLua3rd,
        setting.SprotoGenLua,
        luaFile)
    os.system(cmd)

def exportAll(excelPath):
    #生成json
    excel2Json.exportAll(excelPath, setting.jsonPath)

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
