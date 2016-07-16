
import pyodbc,xlrd
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\Final.xlsx")
#sh=wb.sheet_by_name("update-26-8-15")
sh=wb.sheet_by_name("updation")
for i in range(160):
    ac=str(int(sh.cell_value(i+1,0)))
    if len(ac)==9:ac='0'+ac
    if len(ac)==8:ac='00'+ac
    
    name=sh.cell_value(i+1,1)
    addr=sh.cell_value(i+1,2)
    mno=sh.cell_value(i+1,5)
    gisid=cur.execute("select GISID from CUSTOMERINFO where ACCOUNTNUMBER=?",ac).fetchone()
    cur.execute("update CONSUMERMETER set ENERGY_METER_LAB_NO=?,CREATIONUSER='XCON'  where RELGISID=?",mno,gisid[0])
    
    cur.execute("update CUSTOMERINFO set CUST_NAME=?,CUST_ADD_LINE1=?,CREATIONUSER='XCON'\
                where ACCOUNTNUMBER=?",name,addr,ac)
    
#finally register the changes
#conn.commit()
