echo off

set tool=ConfigGen/SprotoGen/SprotoGen.exe
set _3rd="ConfigGen/SprotoGen"
set _p="ConfigGen"

start %tool% "-3rd" %_3rd% "-p" %_p% "-f" "gen_net_cs"
