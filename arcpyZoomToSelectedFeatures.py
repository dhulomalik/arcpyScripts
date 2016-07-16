import arcpy
from arcpy.mapping import *

mxd=arcpy.mapping.MapDocument(r"d:\current.mxd")
df=arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
for lyr in arcpy.mapping.ListLayers(mxd):
    print("Layer Name:",lyr.name)

print df.displayUnits
print df.scale
print df.mapUnits
df.scale=100000
print df.extent
print df.scale

# Local variables:
fire01_11 = "d:\\fire01_11.shp"
fireLayer = "fireLayer"

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(fire01_11, fireLayer, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;LATITUDE LATITUDE VISIBLE NONE;LONGITUDE LONGITUDE VISIBLE NONE;BRIGHTNESS BRIGHTNESS VISIBLE NONE;SCAN SCAN VISIBLE NONE;TRACK TRACK VISIBLE NONE;ACQ_DATE ACQ_DATE VISIBLE NONE;ACQ_TIME ACQ_TIME VISIBLE NONE;SATELLITE SATELLITE VISIBLE NONE;CONFIDENCE CONFIDENCE VISIBLE NONE;VERSION VERSION VISIBLE NONE;BRIGHT_T31 BRIGHT_T31 VISIBLE NONE;FRP FRP VISIBLE NONE")




