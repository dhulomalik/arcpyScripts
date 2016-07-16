import pyodbc,xlrd,arcpy
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\Final.xlsx")
shDel=wb.sheet_by_name("del")
objectIDs=[]
mxd = arcpy.mapping.MapDocument(r"I:\DataNScripts\Enterprise\awasvikas\clean.mxd")

sp=arcpy.mapping.ListLayers(mxd,"Service Point")[0]
descsp = arcpy.Describe(sp)
spshapefieldname = descsp.ShapeFieldName
#GIS='40028123452'
#arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION",
#                                           "[GISID]='%s'" % GIS)
'''
rows = arcpy.UpdateCursor(sp)
for row in rows:
    print row.getValue("TOWNCODE")
    rows.deleteRow(row)
del rows
'''
#file1=open(r"c:/Users/ajay/Desktop/obj.txt","w")      
for i in range(111):

    ac=str(int(shDel.cell_value(i+1,0)))
    if len(ac)==9:ac='0'+ac
    if len(ac)==8:ac='00'+ac
    #gisid=cur.execute("select GISID,SERVICEPOINTGISID from CUSTOMERINFO where ACCOUNTNUMBER=?",ac).fetchone()
    #obj=cur.execute("select OBJECTID from CONSUMERMETER where RELGISID=?",gisid[0]).fetchone()
    #GIS=gisid[1]
    #arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION",
    #                                       "[GISID]='%s'" % GIS)
    #rows = arcpy.UpdateCursor(sp)
    #for row in rows:
        #print row.getValue("TOWNCODE")
        #rows.deleteRow(row)
    #del rows
    #cur.execute("delete from CONSUMERMETER where OBJECTID=?",obj[0])
    #print obj
    
    cur.execute("delete from CUSTOMERINFO where ACCOUNTNUMBER=?",ac)
    print ac,i
    #file1.writelines(str(obj)+str(ac))
    # delete the object referring to object it
    #o=cur.fetchone()
    
  
