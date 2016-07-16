import arcpy
mxd=arcpy.mapping.MapDocument(r"D:\Project.mxd")
df=arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
scalebar=arcpy.mapping.ListLayoutElements(mxd,"MAPSURROUND_ELEMENT","ScaleBar")[0]

scalebar.elementPositionX=df.elementPositionX+(df.elementWidth/2)
mxd.save()
del mxd
                              
