import os,time,openpyxl,sqlite3,subprocess,json,urllib.request,urllib.parse,getpass

def request3(appkey, m="GET"):
    url = "http://op.juhe.cn/onebox/exchange/currency"
    params = {
        "from" : "日元", #转换汇率前的货币代码
        "to" : "人民币", #转换汇率成的货币代码
        "key" : appkey, #应用APPKEY(应用详细页查询)

    }
    params = urllib.parse.urlencode(params)
    if m =="GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read().decode('utf-8')
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print (res["result"])
        else:
            print ("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print ("request api err")

appkey = "5e8f8edcb52e039809c5047cd312dc3d"
request3(appkey,"GET")