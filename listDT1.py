import arcpy
mxd = arcpy.mapping.MapDocument('CURRENT')
df = mxd.activeDataFrame
lyrs = arcpy.mapping.ListLayers(mxd, "Distribution Transformer", df)
lyr = lyrs[0]
listDT=[]
listFeeder=[]
with arcpy.da.SearchCursor(lyr, ['GISID', 'DTRNAME','FEEDERNAME','SUBSTATIONNAME']) as cursor:
    for row in cursor:
        listDT.append(row[0])
        listFeeder.append(row[2])
setFeeder=set(listFeeder)
#expression = arcpy.AddFieldDelimiters(lyr, 'FEEDERNAME') + " = 'TRILOCHAN'"
expression='FEEDERNAME="TRILOCHAN"'

subsetDT=[]
with arcpy.da.SearchCursor(lyr, ['GISID', 'DTRNAME',],where_clause=expression) as cursor:
    for row in cursor:
        subsetDT.append(row[1])

arcpy.SelectLayerByAttribute_management(lyr,'NEW_SELECTION',' DTRNAME = "%s" ' %subsetDT[0])
#arcpy.CopyFeatures_management(lyr, "dtFlag")
#temp dtf by MakeFeatureLayer
#dtf=arcpy.MakeFeatureLayer_management(lyr, "dtFlag1")
#and permanent on disk by CopyFeatures_management
dtf=arcpy.CopyFeatures_management(lyr, "dtFlag1")
#or even SaveToLayerFile_management after MakeFeatureLayer


Elec_Net = r"C:\Users\ajay\Desktop\PuVVNL_VARANASI_DIV_3_16OCT15 - ajay.mdb\ElectricDataset\ElectricDataset_Net"
arcpy.SetFlowDirection_management(Elec_Net, "WITH_DIGITIZED_DIRECTION")
arcpy.gp.TraceGeometricNetwork(Elec_Net, "Elec_NET1", dtf, "TRACE_DOWNSTREAM", "", "", "", "", "", "NO_TRACE_ENDS", "", "", "", "AS_IS", "", "", "", "AS_IS")
layers1 = arcpy.mapping.ListLayers(mxd)
soh = []
for l in layers1:
    if l.isGroupLayer:
        if l.name == "Elec_NET1":
            
            print "Found"
            for subLayer in l:
                print subLayer.name
                if subLayer.name == "SecOHElectricLineSegment":
                    soh = []
                    rows = arcpy.SearchCursor("SecOHElectricLineSegment","","","OBJECTID")
                    for row in rows:
                        soh.append(row.getValue("OBJECTID"))
                    del rows, row


'''
layer.labelClasses[0].expression = "[<field expression here>]"
layer.showLabels = True
arcpy.RefreshActiveView()

layer.labelClasses[0].expression = "[GISID]"
layer.labelClasses[0].expression=layer.labelClasses[0].expression+"+[OBJECTID]"


import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT") 
layer = arcpy.mapping.ListLayers(mxd, "")[0] 
if layer.supports("LABELCLASSES"):
    for lblclass in layer.labelClasses:
        lblclass.showClassLabels = True
lblclass.expression = " [Label]"
layer.showLabels = True
arcpy.RefreshActiveView()


import arcpy
from arcpy import env

# Set the current workspace
env.workspace = "C:/data"

# Set layer to apply symbology to
inputLayer = "sf_points.lyr"

# Set layer that output symbology will be based on
symbologyLayer = "water_symbols_pnt.lyr"

# Apply the symbology from the symbology layer to the input layer
arcpy.ApplySymbologyFromLayer_management (inputLayer, symbologyLayer)

'''
#turn on and off a layer from Map and TOC
dtlyr=lyrs = arcpy.mapping.ListLayers(mxd, "dtFlag1", df)[0]
dtlyr.visible=False

df.scale=10000
df.zoomToSelectedFeatures()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()





