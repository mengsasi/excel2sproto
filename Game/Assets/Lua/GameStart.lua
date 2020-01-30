require "main"

function StartGame()
    Debug.Log("lua game start")
    require "Framework/Common/GameLog"

    -- 测试读取
    require("Logic/Config/ConfigMgr").Init()

    local all = TestConfigs.GetAll()
    GameLog.SkyLog(all)
    
end

function StopGame()
    Debug.Log("lua game stop")
end
