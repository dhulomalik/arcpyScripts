import pyodbc,xlrd
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\DataFinalUpdation.xlsx")
sh=wb.sheet_by_name("update-26-8-15")
#sh=wb.sheet_by_name("updation")
n=0
for i in range(246):
    ac=str(int(sh.cell_value(i+1,0)))
    name=sh.cell_value(i+1,1)
    addr=sh.cell_value(i+1,2)
    mno=sh.cell_value(i+1,5)
    gisid=cur.execute("select GISID from CUSTOMERINFO where ACCOUNTNUMBER=?",ac).fetchone()
    if str(gisid)!='None':n=n+1
    
