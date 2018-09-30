#!usr/bin/env python
#coding=GBK
import os,time,openpyxl,sqlite3,subprocess,xlsxwriter
from prettytable import PrettyTable
creat_project_time = (time.strftime("%y%m%d-%H%M%S"))
def back_to_interface():
    os.system('cls')
    interface()

def cidb(sql_request):
    get_old_path = os.getcwd()
    connect_db = sqlite3.connect("%s\ci.db"%get_old_path)
    cursor_db = connect_db.cursor()
    sql = cursor_db.execute(sql_request)
    fetchall_sql = sql.fetchall()
    return fetchall_sql

def creat_project(selected_company, selected_company_full, selected_company_address):
    #define project name
    conform_conpany = input("""Selected company is >>>-%s-<<<,
Please conform(Press n to abord else continue)<<<#""" % selected_company)
    if conform_conpany == ("n"):
        select_company_function()
    else:
        pass
    case_name = input("Please input the project name:")
    # SH_number = input("Please input the project of SH Number:")
    # if SH_number == "":
    #     SH_unll_conform = input("SH Number is null,Do U want wirte later?(y/n):")
    #     if SH_unll_conform == "n":
    #         SH_number
    case_folder_name = ("EX-%s-%s" % (selected_company, case_name))
    #generate quotation name
    quotation_name = ("%s様向け%s購入費用-Python.7W%s" % (selected_company_full, case_name, creat_project_time))
    costtable_name = ("原価計算書-%s様向け%s購入費用-Python.7W%s" % (selected_company_full, case_name, creat_project_time))
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
    get_quotation_time = (("見積日付：%s年%s月%s日"% (get_time_year,get_time_mouth,get_time_day)))
    quotation = openpyxl.load_workbook(new_quotation_path)
    write_open_quotation_excel = quotation.active
    write_open_quotation_excel["D6"] = selected_company_full
    write_open_quotation_excel["AC2"] = get_quotation_time
    write_open_quotation_excel["J21"] = selected_company_address
    mitsumori_sheet = quotation.get_sheet_by_name('見積明細')
    mitsumori_sheet["C1"] = case_name
    quotation.save(new_quotation_path)
    #start generate costtable
    print("Generating Costtable...")
    os.system("copy %s %s" % (old_costtable_path,new_costtable_path))
    costtable = openpyxl.load_workbook(new_costtable_path)
    write_costtable_excel = costtable.active
    #write_costtable_excel["E1"] = SH_number
    write_costtable_excel["G7"] = selected_company_full
    write_costtable_excel["G8"] = selected_company_full
    write_costtable_excel["G9"] = case_name
    costtable.save(new_costtable_path)
    print("Done!")
    #open folder quotation and costtable
    continue_or_not = input("""#>>>>Continue creat quotation?:(Press "y" to continue else Open folder)<<<#""")
    if continue_or_not == ("y"):
        select_company_function()
    else:
        os.system("explorer.exe E:\Resources\Documents\\Python.7W\\EX-Show-Todo-List\\")
        os.system("start %s"%new_quotation_path)
        os.system("start %s"%new_costtable_path)
        print("#>>>>The folder is opened ,Now We Back to interface<<<#")
        back_to_interface()

# def add_new_company():
#     fcode = input("""What is the company code in your db?(1-100)>>>""")
#     safon = input("""set the pcode same as fcode?(y/n)>>>""")
#     if safon == ("n"):
#         pcodi = input("""What is the company code in your mindmap?(Python.7W?(1-100))>>>""")
#         pcode = ("Python.7W%s"%(pcodi))
#     else:
#         pcode = ("Python.7W%s"%(fcode))
#     ncode = input("""What is the company code?(SDSH)>>>""")
#     cname = input("""What is the company fullname?(昭和電工新材料珠海)>>>""")
#     caddr = input("""What is the company address?(旺旺大厦)>>>""")
#     con = sqlite3.connect("E:\Resources\Documents\Github\Sandbox\Python.7W\ci.db")
#     cur = con.cursor()
#     cur.execute("create table if not exists cidb (fcode,pcode,ncode,cname,caddr)")
#     cur.execute("insert into cidb values (?,?,?,?,?)",(fcode,pcode,ncode,cname,caddr))
#     cur.rowcount
#     cur.close()
#     con.commit()
#     con.close()

def select_company_function():
    os.system('cls')
    cidball = cidb(sql_request='SELECT * FROM cidb')
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
    select_company = input("#>>>>Please Select a company by ID<<<#")
    select_company_int = int(select_company)
    # get_old_path = os.getcwd()
    # con = sqlite3.connect("%s\ci.db"%get_old_path)
    # cur = con.cursor()
    # invald_inpu_cidb_all_search_get_data = cur.execute("SELECT fcode FROM cidb")
    # invald_inpu_cidb_all_search = invald_inpu_cidb_all_search_get_data.fetchall()
    # for hhhhh in invald_inpu_cidb_all_search:
    #     print([hhhhh])
    # print(invald_inpu_cidb_all_search[0])
    # print(type(invald_inpu_cidb_all_search[0]))
    # if select_company not in invald_inpu_cidb_all_search:
    #     print("saa")
    #     select_company_function()
    # else:
    #     pass
    cidb_data = cidb(sql_request="SELECT * FROM cidb WHERE fcode = '%s'" %select_company_int)
    format_cidb_data = cidb_data[0]
    company_data_list = [{'fcode':format_cidb_data[0],'pcode':format_cidb_data[1],'ncode':format_cidb_data[2],'cname':format_cidb_data[3],'caddr':format_cidb_data[4],}]
    company_data = company_data_list[0]
    selected_company = company_data["fcode"]
    selected_company_full = company_data["cname"]
    selected_company_address = company_data["caddr"]
    creat_project(selected_company, selected_company_full, selected_company_address)

def show_todo_List():
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
    back_to_interface()

def network_switcher():
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
    back_to_interface()

def backup_7w_folder():
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
    back_to_interface()

def interface():
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
    function_list.add_row(["0","exit","Quit the program"])
    print(function_list)
    choice_by_id = input("#>>>Please make choice by ID<<<#")
    if choice_by_id == "1":
        show_todo_List()
    elif choice_by_id == "2":
        network_switcher()
    elif choice_by_id == "3":
        select_company_function()
    elif choice_by_id == "4":
        backup_7w_folder()
    elif choice_by_id == "0":
        print("ByeBye")
        time.sleep(1)
        exit()
    else:
        back_to_interface()
os.system('cls')
interface()
