import arcpy,string,datetime,xlrd,pyodbc
d=datetime.date.today()
ds=d.strftime("%y/%m/%d")

wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\Final.xlsx")
sh=wb.sheet_by_name("creation")

odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur1=conn.cursor()
mxd = arcpy.mapping.MapDocument(r"I:\DataNScripts\Enterprise\awasvikas\clean.mxd")

sp=arcpy.mapping.ListLayers(mxd,"Service Point")[0]
descsp = arcpy.Describe(sp)
spshapefieldname = descsp.ShapeFieldName
ss=arcpy.mapping.ListLayers(mxd,"Support Structure")[0]
descss = arcpy.Describe(ss)
ssshapefieldname = descss.ShapeFieldName
dt=arcpy.mapping.ListLayers(mxd,"Distribution Transformer")[0]
descdt = arcpy.Describe(dt)
dtshapefieldname = descdt.ShapeFieldName
bp=arcpy.mapping.ListLayers(mxd,"BuildingPoints")[0]
descbp = arcpy.Describe(bp)
bpshapefieldname = descbp.ShapeFieldName
lt=arcpy.mapping.ListLayers(mxd,"LT Overhead Line")[0]
desclt = arcpy.Describe(lt)
ltshapefieldname = desclt.ShapeFieldName

c=arcpy.GetCount_management(lt)
count = int(c.getOutput(0))

def getXYBP(GIS=""):
    
    arcpy.SelectLayerByAttribute_management(bp, "NEW_SELECTION",
                                           "[BUILDINGID]='%s'" % GIS)
    rows = arcpy.SearchCursor(bp)
    for row in rows:
        feat = row.getValue(ssshapefieldname)
        sublocality=row.getValue('SUBLOCALITY')
        #print sublocality
        pnt = feat.getPart()
        return str(pnt.X)+";"+str(pnt.Y)+";"+sublocality


def getXYSS(GIS=''):
    
    arcpy.SelectLayerByAttribute_management(ss, "NEW_SELECTION",
                                           "[GISID]='%s'" % GIS)
    rows = arcpy.SearchCursor(ss)
    print GIS
    for row in rows:
        feat = row.getValue(ssshapefieldname)
        pnt = feat.getPart()
        return pnt
    del rows



