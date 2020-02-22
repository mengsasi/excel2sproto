GameInit = {}

local Module = {}

function GameInit.RegisterModule(path)
    Module[#Module + 1] = path
end

function GameInit.Update()
    for k, v in pairs(Module) do 
        local item = require(v)
        item.InitModule()
    end
end

return GameInit