#import pyodbc

def get_engine(kwargs):
    return kwargs

def cursor_example_for_mssqlserver():
    server = 'server_name'
    database = 'redshift'
    username = 'uname'
    #driver='{ODBC Driver 17 for SQL Server}'
    #driver='/usr/lib/libtdsodbc.so'
    driver='FreeTDS'
    cnxn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    #cursor = cnxn.cursor()
    return cnxn
