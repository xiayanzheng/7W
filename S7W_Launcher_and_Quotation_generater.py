#!usr/bin/env python
#coding=GBK
import os,time,openpyxl,sqlite3,subprocess
from prettytable import PrettyTable
# from smb.SMBConnection import *
# from smb.base.SharedFile import *
# from smb.SMBProtocol import *

class common(object):

    def interface(self):
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
            function_list = PrettyTable(["Function ID","Name","Usage"])
            function_list.align["Name"] = "l"
            function_list.align["Usage"] = "l"
            function_list.padding_width = 1
            function_list.add_row(["1","Python.7W-Show-Todo-List","This Function\nWill Show Your Todo List"])
            function_list.add_row(["2","Python.7W-Network-Switcher-HSG","This Function\nWill Setup your\nnetwork environment easily"])
            function_list.add_row(["3","7W_Quotation_generater","Let's\ncreat a Quotation"])
            function_list.add_row(["4","7W_Backup","This Function\nWill Backup Python.7W Folder"])
            function_list.add_row(["5","7W_Warranty","Coming soon"])
            function_list.add_row(["0","exit","Quit the program"])
            print(function_list)
            choice_by_id = input("#>>>Please make choice by ID<<<#")
            if choice_by_id == "1":
                other_funtion.show_todo_List(self)
            elif choice_by_id == "2":
                other_funtion.network_switcher(self)
            elif choice_by_id == "3":
                quatation_generater.select_company_function(self)
            elif choice_by_id == "4":
                other_funtion.backup_7w_folder(self)
            elif choice_by_id == "5":
                info.get_warranty(self)
            if choice_by_id == "0":
                print("ByeBye")
                exit()
            else:
                common.interface(self)

    def cidb(self,sql_request):
        get_old_path = os.getcwd()
        # connect_db = sqlite3.connect("%s\ci.db"%get_old_path)
        connect_db = sqlite3.connect("/Users/xiayanzheng/Documents/github/Sandbox/Python.7W/ci.db")
        cursor_db = connect_db.cursor()
        sql = cursor_db.execute(sql_request)
        fetchall_sql = sql.fetchall()
        return fetchall_sql

    def show_company_list(self):
        # os.system('cls')
        cidball = common.cidb(self,sql_request="SELECT * FROM company_name")
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

    def check_input(self):
        if  self == (""):
            null = ("Null,do y/n")
            if null == ("n"):
                common.check_input(self)
            else:
                pass
        else:
            conform = ("""Please conform(Press n to abord else continue)<<<#""")
            if conform == ("n"):
                common.interface(self)
            else:
                pass

class info(object):

    def get_warranty(self):
        common.show_company_list(self)
        selected_company = input("Please selecet a company:")
        warranty_query = common.cidb(self,sql_request="SELECT * FROM warranty WHERE user = '%s'" %selected_company)
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
            print(company_list)
        continueorquit = input(
"""
Press (y) to Continue
Press (n) to quit
>>>>""")
        if continueorquit == ("y"):info.get_warranty(self)
        else:common.interface(self)
    def registe_warranty(self):
        print("Please tell me follow infomation.")
        in_w_class = input("Class:")
        in_w_activedate = input("Activedate:")
        in_w_expiredate = input("Expiredate:")
        in_w_class = input("Class:")
        in_w_class = input("Class:")



