
#!/usr/local/python
# coding=UTF-8
import os

# file = open( "test.html", "r" )
# fileadd = open("test.txt","r")
# content = file.read()
# contentadd = fileadd.read()
# file.close()
# fileadd.close()
# pos = content.find( "</table>" )
# if pos != -1:
#         content = content[:pos] + contentadd + content[pos:]
#         file = open( "test.html", "w" )
#         file.write( content )
#         file.close()
#         print ("OK")

def loding():
    for gu in range(100):
        os.system('cls')
        print("Loding.")
        os.system('cls')
        print("Loding..")
        os.system('cls')
        print("Loding...")
        os.system('cls')


def wd_reg():
    get_workdate_year = input("workDate.Year")
    get_workdate_month = input("workDate.Month")
    get_workdate_day = input("workDate.Day")
    date_format_string = ("%2F")
    print("workDate=%s%s%s%s%s%s&"% (get_workdate_year,date_format_string,get_workdate_month,date_format_string,get_workdate_day,date_format_string))
    for one_day in range(1,6):
        get_workType = input("workType:")
        get_time = input("time:")
        get_project = input("projcet:")
        get_customer = input("customer:")
        print("workType%s=%s&time%s=%s&projectNo%s=%s&customer%s=%s" % (one_day,get_workType,one_day,get_time,one_day,get_project,one_day,get_customer))
        print("+++++++++++++++++++++++")
        print("""org.apache.struts.taglib.html.TOKEN=94c056eb1f7d1497a5b2371479251fb7&event=forward_register&delFlag=0&type=8131001000&costNo=&"SSS"userId=xyz&"++++"status=100HTTP/1.1 200 OK""")
        print(one_day)

        all = ("""
POST /hsg/cost/costDSP.do?r=260881190116835816 HTTP/1.1
Host: 112.74.110.121:8080
Connection: keep-alive
Content-Length: 455
Cache-Control: max-age=0
Origin: http://112.74.110.121:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3103.400 QQBrowser/9.6.11372.400
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Referer: http://112.74.110.121:8080/hsg/cost/costDSP.do?r=4865240248922332264
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=D5DA0AAC05FCF7D1E81276FB269B6EC1; JSESSIONID=5FC8179061F26412DD52D7F90E21BEB4

Server: Apache-Coyote/1.1
Content-Type: text/html;charset=UTF-8
Transfer-Encoding: chunked
Date: Thu, 06 Jul 2017 02:20:16 GMT
""")



# wd_reg()
loding()
