@echo off

set toolPath="./ConfigGen/AutoGen/excel2sproto.py"
set excelPath="�������ñ�.xlsx"
set exportPath="./ConfigGen/Sproto"

python %toolPath% %excelPath% %exportPath%

pause
