import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import setting

lua = '''local sproto = require "sproto/sproto"
local JSON = require "cjson"

local Gen = {}

local function Load(path)
    return CS.Core.FileUtils.Load(path)
end

local function Save(path, bytes)
    CS.Core.FileUtils.SaveBytes(path, bytes)
end

local function GenBytes(spPath, jsonPath, bytesPath)
    local sp = sproto.parse(Load(spPath))
    local js = Load(jsonPath)
    local data = JSON.decode(js)
    local TestConfigs = {
        AllTestConfig = data
    }
    local data_bytes = sp:encode("TestConfigs", TestConfigs)
    Save(bytesPath, data_bytes)
end

local sprotoPath = \"|sprotoPath|\"
local jsonPath = \"|jsonPath|\"
local bytesPath = \"|bytesPath|\"

GenBytes(sprotoPath, jsonPath, bytesPath)

return Gen'''

#TestConfig Lua -> TestConfigGen.lua
def genLuaFile(table, exportPath):
    config = table.cell_value(0, 0)
    configs = config + "s"

    sprotoPath = setting.sprotoPath + "/" + config + ".sproto"
    jsonPath = setting.jsonPath + "/" + configs + ".json"
    bytesPath = setting.bytesPath + "/" + configs + ".bytes"
    sprotoPath = os.path.abspath(sprotoPath)
    jsonPath = os.path.abspath(jsonPath)
    bytesPath = os.path.abspath(bytesPath)

    sprotoPath = sprotoPath.replace('\\', '/')
    jsonPath = jsonPath.replace('\\', '/')
    bytesPath = bytesPath.replace('\\', '/')

    luaFile = lua
    luaFile = luaFile.replace('AllTestConfig', 'All' + config)
    luaFile = luaFile.replace('TestConfigs', configs)

    luaFile = luaFile.replace('|sprotoPath|', sprotoPath)
    luaFile = luaFile.replace('|jsonPath|', jsonPath)
    luaFile = luaFile.replace('|bytesPath|', bytesPath)
    
    luaPath = exportPath + "/" + config + "Gen.lua"
    dir = os.path.dirname(luaPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(luaPath, "w", "utf-8")
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
        print("generate luagen done " + name)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('excel2LuaGen argv error')
            os.system("pause")
            
        excelPath = sys.argv[1]
        exportPath = sys.argv[2]
        
        exportAll(excelPath, exportPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
