cls
REM @echo off
color 0a
chcp 65001 
setlocal
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy-MM-dd-HH-mm-ss'') do set yyyy-MM-dd-HH-mm-ss=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy-MM-dd'') do set yyyy_MM_dd=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'yyyy'') do set yyyy=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'MM'') do set MM=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'dd'') do set dd=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'HH'') do set HH=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'mm'') do set mm=%%i
for /f "delims=" %%i in ('Powershell.exe get-date -Format 'ss'') do set ss=%%i


  

set this_nx=All_For_One.xlsx 
set this_n=All_For_One
set this_x=.xlsx
bandizip c "%this_n% %yyyy-MM-dd-HH-mm-ss%.zip" "%this_nx%"

