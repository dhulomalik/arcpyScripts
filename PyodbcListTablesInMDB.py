import pyodbc,xlrd
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\DataFinalUpdation.xlsx")
sh=wb.sheet_by_name("update-26-8-15")
for row in cur.tables():
    print row.table_name

#cursor.execute("select a from tbl where b=? and c=?", (x, y))
#cursor.execute("select album_id, photo_id from photos where user_id=1")
#row = cursor.fetchone()
#print row.album_id, row.photo_id
#print row[0], row[1] # same as above, but less readable

#rows = cursor.execute("select * from tmp").fetchall()
#cursor.execute("insert into products(id, name) values ('pyodbc', 'awesome library')")
#cnxn.commit()
#cursor.execute("insert into products(id, name) values (?, ?)", 'pyodbc', 'awesome library')
#cnxn.commit()
#cursor.execute("delete from products where id <> ?", 'pyodbc')
#print cursor.rowcount, 'products deleted'
#cnxn.commit()
#deleted = cursor.execute("delete from products where id <> 'pyodbc'").rowcount
#cnxn.commit()
#deleted = cursor.execute("delete from products where id <> 'pyodbc'").rowcount
#cursor.execute("UPDATE progress SET CockpitDrill = ? WHERE progress_primarykey = ?", newcockpitdrillvalue, oldprimarykeyvalue)
mt=cur.execute('select * from Meter').fetchall()
mtF=cur.columns("Meter").fetchall()
columns = [column[0] for column in cur.description]
cur.execute("update CUSTOMERINFO set CREATIONUSER='ajay' where OBJECTID=477433")
cust=cur.execute('select ACCOUNTNUMBER,CUST_NAME,POLECODE from CUSTOMERINFO where OBJECTID=477433').fetchall()

cust=cur.execute("select CUST_NAME,CUST_ADD_LINE1,POLECODE from CUSTOMERINFO where ACCOUNTNUMBER='7830321000'").fetchall()

#['OBJECTID', 'CREATIONUSER', 'DATECREATED', 'LASTUSER', 'DATEMODIFIED', 'ACCOUNTNUMBER',
#'DATASOURCE', 'MONTHCD', 'SERVICEADDRESSOBJECTID', 'HYPERLINK', 'COMMENTS', 'CUST_NAME',
#'CUST_OCC_NAME', 'OWNER', 'CUST_PAN_NO', 'CUST_FATHER_NAME', 'CUST_HUSBAND_NAME',
#'CUST_ADD_LINE1', 'CUST_ADD_LINE2', 'LEFTSIDEHOUSECIN', 'RIGHTSIDEHOUSECIN', 'COLONYNAME',
#'WARDNUMBER', 'BPLNUMBER', 'EMAIL', 'GOVTEMPLOYEE', 'POLENAME', 'ZONEMATCH', 'ZONENAME',
#'KHASARA_METER_NO', 'PHONE_NO_MOBILE', 'PHONE_NO_LL', 'CON_TOT_LOAD', 'ESTIMATED_LOAD',
#'SANCTIONED_LOAD', 'SERVICETYPE', 'BPL', 'DEPTEMPLOYEE', 'KNO', 'HV2NO', 'SCNO', 'BOOKNO',
#'CINNUMBER', 'FIRMNAME', 'AREANAME', 'POLECODE', 'BUILDINGID', 'BUILDINGFLOORNUMBER',
#'SUPPLYVOLTAGE', 'RATEDVOLTAGE', 'POWERFACTOR', 'DOUBLEMETER', 'METERCTRATIO', 'LINECTRATIO',
#'BUSVECTORGROUP', 'CONNECTEDCIRCUIT', 'LTCIRCUITENO', 'SUPPLYPHASE', 'SUPPLYTYPE',
#'ACTUALUSE', 'READINGFOUND', 'SERVICECABLELENGTH', 'CONSUMERSTATUS', 'SUPPLY_RELEASE_DATE',
#'REMARKS', 'METERCOLORCODE', 'CONFIGURATIONCHANGEDATE', 'CCB_NC_INSERTED', 'CON_CORELATION',
#'SERVICECABLESIZE', 'PINNO', 'GISID', 'WEBEDITOR', 'TARRIF_CAT', 'METERROOM_INDEPENDENTENTRY',
#'GROUPCODE', 'DTRGISID', 'TOWNCODE', 'DTRWISEWALKSEQNO', 'DTRWISEPOLENO', 'PHASEDESIGNATION',
#'DIVISIONNAME', 'SERVICEPOINTGISID', 'TEMPPOLECODE', 'SURVEY_BUILDINGID', 'SUBSTATIONNAME',
#'FEEDERNAME', 'DTR_TCODE', 'CI_SURVEY_UNIQUE_ID']

#conn.commit()
#ac=str(sh.cell_value(1,0))[:-2]
count=0
querry="update CUSTOMERINFO set CUST_NAME=?,CUST_ADD_LINE1=? where ACCOUNTNUMBER=?"
for i in range(246):
    ac=sh.cell_value(i+1,0)
    name=sh.cell_value(i+1,1)
    addr=sh.cell_value(i+1,2)
    mno=sh.cell_value(i+1,5)
    gisid=cur.execute("select GISID from CUSTOMERINFO where ACCOUNTNUMBER=?",ac).fetchone()
    #if sh.cell_value(i+1,1)==cust[0]:count=count+1
    #if sh.cell_value(i+1,1)!=cust[0]:print i,sh.cell_value(i+1,1),cust[0]
    cur.execute("update CONSUMERMETER set ENERGY_METER_LAB_NO=?,CREATIONUSER='XCON'  where RELGISID=?",mno,gisid[0])
    #if sh.cell_value(i+1,5)==mtno[0]:count=count+1
    cur.execute("update CUSTOMERINFO set CUST_NAME=?,CUST_ADD_LINE1=?,CREATIONUSER='XCON' where ACCOUNTNUMBER=?",name,addr,ac)
    