class quatation_generater(object):

    def creat_project(self,selected_company, selected_company_full, selected_company_address):
        get_time = (time.strftime("%y%m%d-%H%M%S"))
        #define project name
        case_name = input("Please input the project name:")
        common.check_input(self)
        SH_number = input("Please input the project of SH Number:")
        case_folder_name = ("EX-%s-%s" % (selected_company, case_name))
        #generate quotation name
        quotation_name = ("%s����%sُ���M��-Python.7W%s" % (selected_company_full, case_name, get_time))
        costtable_name = ("ԭ��Ӌ���-%s����%sُ���M��-Python.7W%s" % (selected_company_full, case_name, get_time))
        #the old_project_path = original quotaion file path
        get_old_path = os.getcwd()
        old_quotation_path = ("%s\S7W_Quo_Master.xlsx"% get_old_path)
        old_costtable_path = ("%s\S7W_Costtable_Master.xlsx"% get_old_path)
        #generate new project path
        new_quotation_path = ("E:\Resources\Documents\\Python.7W\EX-Show-Todo-List\%s\%s.xlsx" % (case_folder_name, quotation_name))
        new_costtable_path = ("E:\Resources\Documents\\Python.7W\EX-Show-Todo-List\%s\%s.xlsx" % (case_folder_name, costtable_name))
        os.mkdir("E:\Resources\Documents\\Python.7W\EX-Show-Todo-List\%s" % case_folder_name)
        #get time
        get_time_year = (time.strftime("%Y"))
        get_time_mouth = (time.strftime("%m"))
        get_time_day = (time.strftime("%d"))
        #start generate quotation
        print("Generating Quotation...")
        os.system("copy %s %s" % (old_quotation_path,new_quotation_path))
        get_quotation_time = (("Ҋ�e�ո���%s��%s��%s��"% (get_time_year,get_time_mouth,get_time_day)))
        quotation = openpyxl.load_workbook(new_quotation_path)
        write_open_quotation_excel = quotation.active
        write_open_quotation_excel["D6"] = selected_company_full
        write_open_quotation_excel["AC2"] = get_quotation_time
        write_open_quotation_excel["J21"] = selected_company_address
        mitsumori_sheet = quotation.get_sheet_by_name('Ҋ�e����')
        mitsumori_sheet["C1"] = case_name
        quotation.save(new_quotation_path)
        #start generate costtable
        print("Generating Costtable...")
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
        continue_or_not = input("""#>>>>Continue creat quotation?:(Press "y" to continue else Open folder)<<<#""")
        if continue_or_not == ("y"):
            quatation_generater.get_base_data(self)
        else:
            os.system("explorer.exe E:\Resources\Documents\\Python.7W\\EX-Show-Todo-List\\")
            os.system("start %s"%new_quotation_path)
            os.system("start %s"%new_costtable_path)
            print("#>>>>The folder is opened ,Now We Back to interface<<<#")
            common.interface(self)

    def get_base_data(self):
        common.show_company_list(self)
        select_company = input("#>>>>Please Select a company by ID<<<#")
        select_company_int = int(select_company)
        cidb_data = common.cidb(self,sql_request="SELECT * FROM company_name WHERE fcode = '%s'" %select_company_int)
        format_cidb_data = cidb_data[0]
        company_data_list = [{'fcode':format_cidb_data[0],'pcode':format_cidb_data[1],'ncode':format_cidb_data[2],'cname':format_cidb_data[3],'caddr':format_cidb_data[4],}]
        company_data = company_data_list[0]
        selected_company = company_data["fcode"]
        selected_company_full = company_data["cname"]
        selected_company_address = company_data["caddr"]
        quatation_generater.creat_project(self,selected_company, selected_company_full, selected_company_address)

class other_funtion():

    def show_todo_List(self):
        os.system('cls')
        pwd = os.getcwd()
        get_show_Todo_List_path = ("%s\\S7W_Show_Todo_List.bat"% pwd)
        sub_show_Todo_List = subprocess.Popen("cmd.exe /c" + "%s abc"%get_show_Todo_List_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = sub_show_Todo_List.stdout.readline()
        while(curline != b''):
            print(curline.decode('GBK'))
            curline = sub_show_Todo_List.stdout.readline()
        sub_show_Todo_List.wait()
        print(sub_show_Todo_List.returncode)
        sub_show_Todo_List.terminate()
        common.interface(self)

    def network_switcher(self):
        os.system('cls')
        pwd = os.getcwd()
        get_network_switcher_HSG_path = ("%s\\S7W_Network_Switcher_HSG.bat"% pwd)
        sub_network_switcher_HSG = subprocess.Popen("cmd.exe /c" + "%s abc"%get_network_switcher_HSG_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = sub_network_switcher_HSG.stdout.readline()
        while(curline != b''):
            print(curline.decode('GBK'))
            curline = sub_network_switcher_HSG.stdout.readline()
        sub_network_switcher_HSG.wait()
        print(sub_network_switcher_HSG.returncode)
        sub_network_switcher_HSG.terminate()
        common.interface(self)

    def backup_7w_folder(self):
        os.system('cls')
        pwd = os.getcwd()
        get_S7W_Backup = ("%s\\S7W_Backup.bat"% pwd)
        sub_S7W_Backup = subprocess.Popen("cmd.exe /c" + "%s abc"%get_S7W_Backup, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curline = sub_S7W_Backup.stdout.readline()
        while(curline != b''):
            print(curline.decode('GBK'))
            curline = sub_S7W_Backup.stdout.readline()
        sub_S7W_Backup.wait()
        print(sub_S7W_Backup.returncode)
        sub_S7W_Backup.terminate()
        os.system('cls')
        common.interface(self)

    # def docuupdate(self):
    #     #��ʼ��һ��samba���ʶ���
    #     samba = SMBConnection('�û���','����','���ص�NetBios Name','Զ�˵�NetBios Name','Domain(�������Ϊ��)')
    #     #����һ��samba����
    #     samba.connect('IP','timeout(����Ϊ��Ĭ��60)')   #����True/False
    #     #�ӷ�������ȡ�ļ��б�
    #     flist = samba.listPath('����ռ�(��C$��/Share/)','Ҫ��ȡ���ļ�Ŀ¼���ļ���')  #���ص����ļ�������ɵ�Ԫ�飬ע�ⷵ�ؽ��������������ļ������� . �� .. Ҳ�������ȥ��
    #     #�����ļ�������
    #     f = open('�����ļ�','w')  #����Ҫ����������ŵ��Ǹ��ļ��Ŀ���
    #     samba.retrieveFile('����ռ�','�������ļ���ַ',f)  #������ļ�д��f����
    #     f.close()
    #     #�ϴ��ļ���������
    #     f = open('�����ļ�','r')
    #     samba.storeFile('����ռ�','�������ļ���ַ',f)
    #     f.close()
    #     print ()


if __name__ == '__main__':
    common.interface(self=None)