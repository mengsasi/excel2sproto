#这个目录是以bat所在目录为基准的，不是这个py文件为基准
excelPath = "./"

toolRoot = "./ConfigGen"

jsonPath = toolRoot + "/Json"

#======Doc======#
# sprotoPath = toolRoot + "/Sproto"

# #游戏中读取bytes配置的lua脚本
# luaPath = toolRoot + "/Lua"
# allLuaRequirePath = "Logic/Config/"

# #用于生成bytes的lua脚本
# luaGenPath = toolRoot + "/LuaGen"
# allGenRequirePath = ""

# bytesPath = toolRoot + "/Bytes"

#======Game======#
sprotoPath = "../Game/Assets/Res/Configs/Sproto"

luaPath = "../Game/Assets/Lua/Logic/Config"
allLuaRequirePath = "Logic/Config/"

luaGenPath = "../Game/Assets/Lua/Editor/LuaGen"
allGenRequirePath = "LuaGen/"

bytesPath = "../Game/Assets/Res/Configs/Bytes"


SprotoGenExe = "./ConfigGen/SprotoGen/SprotoGen.exe"
# SprotoGenExe = "../Tool/SprotoGen/SprotoGen/bin/x64/Debug/SprotoGen.exe"
SprotoGenLua3rd = "./ConfigGen/SprotoGen"
SprotoGenLua = "./ConfigGen/LuaGen"

