import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
sp=arcpy.mapping.ListLayers(mxd,"Service Point")[0]
ff=arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION",
                                           "[BUILDINGID]='%s'" %'0760737143510')

                                           "[BUILDINGID]='%s'" %'0760737143510')
arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION","[GISID]='%s'" % 40009122090)
arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION","[GISID]='%s'" % '40009122090')
sp
fld=arcpy.ListFields(sp)
fld
for f in fld:
    print f.name

arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION","[ServicePoint.GISID]='%s'" % '40009122090')
arcpy.SelectLayerByAttribute_management(sp, "NEW_SELECTION","[GISID]='%s'" % '40009122090')
arcpy.CopyFeatures_management(sp, spSelect)
arcpy.CopyFeatures_management(sp, "spSelect")
arcpy.SelectLayerByLocation_management(lt, rel, selectFeatures)
lt=arcpy.mapping.ListLayers(mxd,"LT Overhead Line")[0]
arcpy.SelectLayerByLocation_management(lt,"WITHIN_A_DISTANCE", spSelect,0.1)
sps=arcpy.CopyFeatures_management(sp, "spSelect")
sps=arcpy.CopyFeatures_management(sp, "spSelect1")
arcpy.SelectLayerByLocation_management(lt,"WITHIN_A_DISTANCE", sps,0.1)
arcpy.SelectLayerByLocation_management(lt,"WITHIN_A_DISTANCE", sps,0.1)
dir(sps)
sps=arcpy.CopyFeatures_management(sp)
dir(sp)
