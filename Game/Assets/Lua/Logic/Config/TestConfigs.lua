local sproto = require "sproto/sproto"

local LoadBytes = CS.Core.FileUtils.LoadBytes

local file = LoadBytes(Application.dataPath .. "/Res/Sproto/TestConfig.sproto")

local sp = sproto.parse(file)

local bytes = LoadBytes(Application.dataPath .. "/Res/Configs/TestConfigs.bytes")

local data = sp:decode("TestConfigs", bytes)

GameLog.SkyLog(data)