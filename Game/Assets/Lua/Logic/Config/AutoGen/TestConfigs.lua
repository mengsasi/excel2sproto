local JSON = require "cjson"

TestConfigs = {}

local Configs = {}

local function disposeNumArr(arr, rate)
    local newArr = {}
    for k, v in ipairs(arr) do 
        table.insert(newArr, v / rate)
    end
    return newArr
end

local function disposeStructArr_ntest(arr)
	local newArr = {}
	for k, v in ipairs(arr) do
		v.count = v.count / 1000
		table.insert(newArr, v)
	end
	return newArr
end

local function disposeValue(conf)
	conf.tnumber = conf.tnumber / 10
	conf.numbers = disposeNumArr(conf.numbers, 10)
	conf.nitem.count = conf.nitem.count / 100
	conf.cost = JSON.decode(conf.cost)
	conf.ntest = disposeStructArr_ntest(conf.ntest)
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