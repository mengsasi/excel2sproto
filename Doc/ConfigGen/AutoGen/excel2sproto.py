import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import sprotoGen
import globalStruct
    
#收集结构体信息
def collectStructInfo(table, ncols):
    dic = {}
    for c in range(0, ncols):
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if "number" in propType:
            propType = "integer"
        #没有- 并且有.
        if propName.find("-") == -1 and propName.find(".") != -1:
            propNames = propName.split(".")
            #item.id item.count
            struct_name = propNames[0]
            struct_item_name = propNames[1]
            structTmp = {}
            structTmp["index"] = 0
            if struct_name in dic:
                structTmp = dic[struct_name]
            ind = structTmp["index"]
            structTmp[ind] = { "name": struct_item_name, "type": propType }
            ind += 1
            structTmp["index"] = ind
            dic[struct_name] = structTmp
    return dic
    
#收集数组信息
def collectArrayInfo(table, ncols):
    arr = {}
    for c in range(0, ncols):
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if "number" in propType:
            propType = "integer"
        if propName.find("-") != -1 and propName.find(".") == -1:
            propNames = propName.split("-")
            arr[propNames[0]] = { 'name': propNames[0], 'type': '*' + propType }
    return arr
    
#收集结构体数组信息
def collectStructArrayInfo(table, ncols):
    structArr = {}
    for c in range(0, ncols):
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if "number" in propType:
            propType = "integer"
        if propName.find("-") != -1 and propName.find(".") != -1:
            #item-0.id item-0.count
            propNames = propName.split("-")
            struct_name = propNames[0]
            parts = propNames[1].split(".")
            struct_item_index = parts[0]
            struct_item_name = parts[1]
            if struct_item_index != '0':
                continue
            structTmp = {}
            structTmp["index"] = 0
            if struct_name in structArr:
                structTmp = structArr[struct_name]
            ind = structTmp["index"]
            structTmp[ind] = { "name": struct_item_name, "type": propType }
            ind += 1
            structTmp["index"] = ind
            structArr[struct_name] = structTmp
    return structArr
    
def table2sproto(table, exportPath):
    nrows = table.nrows
    ncols = table.ncols
    config = table.cell_value(0, 0)
    configs = config + "s"
    
    sprotoPath = exportPath + "/" + config + ".sproto"
    dir = os.path.dirname(sprotoPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(sprotoPath, "w", "utf-8")
    
    sprotoTmp = ""
    sp = sprotoGen.Sproto()
    sp.title = config
    #结构体
    sp_struct = collectStructInfo(table, ncols)
    sp_arr = collectArrayInfo(table, ncols)
    sp_struct_arr = collectStructArrayInfo(table, ncols)
    sp_childs = {}
    for c in range(0, ncols):
        #第3行是属性 第4行是数据类型
        propName = table.cell_value(3, c)
        propType = table.cell_value(4, c)
        if propName == "" or propType == "":
            continue #跳过空列
        if propType == "ignore":
            continue
        if "number" in propType:
            propType = "integer"
        if propName.find("-") != -1 and propName.find('.') != -1:
            #结构体数组
            propNames = propName.split("-")
            prop0 = propNames[0]
            parts = propNames[1].split(".")
            struct_item_index = parts[0]
            if struct_item_index != '0':
                continue
            if prop0 in sp_struct_arr:
                sp_childs[prop0] = { 'name': prop0, 'type': "*" + prop0 }
            continue
        elif propName.find("-") != -1:
            #数组
            propNames = propName.split("-")
            prop0 = propNames[0]
            if prop0 in sp_arr:
                sp_childs[prop0] = sp_arr[prop0]
            continue
        elif propName.find(".") != -1:
            #结构体
            propNames = propName.split(".")
            prop0 = propNames[0]
            if prop0 in sp_struct:
                sp_childs[prop0] = { 'name': prop0, 'type': prop0 }
            continue
        sp_childs[propName] = { 'name': propName, 'type': propType }
    sp_st = {}
    for k, v in sp_struct.items():
        if not globalStruct.check(k):
            sp_st[k] = v
    for k, v in sp_struct_arr.items():
        if not globalStruct.check(k):
            sp_st[k] = v
    sp.structs = sp_st
    sp.childs = sp_childs
    sprotoTmp += sp.parseSproto()
    sprotoTmp += '\n'
    
    sp_all = sprotoGen.Sproto()
    sp_all.title = configs
    allConfig = 'All' + config
    #    AllUIConfig 0 : *UIConfig
    sp_all.childs = {
        allConfig: {
            'name': allConfig,
            'type': '*' + config
        }
    }
    sprotoTmp += sp_all.parseSproto()
    
    file.write(sprotoTmp)
    file.close()
    return
    
def exportAll(excelPath, exportPath):
    excel = xlrd.open_workbook(excelPath)
    allSheetNames = excel.sheet_names()
    for name in allSheetNames:
        exports = name.split("_")
        if len(exports) > 1:
            if str(exports[1]) == "noexport":
                continue
        table = excel.sheet_by_name(name)
        table2sproto(table, exportPath)
        print("generate sproto done " + name)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('excel2sproto argv error')
            os.system("pause")
            
        excelPath = sys.argv[1]
        exportPath = sys.argv[2]
        
        exportAll(excelPath, exportPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
