@echo off
goto menu

:menu
title 7W Backup
echo =====================================          
echo 1. Quick Backup - To Local Disk
echo 2. Full Beckup  - To Removeable Disk
echo 3. Quit
echo =====================================
echo #¡ªPlease make choice by ID¡ª#

set /P var=":"
if %var%==1 goto qbackup
if %var%==2 goto fbackup
if %var%==3 goto 

:qbackup
DEL /f/s/q F:\Downloadcenter\BAKC\7WB\*.*
RD /s/q E:\Downloadcenter\BAKC\7WB
xcopy E:\Resources\Documents\7W E:\Downloadcenter\BAKC\7WB\ /e /y
echo Backup Success.
echo Location E:\Downloadcenter\BAKC\7WB\
pause
goto menu

:fbackup
DEL /f/s/q F:\7WB\*.*
RD /s/q F:\7WB\
xcopy E:\Resources\Documents\7W F:\7WB\ /e /y
echo Backup Success.
echo Location F:\7WB\
pause
goto menu




