import os,time,openpyxl,sqlite3,subprocess,json,urllib.request,urllib.parse,getpass,platform,datetime
from forex_python.converter import CurrencyRates
from prettytable import PrettyTable


def cidb_write(self, db_sql, db_data):
    get_old_path = os.getcwd()
    connect_db = sqlite3.connect("%s\cimt.db" % get_old_path)
    # connect_db = sqlite3.connect('/Users/xiayanzheng/Onedriver/OneDrive/Lib-Sandbox/cimt.db')
    c = connect_db.cursor()
    # Create table
    # c.execute('''Create TABLE if not exists sql_target_table("NA")''')
    # Insert links into table
    c.execute(db_sql, db_data)
    connect_db.commit()

start = input("Press any key to start log:")
if start != None:
    current_date = (time.strftime("%Y-%m-%d"))
    print(current_date)
    start_time= (int(time.strftime('%H%M%S')))
    ent_time = (int(time.strftime('%H%M%S')))
    run_time = ent_time - start_time
    print(start_time,ent_time,run_time)
    user = input("Work For Who:")
    what = input("What:")
    why = input("Why:")
    how = input("How:")
    # cidb_write(self=None, )
