@echo off

set toolPath="./ConfigGen/AutoGen/excel2LuaGen.py"
set excelPath="�������ñ�.xlsx"
set exportPath="./ConfigGen/LuaGen"

python %toolPath% %excelPath% %exportPath%

pause