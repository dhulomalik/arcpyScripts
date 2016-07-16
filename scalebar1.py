import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Project\Projec4t.mxd")
scaleBar = arcpy.mapping.ListLayoutElements(mxd, "MAPSURROUND_ELEMENT", "ScaleBar")[0]
df = arcpy.mapping.ListDataFrames(mxd, scaleBar.parentDataFrameName)[0]
scaleBar.elementPositionX = df.elementPositionX + (df.elementWidth / 2)
mxd.save()
