import os
import traceback

import setting
import excel2Bytes

def exportAll():
    path = setting.excelPath

    files = os.listdir(path)
    for file in files:
        if os.path.splitext(file)[1] == ".xlsx":
            absPath = path + file
            excel2Bytes.exportAll(absPath)

if __name__ == '__main__':
    try:
        exportAll()
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
