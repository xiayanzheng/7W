@echo off
goto menu

:menu
title Network Switcher for 7W.HSG
echo ==================================          
echo 1.Switch to HSG Network - Ethernet
echo 2.Switch to DHCP - Ethernet
echo 3.Switch to DHCP - Wireless
echo 4.Back to 7W-interface
echo ==================================
echo #¡ªPlease make choice by ID¡ª#

set /P var=":"
if %var%==1 goto hsgnetwork
if %var%==2 goto edhcp
if %var%==3 goto wdhcp
if %var%==4 goto end

:hsgnetwork
echo [[[Now Switch to HSG Network - Ethernet]]]]
echo [[[Setting IP]]]
Netsh interface IP Set Addr "HSG-Local" Static 10.97.205.94 255.255.255.192 10.97.205.65
echo [[[Setting DNS]]].
Netsh interface IP Set dns "HSG-Local" static 10.97.205.80 primary
echo [[[Setting Backup DNS]]]
Netsh interface IP add dns "HSG-Local" 10.97.244.10
route delete 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.10.2 metric 1
route delete 10.0.0.0
route delete 170.0.0.0
route delete 158.0.0.0
route delete 133.144.181.0
route delete 133.144.235.0
route delete 133.144.236.0
route delete 202.48.200.169
route add 10.0.0.0 mask 255.0.0.0 10.97.205.65 metric 1 -p
route add 170.0.0.0 mask 255.0.0.0 10.97.205.65 metric 1 -p
route add 158.0.0.0 mask 255.0.0.0 10.97.205.65 metric 1 -p
route add 133.144.181.0 mask 255.255.255.0 10.97.205.65 metric 1 -p
route add 133.144.235.0 mask 255.255.255.0 10.97.205.65 metric 1 -p
route add 133.144.236.0 mask 255.255.255.0 10.97.205.65 metric 1 -p
route add 202.48.200.169 mask 255.255.255.255 10.97.205.65 metric 1 -p
echo [[[Setup Successfully]]]
goto menu

:edhcp
echo [[[Now Switch to DHCP - Ethernet]]]
echo [[[Setting DHCP on Ethernet]]]
netsh interface ip set address name="HSG-Local" source=dhcp
netsh interface ip set dns name="HSG-Local" source=dhcp
echo [[[Setup Successfully]]]
goto menu

:wdhcp
echo [[[Now Switch to DHCP - Wireless]]]]
echo [[[Setting DHCP on Wireless]]]
netsh interface ip set address name="Wireless" source=dhcp
netsh interface ip set dns name="Wireless" source=dhcp
echo [[[Setup Successfully]]]
goto menu

:end
exit
