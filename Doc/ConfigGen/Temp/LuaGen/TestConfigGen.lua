local sproto = require "sproto/sproto"
local JSON = require "cjson"

local Gen = {}

local function MakeDir(path)
    CS.Core.FileUtils.MakeDir(path)
end

local function Load(path)
    return CS.Core.FileUtils.Load(path)
end

local function SaveBytes(path, bytes)
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
    SaveBytes(bytesPath, data_bytes)
end

local sprotoPath = "E:/excel2sproto/Game/Assets/Res/Configs/Sproto/TestConfigs.sproto"
local jsonPath = "E:/excel2sproto/Doc/ConfigGen/Temp/Json/TestConfigs.json"
local bytesPath = "E:/excel2sproto/Game/Assets/Res/Configs/Bytes/TestConfigs.bytes"

MakeDir(bytesPath)
GenBytes(sprotoPath, jsonPath, bytesPath)

return Gen