
import pyodbc,xlrd,arcpy,os
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\Final.xlsx")
shDel=wb.sheet_by_name("del1")
objectIDs=[]
mxd = arcpy.mapping.MapDocument("CURRENT")

sp=arcpy.mapping.ListLayers(mxd,"Service Point")[0]
lt=arcpy.mapping.ListLayers(mxd,"LT Overhead Line")[0]
descsp = arcpy.Describe(sp)
spshapefieldname = descsp.ShapeFieldName

arcpy.Frequency_analysis(r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb\CUSTOMERINFO",\
                             r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb\CUSTOMERINFO_Frequency",\
                             "SERVICEPOINTGISID")
noIter=shDel.nrows
for i in range(noIter-1):
    print "this is %d iteration" %i
    
    obgid=str(int(shDel.cell_value(i+1,0)))

    # if len(ac)==9:ac='0'+ac
    # if len(ac)==8:ac='00'+ac
    
   
    gisid=cur.execute("select GISID,SERVICEPOINTGISID from CUSTOMERINFO where OBJECTID=?",obgid).fetchone()
    obj=cur.execute("select OBJECTID from CONSUMERMETER where RELGISID=?",gisid[0]).fetchone()
    #GIS=gisid[1]
    #arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION",
    #                                       "[GISID]='%s'" % GIS)
    #rows = arcpy.UpdateCursor(sp)
    #for row in rows:
        #print row.getValue("TOWNCODE")
        #rows.deleteRow(row)
    #del rows
    
    customerFreq = arcpy.SearchCursor(r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb\CUSTOMERINFO_Frequency")
    freq=0
    for cust in customerFreq:
        if cust.getValue("SERVICEPOINTGISID")==gisid[1]:freq=cust.getValue("FREQUENCY")
    print freq
    if freq==1:
        files=os.listdir(r"C:\Users\ajay\Documents\ArcGIS")
        for f in files:
            if 'spSelect' in f:os.remove(r"C:\Users\ajay\Documents\ArcGIS\%s" %f)
        
        arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION","[GISID]='%s'" % gisid[1])
        spSelect=arcpy.CopyFeatures_management(sp, r"C:\Users\ajay\Documents\ArcGIS\spSelect.shp")
        
        arcpy.SelectLayerByLocation_management(lt,"WITHIN_A_DISTANCE", spSelect,0.1)
        c=arcpy.GetCount_management(lt)
        count = int(c.getOutput(0))
        print "no of lt selected",count

        if count==1:
            rows = arcpy.UpdateCursor(sp)
            for row in rows:
                print row.getValue("TOWNCODE")
                rows.deleteRow(row)
            del row
            del rows
        #arcpy.DeleteFeatures_management(r"C:\Users\ajay\Documents\ArcGIS\spSelect.shp")
        #arcpy.DeleteFeatures_management(lt)
        
            rows1 = arcpy.UpdateCursor(lt)
            for ro in rows1:
                print ro.getValue("TOWNCODE")
                rows1.deleteRow(ro)
            del ro
            del rows1
        

    cur.execute("delete from CONSUMERMETER where OBJECTID=?",obj[0])
    cur.execute("delete from CUSTOMERINFO  where OBJECTID=?",obgid)
    
    
    print obj[0]


    #cur.execute("delete from CUSTOMERINFO where ACCOUNTNUMBER=?",ac)
    #print ac,i
    #file1.writelines(str(obj)+str(ac))
    # delete the object referring to object it
    #o=cur.fetchone()
    
#conn.commit()
#arcpy.Delete_management(r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb\CUSTOMERINFO_Frequency", '')   

