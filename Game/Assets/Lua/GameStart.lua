require "main"

function StartGame()
    Debug.Log("lua game start")
    require "Framework/Common/GameLog"

    require("Logic/GameInit")

    -- 测试读取
    require("Logic/Config/ConfigMgr").Init(GameInit.RegisterModule)
    GameInit.Update()

    local all = TestConfigs.GetAll()
    GameLog.SkyLog(all)
    
end

function StopGame()
    Debug.Log("lua game stop")
end
