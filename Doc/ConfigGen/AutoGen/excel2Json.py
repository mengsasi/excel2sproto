import os
import sys
import codecs
import xlrd #http://pypi.python.org/pypi/xlrd
import traceback

import json

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(num)
        return True
    except (TypeError, ValueError):
        pass
    return False
    
def disposeValue(val, type):
    #类型问题
    if "number" in type:
        if val == "":
            val = 0
        else:
            ts = type.replace("number", "")
            val = val * int(ts)
        val = int(val)
    elif type == "integer":
        if val == "":
            val = 0
        val = int(val)
    elif type == "string":
        #if is_number(val): #执行慢
        #    val = int(val)
        val = str(val)
        if "." in val: #整数含有.0
            val = val.split(".")[0]
    if type == "bool" or type == "boolean":
        if val == '0':
            val = False
        else:
            val = True
    return val

def isEmptyLine(table, row, ncols):
    linecnt = 0
    for i in range(ncols - 1):
        v = table.cell_value(row, i)
        v = str(v)
        linecnt += len(v)
        if linecnt > 0:
            return False
    if linecnt == 0:
        return True
    else:
        return False
        
def table2Json(table, exportPath):
    nrows = table.nrows
    ncols = table.ncols
    config = table.cell_value(0, 0)
    configs = config + "s"

    jsonPath = exportPath + "/" + configs + ".json"
    dir = os.path.dirname(jsonPath)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    file = codecs.open(jsonPath, "w", "utf-8")
    
    datas = []
    for r in range(7, nrows):
        if isEmptyLine(table, r, ncols): #跳过空行
            continue
        data = {}
        for c in range(ncols):
            propName = table.cell_value(3, c)
            propType = table.cell_value(4, c)
            if propName == "" or propType == "":
                continue #跳过空列
            if propType == "ignore":
                continue
            cellValue = table.cell_value(r, c)
            cellValue = disposeValue(cellValue, propType)
            if propName.find("-") != -1 and propName.find('.') != -1:
                #结构体数组
                propNames = propName.split("-")
                prop0 = propNames[0]
                parts = propNames[1].split(".")
                struct_item_index = int(parts[0]) #int
                struct_item_name = parts[1]
                if not prop0 in data:
                    data[prop0] = []
                arr = data[prop0]
                item = {}
                if len(arr) > struct_item_index:
                    item = arr[struct_item_index]
                else:
                    arr.append(item)
                #if arr[struct_item_index] is None:
                #    item = {}
                item[struct_item_name] = cellValue
                arr[struct_item_index] = item
                continue
            elif propName.find("-") != -1:
                #数组
                propNames = propName.split("-")
                prop0 = propNames[0]
                if not prop0 in data:
                    data[prop0] = []
                data[prop0].append(cellValue)
                continue
            elif propName.find(".") != -1:
                #结构体
                propNames = propName.split(".")
                prop0 = propNames[0]
                struct_item_name = propNames[1]
                s = {}
                if prop0 in data:
                    s = data[prop0]
                s[struct_item_name] = cellValue
                data[prop0] = s
                continue
            data[propName] = cellValue
        datas.append(data)
    jsonStr = json.dumps(datas)
    #print(jsonStr)
    file.write(jsonStr)
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
        table2Json(table, exportPath)
        print("generate json done " + name)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('excel2Json argv error')
            os.system("pause")
            
        excelPath = sys.argv[1]
        exportPath = sys.argv[2]
        
        exportAll(excelPath, exportPath)
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
