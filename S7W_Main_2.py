#!usr/bin/env python
#coding=GBK
import os,time,openpyxl,sqlite3,subprocess,json,urllib.request,urllib.parse,getpass,platform
from forex_python.converter import CurrencyRates
from prettytable import PrettyTable

class jarvis():

    ##Using getpass module
    # def authorization(self):
    #     os.system('cls')
    #     global au_login
    #     au_login = input("Login:")
    #     au_password = getpass.getpass("Password:")
    #     get_up = jarvis.cidb_read(self, sql_data_r='SELECT * FROM userinfo')
    #     for loop_get_up in get_up:
    #         if au_login and au_password in loop_get_up:
    #             jarvis.interface(self)
    #         else:
    #             print("Wrong Username or Password,Pls Try again after 3 seconds.")
    #             time.sleep(3)
    #             jarvis.authorization(self)
    #
    ##Using input module
    # def authorization(self):
    #     os.system('cls')
    #     global au_login
    #     au_login = input("Login:")
    #     au_password = input("Password:")
    #     get_up = jarvis.cidb_read(self, sql_data_r='SELECT * FROM userinfo')
    #     for loop_get_up in get_up:
    #         if au_login and au_password in loop_get_up:
    #             jarvis.interface(self)
    #         else:
    #             print("Wrong Username or Password,Pls Try again after 3 seconds.")
    #             time.sleep(3)
    #             jarvis.authorization(self)

    def interface(self):
            global au_login,current_date,os_version
            os_version = platform.system()
            current_date = (time.strftime("%Y-%m-%d"))
            au_login = ("yzxia")
            os.system('cls')
            print('''
    MMMMMMMMMM  MM       MMMM       MM
    MMMMMMMMMM  MM       MMMM       MM
            MM  MM       MMMM       MM
           WM   MM       MMMM       MM
          WM    MM       MMMM       MM
         MM      MM     MM  MM     MM
        MM        MM   MM    MM   MM
       MM           MVM        MVM
      MM             M          M
      MM             W          W  ''')
            function_list = PrettyTable(["Please make choice by ID"])
            function_list.padding_width = 1
            function_list.align["Please make choice by ID"] = "l"
            function_list.add_row(["Press <1> to contact NetworkEngineer"])
            function_list.add_row(["Press <2> to contact WarrantyManager"])
            function_list.add_row(["Press <3> to contact ProjectManager"])
            function_list.add_row(["Press <4> to contact AssistantPress"])
            function_list.add_row(["Press <5> to contact FinancialManager"])
            function_list.add_row(["Press <0> to Quit"])
            print(function_list)
            jarvis.today(self)
            print("Jarvis:Hello Sir,What can i do for u")
            choice_by_id = input(("%s:"%au_login))
            if choice_by_id == "1":
                network_engineer.interface(self)
            elif choice_by_id == "2":
                warranty_manager.interface(self)
            elif choice_by_id == "3":
                project_manager.interface(self)
            elif choice_by_id == "4":
                assistant.interface(self)
            elif choice_by_id == "5":
                financial_manager.interface(self)
            elif choice_by_id == "0":
                print("ByeBye")
                exit()
            else:
                self.interface(username=None)

    def today(self):
        if current_date == jarvis.get_last_column_in_cidb(self,jarvis.cidb_read(self,sql_data_r="SELECT update_time FROM system_info")):
            pass
        else:
            try:
                financial_manager.jpy_to_cny_foreign_exchange(self)
                financial_manager.get_exchange_rate(self,rate_from="CNY",rate_to="JPY",rate_cu=1)
                db_sql = ("INSERT INTO system_info VALUES(?,?,?)")
                db_data = (os_version,current_date,au_login)
                jarvis.cidb_write(self,db_sql,db_data)
                print("++++++++Today's CNY to JPY Exchange Rate is",jarvis.get_last_column_in_cidb
                (self,jarvis.cidb_read(self,sql_data_r="SELECT rate FROM cny_to_jpy_rate")),"++++++++")
            except:
                print("Jarvis:Data Source Unaccessable,Pls NumCheck NetorkSetting or Contact Administrator")
                pass

    def cidb_read(self, sql_data_r):
        get_old_path = os.getcwd()
        connect_db = sqlite3.connect("%s\cimt.db"%get_old_path)
        # connect_db = sqlite3.connect('/Users/xiayanzheng/Onedriver/OneDrive/Lib-Sandbox/cimt.db')
        cursor_db = connect_db.cursor()
        sql = cursor_db.execute(sql_data_r)
        fetchall_sql = sql.fetchall()
        return fetchall_sql

    def cidb_write(self,db_sql,db_data):
        get_old_path = os.getcwd()
        connect_db = sqlite3.connect("%s\cimt.db"%get_old_path)
        # connect_db = sqlite3.connect('/Users/xiayanzheng/Onedriver/OneDrive/Lib-Sandbox/cimt.db')
        c = connect_db.cursor()
        #Create table
        # c.execute('''Create TABLE if not exists sql_target_table("NA")''')
        #Insert links into table
        c.execute(db_sql,db_data)
        connect_db.commit()

    def show_company_list(self):
        os.system('cls')
        cidball = jarvis.cidb_read(self, sql_data_r='SELECT * FROM company_name')
        company_list = PrettyTable(["ID","Code","CompanyName","Address"])
        company_list.align["CompanyName"] = "l"
        company_list.align["Address"] = "l"
        company_list.padding_width = 1
        for cidball_data in cidball:
            cidball_fcode = cidball_data[1]
            cidball_pcode = cidball_data[2]
            cidball_cname = cidball_data[3]
            cidball_caddr = cidball_data[4]
            company_list.add_row([cidball_fcode,cidball_pcode,cidball_cname,cidball_caddr])
        print(company_list)

    def execute_bat(self, bat_file_path):
        pwd = os.getcwd()
        sa = bat_file_path
        run_bat_path = ("%s\\%s" % (pwd,sa))
        print(run_bat_path)
        run_bat = subprocess.Popen("cmd.exe /c" + "%s abc" %run_bat_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = run_bat.stdout.readline()
        while(curline != b''):
            print(curline.decode('GBK'))
            curline = run_bat.stdout.readline()
        run_bat.wait()
        print(run_bat.returncode)
        run_bat.terminate()
        jarvis.interface(self)

    def continue_or_not(self,c_class,c_def):
        continue_or_quit = input("Jarvis:Press (y) to Continue or Press (n) to quit:")
        if continue_or_quit == ("y"):
            print("NK")
            gu = "gu"
            gu
        else:
            jarvis.interface(self)

    def get_last_column_in_cidb(self,data):
        list = []
        for traversal in data:
            list.append(traversal)
        result = (list[-1])[0]
        return result

class project_manager():

    def interface(self):
        function_list = PrettyTable(["Project Manager:Hi,What can i do for U?:"])
        function_list.padding_width = 1
        function_list.add_row(["Press <1> to Create a Quotation"])
        function_list.add_row(["Press <0> Back to Main Interface"])
        print(function_list)
        choice_by_id = input(("%s:"%au_login))
        if choice_by_id == "1":
            project_manager.get_base_data(self)
        else:
            jarvis.interface(self)

    def get_base_data(self):
        jarvis.show_company_list(self)
        select_company = input("Project Manager:Please Select a company by ID:")
        select_company_int = int(select_company)
        cidb_data = jarvis.cidb_read(self,sql_data_r="SELECT * FROM company_name WHERE fcode = '%s'" % select_company_int)
        format_cidb_data = cidb_data[0]
        company_data_list = [{'fcode':format_cidb_data[0],'pcode':format_cidb_data[1],'ncode':format_cidb_data[2],'cname':format_cidb_data[3],'caddr':format_cidb_data[4],}]
        company_data = company_data_list[0]
        selected_company = company_data["fcode"]
        selected_company_full = company_data["cname"]
        selected_company_address = company_data["caddr"]
        project_manager.creat_project(self, selected_company, selected_company_full, selected_company_address)

    def creat_project(self,selected_company, selected_company_full, selected_company_address):
        get_time = (time.strftime("%y%m%d-%H%M%S"))
        #define project name
        case_name = input("Project Manager:Please input the project name:")
        # common.check_input(self)
        SH_number = input("Project Manager:Please input the project SH Number:")
        case_folder_name = ("EX-%s-%s" % (selected_company, case_name))
        #generate quotation name
        quotation_name = ("%s様向け%s購入費用-Python.7W%s" % (selected_company_full, case_name, get_time))
        costtable_name = ("原価計算書-%s様向け%s購入費用-Python.7W%s" % (selected_company_full, case_name, get_time))
        #the old_project_path = original quotaion file path
        get_old_path = os.getcwd()
        old_quotation_path = ("%s\S7W_Quo_Master.xlsx"% get_old_path)
        old_costtable_path = ("%s\S7W_Costtable_Master.xlsx"% get_old_path)
        #generate new project path
        new_quotation_path = ("E:\Resources\Documents\\Python.7W\%s\%s.xlsx" % (case_folder_name, quotation_name))
        new_costtable_path = ("E:\Resources\Documents\\Python.7W\%s\%s.xlsx" % (case_folder_name, costtable_name))
        try:
            os.mkdir("E:\Resources\Documents\\Python.7W\%s" % case_folder_name)
        except:
            print("Project Manager:Folder is exits,Pls Try Again")
            project_manager.interface(self)
        #start generate quotation
        print("Project Manager:Generating Quotation...")
        os.system("copy %s %s" % (old_quotation_path,new_quotation_path))
        get_quotation_time = (("見積日付：%s年%s月%s日"% (time.strftime("%Y,%m,%d"))))
        quotation = openpyxl.load_workbook(new_quotation_path)
        write_open_quotation_excel = quotation.active
        write_open_quotation_excel["D6"] = selected_company_full
        write_open_quotation_excel["AC2"] = get_quotation_time
        write_open_quotation_excel["J21"] = selected_company_address
        mitsumori_sheet = quotation.get_sheet_by_name('見積明細')
        mitsumori_sheet["C1"] = case_name
        quotation.save(new_quotation_path)
        #start generate costtable
        print("Project Manager:Generating Costtable...")
        os.system("copy %s %s" % (old_costtable_path,new_costtable_path))
        costtable = openpyxl.load_workbook(new_costtable_path)
        write_costtable_excel = costtable.active
        write_costtable_excel["E1"] = SH_number
        write_costtable_excel["G7"] = selected_company_full
        write_costtable_excel["G8"] = selected_company_full
        write_costtable_excel["G9"] = case_name
        costtable.save(new_costtable_path)
        print("Done!")
        #open folder quotation and costtable
        continue_or_not = input("""Project Manager:Continue creat quotation?:(Press "y" to continue else Open folder):""")
        if continue_or_not == ("y"):
            project_manager.get_base_data(self)
        else:
            os.system("explorer.exe E:\Resources\Documents\\Python.7W\\")
            os.system("start %s"%new_quotation_path)
            os.system("start %s"%new_costtable_path)
            print("Project Manager:The folder is opened ,Now We Back to interface:")
            project_manager.interface(self)

class assistant():
    def interface(self):
        function_list = PrettyTable(["Assistant:Hi,What can i do for U?:"])
        function_list.padding_width = 1
        function_list.add_row(["Press <1> to Backup"])
        choice_by_id = input(("%s:"%au_login))
        if choice_by_id == "1":
            jarvis.execute_bat(self,bat_file_path="S7W_Backup.bat")
        else:assistant.interface(self)

class network_engineer():
    def interface(self):
        function_list = PrettyTable(["Warranty Manager:Hi,What can i do for U?:"])
        function_list.padding_width = 1
        function_list.add_row(["Press <1> to Change Network Setting"])
        print(function_list)
        choice_by_id = input(("%s:"%au_login))
        if choice_by_id == "1":
            jarvis.execute_bat(self, bat_file_path="S7W_Network_Switcher_HSG.bat")
        else:network_engineer.interface(self)

class warranty_manager():

    def interface(self):
        os.system('cls')
        function_list = PrettyTable(["Warranty Manager:Hi,What can i do for U?:"])
        function_list.padding_width = 1
        function_list.add_row(["""input "search" to get Warranty status"""])
        function_list.add_row(["""input "reg" to registe Warranty status"""])
        print(function_list)
        choice_by_id = input(("%s:"%au_login))
        if choice_by_id == ("search"):
            warranty_manager.get_warranty(self)
        elif choice_by_id == ("reg"):
            warranty_manager.registe_warranty(self)
        else:
            print("Warranty Manager:Unknow command,Pls Try Again。")
            time.sleep(1)
            warranty_manager.interface(self)

    def get_warranty(self):
        jarvis.show_company_list(self)
        selected_company = input("Please selecet a company:")
        warranty_query = jarvis.cidb_read(self,sql_data_r="SELECT * FROM warranty WHERE user = '%s'" % selected_company)
        company_list = PrettyTable(["Class","Activedate","Expiredate","Product","Supportlevel",
                                    "User","Provider","Certificatetype","Certificate","Usage","Agent"])
        company_list.padding_width = 1
        for list_data in warranty_query:
            warranty_class = list_data[0]
            warranty_activedate = list_data[1]
            warranty_expiredate = list_data[2]
            warranty_product = list_data[3]
            warranty_supportlevel = list_data[4]
            warranty_user = list_data[5]
            warranty_provider = list_data[6]
            warranty_certificatetype = list_data[7]
            warranty_certificate = list_data[8]
            warranty_usage = list_data[9]
            warranty_agent = list_data[10]
            company_list.add_row([warranty_class,warranty_activedate,warranty_expiredate,
                                  warranty_product,warranty_supportlevel,warranty_user,
                                  warranty_provider,warranty_certificatetype,
                                  warranty_certificate,warranty_usage,warranty_agent])
        # for list_data in warranty_query:
        #     for x in range(11):
        #         SP = list_data[x]
        #         print(SP)
        #         # company_list.add_row([SP])
        print(company_list)
        warranty_manager.interface(self)

    def registe_warranty(self):
        warranty_elements_list = (["Class","Activedate","Expiredate","Product","Supportlevel","User","Provider","Certificatetype","Certificate","Usage","Agent"])
        count_warranty_list_elements = int(len(warranty_elements_list))
        # print(convert_cout_warranty_elements_to_int,type(convert_cout_warranty_elements_to_int))
        init_warranty_list = []
        for loop_time in count_warranty_list_elements:
            for loop_warranty_elements_list in warranty_elements_list:
                print(loop_warranty_elements_list)
                input_entry = input(":")
                init_warranty_list.append(input_entry)
                len_init_warranty_list = len(init_warranty_list)
                if len_init_warranty_list == count_warranty_list_elements:
                    try:
                        db_sql = ("INSERT INTO warranty VALUES(?,?,?,?,?,?,?,?,?,?,?)")
                        db_data = (init_warranty_list[0],init_warranty_list[1],
                                init_warranty_list[2],init_warranty_list[3],
                                init_warranty_list[4],init_warranty_list[5],
                                init_warranty_list[6],init_warranty_list[7],
                                init_warranty_list[8],init_warranty_list[9],
                                init_warranty_list[10])
                        jarvis.cidb_write(self,db_sql,db_data)
                        choice_by_id = input(("%s:"%au_login))
                        if choice_by_id == ("y"):
                            warranty_manager.interface(self)
                        else:
                            warranty_manager.registe_warranty(self)
                    except:
                        print("Jarvis:DataBase I/O Error Back to interface.")
                else:
                    print("Data Error,pls retry")
                    warranty_manager.get_warranty(self)

class financial_manager():

    def interface(self):
        function_list = PrettyTable(["Financial Manager:Hi,What can i do for U?:"])
        function_list.padding_width = 1
        function_list.add_row(["Press <1> to get Exchange Rate u want"])
        print(function_list)
        choice_by_id = input(("%s:"%au_login))
        if choice_by_id == ("1"):
            financial_manager.search_show_exchange_rate(self)
        else:
            print("Unknown Command，Pls Try Again")

    def jpy_to_cny_foreign_exchange(self, action="GET"):
        appkey = "5e8f8edcb52e039809c5047cd312dc3d"
        data_source = "http://web.juhe.cn:8080/finance/exchange/rmbquot"
        key = {"key" : appkey,"type" : "1"} #两种格式(0或者1,默认为0)
        key = urllib.parse.urlencode(key)
        if action == "GET":
            openurl = urllib.request.urlopen("%s?%s" % (data_source,key))
        else:
            openurl = urllib.request.urlopen(data_source,key)
        raw_data = openurl.read()
        encoding = openurl.info().get_content_charset('utf8')  # JSON default
        result = json.loads(raw_data.decode(encoding))
        if result:
            error_code = result["error_code"]
            if error_code == 0:
                raw_rate_data = result["result"]
                for find_data in raw_rate_data:
                    pick_data = (find_data.get('日元'))
                    name = (pick_data.get("name"))
                    bankConversionPri = (pick_data.get("bankConversionPri"))
                    time = (pick_data.get("time"))
                    date = (pick_data.get("date"))
                    mBuyPri = (pick_data.get("mBuyPri"))
                    mSellPri = (pick_data.get("mSellPri"))
                    fBuyPri = (pick_data.get("fBuyPri"))
                    fSellPri = (pick_data.get("fSellPri"))
                try:
                    db_sql = ("INSERT INTO exchange_rate VALUES(?,?,?,?,?,?,?,?)")
                    db_data = (name,bankConversionPri,fBuyPri,fSellPri,mBuyPri,mSellPri,time,date)
                    jarvis.cidb_write(self,db_sql,db_data)
                except:
                    print("Jarvis:DataBase I/O Error.")
            else:
                print("%s:%s" % (result["error_code"],result["reason"]))
        else:
            print("request api error")

    def search_show_exchange_rate(self):
        rate_fr = input("Financial Manager “From？”:")
        rate_to = input("Financial Manager “To？”:")
        rate_cu = int(input("Financial Manager “How many？”:"))
        print("Financial Manager:The result is:%s" % financial_manager.get_exchange_rate(self,rate_fr,rate_to,rate_cu))
        jarvis.continue_or_not(self,warranty_manager.get_warranty)

    def get_exchange_rate(self,rate_from,rate_to,rate_cu):
        converter = CurrencyRates()
        result = converter.convert(rate_from,rate_to,rate_cu)
        db_sql = ("INSERT INTO cny_to_jpy_rate VALUES(?,?,?,?)")
        db_data = (rate_from, rate_to, result, current_date)
        jarvis.cidb_write(self,db_sql,db_data)
        return result

if __name__ == '__main__':
    jarvis.interface(self=None)