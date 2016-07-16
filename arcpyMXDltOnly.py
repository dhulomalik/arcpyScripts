import arcpy

mxd = arcpy.mapping.MapDocument(r"I:\DataNScripts\Enterprise\awasvikas\puvvnl.mxd")

lt=arcpy.mapping.ListLayers(mxd,"LT Overhead Line")[0]
desclt = arcpy.Describe(lt)
ltshapefieldname = desclt.ShapeFieldName
#desclt = arcpy.Describe(lt)
#ltshapefieldname = desclt.ShapeFieldName
arcpy.SelectLayerByAttribute_management(lt, "NEW_SELECTION",
                                           "[GISID]='%s'" %'40020076137')
rows = arcpy.SearchCursor(lt)
c=arcpy.GetCount_management(lt)
count = int(c.getOutput(0))

