
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
df.name
lyr = arcpy.mapping.ListLayers(mxd)[0]
lyr.name
fld=arcpy.ListFields(lyr)

ff=arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION",
                                           "[BUILDINGID]='%s'" %'0760737143510')
rows = arcpy.SearchCursor(lyr) 
ins = arcpy.UpdateCursor(lyr)
