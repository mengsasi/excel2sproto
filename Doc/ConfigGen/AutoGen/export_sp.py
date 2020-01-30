import os
import traceback

import setting
import excel2sproto
import excel2LuaGen
import excel2Lua
import genAllGen
import genAllLua

def exportAll():
    path = setting.excelPath
    #这个会遍历子文件夹
    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         if os.path.splitext(file)[1] == ".xlsx":
    #             print("excelName is:" + file)

    files = os.listdir(path)
    for file in files:
        if os.path.splitext(file)[1] == ".xlsx":
            absPath = path + file
            # print(absPath)
            excel2sproto.exportAll(absPath, setting.sprotoPath)
            excel2LuaGen.exportAll(absPath, setting.luaGenPath)
            excel2Lua.exportAll(absPath, setting.luaPath)
    
    genAllGen.Gen(setting.luaGenPath, setting.allGenRequirePath)
    genAllLua.Gen(setting.luaPath, setting.allLuaRequirePath)

if __name__ == '__main__':
    try:
        exportAll()
        print("All OK")
    except:
        traceback.print_exc()
        os.system("pause")
