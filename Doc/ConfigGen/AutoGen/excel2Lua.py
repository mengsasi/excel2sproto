import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

lua = '''local sproto = require "sproto/sproto"

local LoadBytes = CS.Core.FileUtils.LoadBytes

local file = LoadBytes(Application.dataPath .. "/Res/Sproto/TestConfig.sproto")

local sp = sproto.parse(file)

local bytes = LoadBytes(Application.dataPath .. "/Res/Configs/TestConfigs.bytes")

local data = sp:decode("TestConfigs", bytes)

GameLog.SkyLog(data)'''

def genLuaFile(table, exportPath):
    config = table.cell_value(0, 0)
    configs = config + "s"

    luaPath = exportPath + "/" + configs + ".lua"
    dir = os.path.dirname(luaPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(luaPath, "w", "utf-8")
    
    #TODO 自定义读取，这里示例
    luaFile = lua

    file.write(luaFile)
    file.close()

def exportAll(excelPath, exportPath):
    excel = xlrd.open_workbook(excelPath)
    allSheetNames = excel.sheet_names()
    for name in allSheetNames:
        exports = name.split("_")
        if len(exports) > 1:
            if str(exports[1]) == "noexport":
                continue
        table = excel.sheet_by_name(name)
        genLuaFile(table, exportPath)
        print("generate lua done " + name)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('excel2Lua argv error')
            os.system("pause")
            
        excelPath = sys.argv[1]
        exportPath = sys.argv[2]
        
        exportAll(excelPath, exportPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
