require "main"

function StartGame()
    Debug.Log("lua game start")
    require "Framework/Common/GameLog"
    
    -- require("LuaGen/AllGen")

    require("Logic/Config/TestConfigs")
end

function StopGame()
    Debug.Log("lua game stop")
end
