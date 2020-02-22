#这个目录是以bat所在目录为基准的，不是这个py文件为基准
excelPath = "./"

toolRoot = "./ConfigGen/Temp"

jsonPath = toolRoot + "/Json"

#======Doc======#
# sprotoPath = toolRoot + "/Sproto"

# #游戏中读取bytes配置的lua脚本
# luaPath = toolRoot + "/Lua"
# allLuaRequirePath = "Logic/Config/AutoGen"

# 用于生成bytes的lua脚本
luaGenPath = toolRoot + "/LuaGen"
allGenRequirePath = ""

# bytesPath = toolRoot + "/Bytes"

#======Game======#
sprotoPath = "../Game/Assets/Res/Configs/Sproto"

luaPath = "../Game/Assets/Lua/Logic/Config/AutoGen"
allLuaRequirePath = "Logic/Config/AutoGen"

# #Unity引擎中菜单 XLua/GenerateBytes 所用目录
# luaGenPath = "../Game/Assets/Lua/Editor/LuaGen"
# allGenRequirePath = "LuaGen/"

bytesPath = "../Game/Assets/Res/Configs/Bytes"


SprotoGenExe = "./ConfigGen/SprotoGen/SprotoGen.exe"
SprotoGenLua3rd = "./ConfigGen/SprotoGen"
SprotoGenLua = toolRoot + "/LuaGen"
