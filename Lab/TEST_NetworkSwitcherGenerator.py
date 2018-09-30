import os
get_old_path = os.getcwd()


class NSG(object):
    def comand_lib(self):
        batinterface = ("""
        @echo off
        echo =================================================
        echo +  User:Xuyun                                   +
        echo +  Proxy Settings                               +
        echo +  Network Settings                             +
        echo =================================================
        echo =  Enable SSC Proxy(SSC)---------------Press 1  =
        echo =  Disable SSC Proxy(Home or Holtel)---Press 2  =
        echo =  Switch to DHCP-------(Ethernet)-----Press 3  =
        echo =  Switch to SSC Network(Ethernet)-----Press 4  =
        echo =================================================
        SET /P variable=""")

        enable_proxy = ("""
        :label1
        reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t  REG_DWORD /d 1 /f
        reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t  REG_SZ /d 192.168.201.1:8080 /f
        reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride /t  REG_SZ /d "192.168.*;<local>" /f
        goto end
        """)
def interface():
    inputes = input("""
1------Add a interface Module
2------Add a Proxy Module
>>>
    """)
