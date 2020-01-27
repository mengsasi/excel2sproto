local sproto = require "sproto/sproto"
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

local sprotoPath = "E:/Project/excel2sproto/Game/Assets/Res/Sproto/TestConfig.sproto"
local jsonPath = "E:/Project/excel2sproto/Doc/ConfigGen/Json/TestConfigs.json"
local bytesPath = "E:/Project/excel2sproto/Game/Assets/Res/Configs/TestConfigs.bytes"

GenBytes(sprotoPath, jsonPath, bytesPath)

return Gen