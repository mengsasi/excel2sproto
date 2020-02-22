local sproto = require "sproto/sproto"

ConfigMgr = {}

local function Load(type, conf)
    -- 根据类型，拼接路径
    local path = Application.dataPath .. "/Res/Configs"
    if type == "sp" then 
        path = path .. "/Sproto/" .. conf .. ".sproto"
        return CS.Core.FileUtils.Load(path)
    elseif type == "bytes" then
        path = path .. "/Bytes/" .. conf .. ".bytes"
        return CS.Core.FileUtils.LoadBytes(path)
    end
end

function ConfigMgr.ParseBytes(configName)
    local spData = Load("sp", configName)
    local sp = sproto.parse(spData)
    local bytes = Load("bytes", configName)
    return sp:decode(configName, bytes)
end

function ConfigMgr.Init(RegisterModule)
    require("Logic/Config/AutoGen/AllConfigs").Init(RegisterModule)

end

return ConfigMgr