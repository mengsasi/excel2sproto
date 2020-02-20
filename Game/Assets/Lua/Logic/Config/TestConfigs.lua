local JSON = require "cjson"

TestConfigs = {}

local Configs = {}

local function disposeValue(conf)
	conf.tnumber = conf.tnumber / 10
	conf.cost = JSON.decode(conf.cost)
	return conf
end

function TestConfigs.InitModule()
    local data = ConfigMgr.ParseBytes("TestConfigs")
    for k, v in pairs(data.AllTestConfig) do 
        Configs[v.id] = disposeValue(v)
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

return TestConfigs