def createServicePoint(i=0):
    GISBP="0"+str(int(sh.cell_value(i+1,4)))
    GISDT=str(int(sh.cell_value(i+1,6)))
    
    GISpole=str(int(sh.cell_value(i+1,3)))
    baseSP=4002813000+i
    baseLT=4002808000+i
    baseCust=7607289105+i
    baseMet=401502429255+i

     
    ins = arcpy.InsertCursor(sp)
    pnt = arcpy.Point()
    line=getXYBP(GISBP)
    print line
    pnt.X, pnt.Y,Location = string.split(line,";")
    feat = ins.newRow()
    feat.shape = pnt
    #feat.setValue(fieldName, inRow.getValue(fieldName))
    
    feat.setValue("BUILDINGID", GISBP)
    feat.setValue("LOCATION", GISBP)
    feat.setValue("SUBTYPECD", 1)
    feat.setValue("CREATIONUSER", 'XCON')
    feat.setValue("DATECREATED", ds)
    feat.setValue("PROJECT_AREA", 'VARANASI')
    feat.setValue("PHASEDESIGNATION", 7)
    feat.setValue("ELECTRICTRACEWEIGHT", '2048')
    feat.setValue("RELSUPPORTSTRUCTUREID",GISpole )
    feat.setValue("ADDRESS", sh.cell_value(i+1,2))
    feat.setValue("DTRGISID", GISDT)
    feat.setValue("TEMPPOLECODE","AV1-4")
    feat.setValue("CONSTRUCTIONSTATUS",1)
    feat.setValue("INSTALLATIONDATE",ds)
    feat.setValue("ENABLED",1)
    feat.setValue("OPERATINGVOLTAGE","440")
    feat.setValue("CONFIGURATIONCHANGEDATE",ds)
    GISid=str(baseSP)
    
    print GISid,GISpole
    feat.setValue("GISID", GISid)
    
    arcpy.SelectLayerByAttribute_management(dt, "NEW_SELECTION",
                                           "[GISID]='%s'" % GISDT)
    dtrows=arcpy.SearchCursor(dt)
    for dtrow in dtrows:
        feat.setValue("TOWNCODE", dtrow.getValue("TOWNCODE"))
        feat.setValue("FEEDERID", dtrow.getValue("FEEDERID"))
        feat.setValue("FEEDERNAME", dtrow.getValue("FEEDERNAME"))
        feat.setValue("SUBSTATIONNAME", dtrow.getValue("SUBSTATIONNAME"))
        feat.setValue("DIVISIONNAME", dtrow.getValue("DIVISIONNAME"))
        feat.setValue("PROJECT_AREA", dtrow.getValue("PROJECT_AREA"))
        
    
    ins.insertRow(feat)
    del ins
    pnt2=getXYSS(GISpole)
    print pnt2
    cur = arcpy.InsertCursor(lt)
    array = arcpy.Array([pnt,pnt2])
    print array
    polyline = arcpy.Polyline(array)
    feat1 = cur.newRow()
    feat1.shape = polyline
    feat1.setValue("CREATIONUSER", 'XCON')
    feat1.setValue("DATECREATED", ds)

    GISidlt=str(baseLT)
    
    #print GISidlt
    feat1.setValue("GISID", GISidlt)
    feat1.setValue("DTRGISID", GISDT)
    feat1.setValue("SUBTYPECD", 5)
    feat1.setValue("PHASEDESIGNATION", 7)
    feat1.setValue("NOMINALVOLTAGE","440")
    feat1.setValue("OPERATINGVOLTAGE","440")
    feat1.setValue("NEUTRALMATERIAL","AL")
    feat1.setValue("NEUTRALSIZE","NA")
    feat1.setValue("FEEDERTYPE","THREE PHASE")
    feat1.setValue("FEEDERCATEGORY","URBAN")
    feat1.setValue("ENABLED",1)
    feat1.setValue("TEMPPOLECODE","AV1-4")
    feat1.setValue("NEUTRAL","Y")
    feat1.setValue("NEUTRALCONDUCTORTYPE","NOTAP")
    feat1.setValue("CABLETYPE","PVC")
    feat1.setValue("CONFIGURATIONCHANGEDATE",ds)
    feat1.setValue("CONDUCTORTYPE_Y","PVC")
    feat1.setValue("CONDUCTORTYPE_R","PVC")
    feat1.setValue("CONDUCTORTYPE_B","PVC")
    
    
    arcpy.SelectLayerByAttribute_management(dt, "NEW_SELECTION",
                                           "[GISID]='%s'" % GISDT)
    dtrows1=arcpy.SearchCursor(dt)
    for dtro in dtrows1:
        feat1.setValue("TOWNCODE", dtro.getValue("TOWNCODE"))
        feat1.setValue("FEEDERID", dtro.getValue("FEEDERID"))
        feat1.setValue("FEEDERNAME", dtro.getValue("FEEDERNAME"))
        feat1.setValue("SUBSTATIONNAME", dtro.getValue("SUBSTATIONNAME"))
        feat1.setValue("DIVISIONNAME", dtro.getValue("DIVISIONNAME"))
        feat1.setValue("PROJECT_AREA", dtro.getValue("PROJECT_AREA"))
        feat1.setValue("DTR_TCODE", dtro.getValue("DTR_TCODE"))
        
    line1=str(pnt.X)+';'+str(pnt.Y)+";"+str(pnt2.X)+';'+str(pnt2.Y)
    print line1

    cur.insertRow(feat1)
    del cur
    GIScust='0'+str(baseCust)
    
    GISmet=str(baseMet)
    ac=str(int(sh.cell_value(i+1,0)))
    if len(ac)==9:ac='0'+ac
    if len(ac)==8:ac='00'+ac
    querryInf="insert into CUSTOMERINFO (CREATIONUSER,DATECREATED,ACCOUNTNUMBER,CUST_NAME,\
CUST_ADD_LINE1,POLECODE,BUILDINGID,GISID,DTRGISID) values (?,?,?,?,?,?,?,?,?)"
    
    querryMet="insert into CONSUMERMETER (CREATIONUSER,DATECREATED,GISID,ACCOUNTNUMBER,\
ENERGY_METER_LAB_NO,RELGISID) values (?,?,?,?,?,?)"
    
    cur1.execute(querryInf,"XCON",ds,ac,sh.cell_value(i+1,1),sh.cell_value(i+1,2)\
                ,GISpole,GISBP,GIScust,GISDT)

    cur1.execute(querryMet,"XCON",ds,GISmet,ac,str(sh.cell_value(i+1,5)),GIScust)
    conn.commit()
    print GISid,GISidlt,GIScust,GISmet
                
def run():
    for i in range(111):
        print "This is %d iteration" %i
        createServicePoint(i+167)
        



