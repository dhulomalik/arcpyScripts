import arcpy,string,datetime,xlrd,pyodbc
d=datetime.date.today()
ds=d.strftime("%y/%m/%d")
wb=xlrd.open_workbook(r"I:\DataNScripts\Enterprise\awasvikas\DataFinalUpdation.xlsx")
sh=wb.sheet_by_name("creation")
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' % \
                (r"I:\DataNScripts\Enterprise\awasvikas\fwdawasvikashpgdb\PuVVNL_VARANASI_DIV6_21AUG15.mdb", "admin", "")
conn = pyodbc.connect(odbc_conn_str)
cur=conn.cursor()
mxd = arcpy.mapping.MapDocument(r"I:\DataNScripts\Enterprise\awasvikas\puvvnl.mxd")
#mxd = arcpy.mapping.MapDocument("CURRENT")

'''for i in range(42):
	lyr = arcpy.mapping.ListLayers(mxd)[i]
	print i+1,lyr.name'''


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


def createServicePoint(line=''):
    ins = arcpy.InsertCursor(sp)
    pnt = arcpy.Point()
    line="697224.1453;2806288.2047"
    pnt.X, pnt.Y = string.split(line,";")
    feat = ins.newRow()
    feat.shape = pnt
    #feat.setValue(fieldName, inRow.getValue(fieldName))
    feat.setValue("BUILDINGID", '0760737143510')
    feat.setValue("LOCATION", '0760737143510')
    #feat.setValue("SUBTYPE", 'Service Point')
    feat.setValue("CREATIONUSER", 'XCON')
    feat.setValue("DATECREATED", ds)
    feat.setValue("PROJECT_AREA", 'VARANASI')
    #feat.setValue("PHASEDESIGNATION", 'RYB')
    feat.setValue("ELECTRICTRACEWEIGHT", '2048')
    feat.setValue("TOWNCODE", '07607')
    #feat.setValue("CONNECTIONSTATUS", 'Existing')
    feat.setValue("DIVISIONNAME", 'UEDD VI-VARANASI')
    ins.insertRow(feat)
    del ins

ssGIS='40004084137'   
def getXYSS(GIS='40004084137'):
    
    arcpy.SelectLayerByAttribute_management(ss, "NEW_SELECTION",
                                           "[GISID]='%s'" % GIS)
    rows = arcpy.SearchCursor(ss)
    for row in rows:
        feat = row.getValue(ssshapefieldname)
        pnt = feat.getPart()
        #print pnt.X, pnt.Y
        return str(pnt.X)+";"+str(pnt.Y)+";"
    del rows

def getFieldsSS(GIS='40004084137'):
    
    arcpy.SelectLayerByAttribute_management(ss, "NEW_SELECTION",
                                           "[GISID]='%s'" % GIS)
    rows = arcpy.SearchCursor(ss)
    fields=descss.fields
    for row in rows:
        
        feat = row.getValue(ssshapefieldname)
        pnt = feat.getPart()
        #print pnt.X, pnt.Y
        for f in fields:
            print row.getValue(f)
        return str(pnt.X)+";"+str(pnt.Y)+";"

bpGIS='0760737143510'
def getXYBP(GIS='0760737143510'):
    
    arcpy.SelectLayerByAttribute_management(bp, "NEW_SELECTION",
                                           "[BUILDINGID]='%s'" % GIS)
    rows = arcpy.SearchCursor(bp)
    for row in rows:
        feat = row.getValue(ssshapefieldname)
        pnt = feat.getPart()
        return str(pnt.X)+";"+str(pnt.Y)
    
def createGISID(base='40028079999',n=11):
    if base[-1]=='9':
        gis=str(int(base[:-1])+1)
    else:
        gis=str(int(base)+1)

    return gis
    

def creatLT(line=""):
    cur = arcpy.InsertCursor(lt)
    pnt1 = arcpy.Point()
    pnt2 = arcpy.Point()
    pnt1.X, pnt1.Y,pnt2.X, pnt2.Y,ssGIS,bpGIS = string.split(line,";")
    
    print pnt2.X
    array = arcpy.Array([pnt1,pnt2])
    polyline = arcpy.Polyline(array)
    feat = cur.newRow()
    feat.shape = polyline
    feat.setValue("CREATIONUSER", 'XCON')
    feat.setValue("DATECREATED", ds)
    feat.setValue("PROJECT_AREA", 'VARANASI')
    feat.setValue("TOWNCODE", '07607')
    feat.setValue("DIVISIONNAME", 'UEDD VI-VARANASI')
    
    cur.insertRow(feat)
    del cur
ll=getXYSS()+getXYBP()+';'+ssGIS+';'+bpGIS
'''
for i in range(10):
    gisP=sh.cell_value(i+1,3)
    gisB=sh.cell_value(i+1,4)
    ll=getXYSS()+getXYBP()
    createLT(ll)
'''    
def createSPLT(bpgis='',ltgis=''):
    bpline=getXYBP(bpgis)
    
