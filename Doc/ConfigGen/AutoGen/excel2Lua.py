import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import excel2sproto

'''示例代码
local JSON = require "cjson"

local function disposeNumArr(arr, rate)
    local newArr = {}
    for k, v in ipairs(arr) do 
        table.insert(newArr, v / rate)
    end
    return newArr
end

local function disposeStructArr_ntest(arr)
    local newArr = {}
    for k, v in ipairs(arr) do 
        v.count = v.count / rate
        table.insert(newArr, v)
    end
    return newArr
end

local function disposeValue(conf)
    conf.tnumber = conf.tnumber / 10
    conf.cost = JSON.decode(conf.cost)
    -- 数组
    conf.numbers = disposeNumArr(conf.numbers, 10)
    -- 结构体
    conf.nitem.count = conf.nitem.count / 100
    -- 结构体数组
    conf.ntest = disposeStructArr_ntest(conf.ntest)
    return conf
end

Configs[v.id] = disposeValue(v)
Configs[v.id] = v
'''

#前后换行
disposeNumArr = '''
local function disposeNumArr(arr, rate)
    local newArr = {}
    for k, v in ipairs(arr) do 
        table.insert(newArr, v / rate)
    end
    return newArr
end
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

    disposeValueStr = ""
    hasJSON = False
    hasDisFunc = False
    hasDisposeNumArr = False
    hasStructArr = False

    #处理浮点，JSON
    sp_struct_arr = excel2sproto.collectStructArrayInfo(table, ncols)
    numStrcutArrDic = {}
    for c in range(0, ncols):
        #第3行是属性 第4行是数据类型
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if propName == "" or propType == "":
            continue #跳过空列
        if propType == "ignore":
            continue
        #JSON
        if propType == "json" or propType == "JSON":
            # conf.cost = JSON.decode(conf.cost)
            jsonVal = "\tconf.{0} = JSON.decode(conf.{1})\n".format(propName, propName)
            disposeValueStr = disposeValueStr + jsonVal
            hasJSON = True
            hasDisFunc = True
        #number
        # 处理结构体，数组，里面的浮点数
        if "number" in propType:
            rate = propType.replace('number', '')
            #number数组
            if propName.find("-") != -1 and propName.find('.') != -1:
                #结构体数组
                propNames = propName.split("-")
                prop0 = propNames[0]
                parts = propNames[1].split(".")
                part1 = parts[1]
                # ntest-0.count
                struct_item_index = parts[0]
                if struct_item_index == '0':
                    if prop0 in sp_struct_arr:
                        if not prop0 in numStrcutArrDic:
                            numStrcutArrDic[prop0] = {}
                        numStrcutArrDic[prop0][part1] = rate
                        hasDisFunc = True
                        hasStructArr = True

            elif propName.find("-") != -1:
                #数组
                propNames = propName.split("-")
                prop0 = propNames[0]
                if propNames[1] == "0":
                    # conf.numbers = disposeNumArr(conf.numbers, 10)
                    numArrVal = "\tconf.{0} = disposeNumArr(conf.{1}, {2})\n".format(prop0, prop0, rate)
                    disposeValueStr = disposeValueStr + numArrVal
                    hasDisFunc = True
                    hasDisposeNumArr = True
            elif propName.find(".") != -1:
                #结构体
                # conf.nitem.count = conf.nitem.count / 100
                numStrcutVal = "\tconf.{0} = conf.{1} / {2}\n".format(propName, propName, rate)
                disposeValueStr = disposeValueStr + numStrcutVal
                hasDisFunc = True
            else:
                # conf.tnumber = conf.tnumber / 10
                numVal = "\tconf.{0} = conf.{1} / {2}\n".format(propName, propName, rate)
                disposeValueStr = disposeValueStr + numVal
                hasDisFunc = True

    if hasStructArr == True:
        numStructArrFunc = ""
        for k, v in numStrcutArrDic.items():
            # conf.ntest = disposeStructArr_ntest(conf.ntest)
            numStructArrVal = "\tconf.{0} = disposeStructArr_{1}(conf.{2})\n".format(k, k, k)
            disposeValueStr = disposeValueStr + numStructArrVal

            funcVal = "\nlocal function disposeStructArr_{}(arr)\n".format(k)
            funcVal = funcVal + "\tlocal newArr = {}\n"
            funcVal = funcVal + "\tfor k, v in ipairs(arr) do\n"
            for kk, vv in v.items():
                funcVal = funcVal + "\t\tv.{} = v.{} / {}\n".format(kk, kk, vv)

            funcVal = funcVal + "\t\ttable.insert(newArr, v)\n"
            funcVal = funcVal + "\tend\n"
            funcVal = funcVal + "\treturn newArr\n"
            funcVal = funcVal + "end\n"
            numStructArrFunc = numStructArrFunc + funcVal

    disposeValueStr = "\nlocal function disposeValue(conf)\n" + disposeValueStr
    disposeValueStr = disposeValueStr + "\treturn conf\nend\n"

    if hasStructArr == True:
        disposeValueStr = numStructArrFunc + disposeValueStr

    if hasDisposeNumArr == True:
        disposeValueStr = disposeNumArr + disposeValueStr

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
