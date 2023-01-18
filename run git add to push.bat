chcp 65001
@echo off
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy MM dd HH mm ss'') do set yyyyMMddHHmmss=%%i
cls


git add *
git commit -m "%yyyyMMddHHmmss%"
git push -u origin main
git status
timeout 5