@echo off

set toolPath="./ConfigGen/AutoGen/excel2Lua.py"
set excelPath="�������ñ�.xlsx"
set exportPath="./ConfigGen/Lua"

python %toolPath% %excelPath% %exportPath%

pause