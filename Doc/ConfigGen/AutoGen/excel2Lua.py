import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import excel2sproto

'''
local JSON = require "cjson"

local function disposeValue(conf)
    conf.tnumber = conf.tnumber / 10
    conf.cost = JSON.decode(conf.cost)
    return conf
end

Configs[v.id] = disposeValue(v)
'''

lua = '''TestConfigs = {}

local Configs = {}
|disposeValue|

function TestConfigs.InitModule()
    local data = ConfigMgr.ParseBytes("TestConfigs")
    for k, v in pairs(data.AllTestConfig) do 
        Configs[v.id] = disposeValueVV
    end
end

function TestConfigs.Get(id)
    return Configs[id]
end

function TestConfigs.GetAll()
    local arr = {}
    for k, v in pairs(Configs) do
        table.insert(arr, v)
    end
    return arr
end

return TestConfigs'''

#TestConfig -> TestConfigs.lua
def genLuaFile(table, exportPath):
    nrows = table.nrows
    ncols = table.ncols
    config = table.cell_value(0, 0)
    configs = config + "s"
    
    luaPath = exportPath + "/" + configs + ".lua"
    dir = os.path.dirname(luaPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(luaPath, "w", "utf-8")
    
    luaFile = lua
    luaFile = luaFile.replace('AllTestConfig', 'All' + config)
    luaFile = luaFile.replace('TestConfigs', configs)

    disposeValueStr = "\nlocal function disposeValue(conf)\n"
    hasJSON = False
    hasDisFunc = False

    #处理浮点，JSON

    #结构体，数组，结构体数组
    sp_struct = excel2sproto.collectStructInfo(table, ncols)
    sp_arr = excel2sproto.collectArrayInfo(table, ncols)
    sp_struct_arr = excel2sproto.collectStructArrayInfo(table, ncols)

    for c in range(0, ncols):
        #第3行是属性 第4行是数据类型
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if propName == "" or propType == "":
            continue #跳过空列
        if propType == "ignore":
            continue
        if propType == "json" or propType == "JSON":
            jsonVal = "\tconf.{0} = JSON.decode(conf.{1})\n".format(propName, propName)
            disposeValueStr = disposeValueStr + jsonVal
            hasJSON = True
            hasDisFunc = True

        if propName.find("-") == -1 and propName.find('.') == -1:
            if "number" in propType:
                rate = propType.replace('number', '')
                numVal = "\tconf.{0} = conf.{1} / {2}\n".format(propName, propName, rate)
                disposeValueStr = disposeValueStr + numVal
                hasDisFunc = True
    
    # sp_struct
    # sp_arr
    # sp_struct_arr
    # 处理结构体，数组，里面的浮点数
    # TODO

    disposeValueStr = disposeValueStr + "\treturn conf\nend"
    if hasDisFunc == True:
        luaFile = luaFile.replace('|disposeValue|', disposeValueStr)
        luaFile = luaFile.replace('disposeValueVV', 'disposeValue(v)')
    else:
        luaFile = luaFile.replace('|disposeValue|', '')
        luaFile = luaFile.replace('disposeValueVV', 'v')

    if hasJSON == True:
        luaFile = "local JSON = require \"cjson\"\n\n" + luaFile

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
