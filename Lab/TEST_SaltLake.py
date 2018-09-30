#coding=utf-8
# import requests
# r = requests.get("http://112.74.110.121:8080/hsg/")
# sa = r.text
# print(sa)

from selenium import webdriver

chrome_driver_path = "D:\Python35\Lib\site-packages\selenium\webdriver\chrome"
global browser
browser = webdriver.Chrome(chrome_driver_path)
url_int = "https://www.baidu.com/"
browser.get(url_int)
print ("Open baidu")
