import arcpy
mxd=arcpy.mapping.MapDocument(r"D:\Project2.mxd")
df=arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
wbattributedCleaned_Layer = "d:\\wbattributedCleaned.shp"
wbattributedCleaned_Layer1 = "wbattributedCleaned_Layer1"

# Process: Make Feature Layer
p=arcpy.MakeFeatureLayer_management(wbattributedCleaned_Layer, wbattributedCleaned_Layer1, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;FID_1 FID_1 VISIBLE NONE;CIRCLE CIRCLE VISIBLE NONE;DISTRICT DISTRICT VISIBLE NONE;DIVISION DIVISION VISIBLE NONE;RANGE RANGE VISIBLE NONE;BEAT BEAT VISIBLE NONE;MOUZA MOUZA VISIBLE NONE;JL_NO JL_NO VISIBLE NONE;PS PS VISIBLE NONE;F_BLOCK F_BLOCK VISIBLE NONE;F_COMP F_COMP VISIBLE NONE")

# Process: Select Layer By Attribute
t=arcpy.SelectLayerByAttribute_management(wbattributedCleaned_Layer1, "NEW_SELECTION", "\"RANGE\" = 'SALUGURAHA'")



texts=arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT")
elements=arcpy.mapping.ListLayoutElements(mxd,"MAPSURROUND_ELEMENT")
print len(elements)
#df.zoomToSelectedFeatures()
#df.scale=1000000


#arcpy.mapping.ExportToGIF(mxd,"D:\\test556.gif")




                              
