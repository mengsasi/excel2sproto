package.path = 'ConfigGen/SprotoGen/lua_src/sprotodump/?.lua;' 

require "sprotodump"

local c2s = "../Game/Assets/Res/Configs/Sproto/c2s.sproto"
local c2s_cs = "../Game/Assets/Scripts/Core/Sproto/c2s.cs"

local s2c = "../Game/Assets/Res/Configs/Sproto/s2c.sproto"
local s2c_cs = "../Game/Assets/Scripts/Core/Sproto/s2c.cs"

Dump("-cs", c2s, "-o", c2s_cs, "-p", "C2S", "-namespace")

Dump("-cs", s2c, "-o", s2c_cs, "-p", "S2C", "-namespace")
