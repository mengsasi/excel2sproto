@echo off

set toolPath="./ConfigGen/AutoGen/excel2Json.py"
set excelPath="�������ñ�.xlsx"
set exportPath="./ConfigGen/Json"

python %toolPath% %excelPath% %exportPath%

pause