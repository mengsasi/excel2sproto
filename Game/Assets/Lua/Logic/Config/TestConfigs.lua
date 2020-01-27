local sproto = require "sproto/sproto"

local sp = sproto.parse [[
    .TestConfig {
        .item {
            id 0 : string
            count 1 : integer
        }
        .nitem {
            id 0 : string
            count 1 : integer
        }
        .test {
            id 0 : string
            count 1 : integer
        }
        .ntest {
            id 0 : string
            count 1 : integer
        }
        id 0 : integer
        skills 1 : *string
        item 2 : item
        test 3 : *test
        tnumber 4 : integer
        numbers 5 : *integer
        nitem 6 : nitem
        ntest 7 : *ntest
    }
    
    .TestConfigs {
        AllTestConfig 0 : *TestConfig
    }
    ]]

local bytes = CS.Core.FileUtils.LoadBytes(Application.dataPath .. "/Res/Configs/TestConfigs.bytes")

local data = sp:decode("TestConfigs", bytes)

GameLog.SkyLog(data)