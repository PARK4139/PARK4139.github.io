chcp 65001
color 0a
REM @echo off
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyymmddhhmmss=%%i


git add *

git commit -m "%yyyymmddhhmmss%"