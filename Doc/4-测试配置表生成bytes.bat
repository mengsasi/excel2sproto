@echo off

set toolPath="./ConfigGen/AutoGen/excel2Bytes.py"
set excelPath="�������ñ�.xlsx"
set exportPath="./ConfigGen/Bytes"

python %toolPath% %excelPath% %exportPath%

pause