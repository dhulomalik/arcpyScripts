# ---------------------------------------------------------------------------
# Test1.py
# Created on: 2011-07-06 23:53:10.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
wbattributedCleaned = "wbattributedCleaned.shp"
wbattributedCleaned_Layer = "wbattributedCleaned_Layer"
wbattributedCleaned_Layer__2_ = "wbattributedCleaned_Layer"
BTR_W__lyr = "D:\\BTR(W).lyr"

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(wbattributedCleaned, wbattributedCleaned_Layer, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;FID_1 FID_1 VISIBLE NONE;CIRCLE CIRCLE VISIBLE NONE;DISTRICT DISTRICT VISIBLE NONE;DIVISION DIVISION VISIBLE NONE;RANGE RANGE VISIBLE NONE;BEAT BEAT VISIBLE NONE;MOUZA MOUZA VISIBLE NONE;JL_NO JL_NO VISIBLE NONE;PS PS VISIBLE NONE;F_BLOCK F_BLOCK VISIBLE NONE;F_COMP F_COMP VISIBLE NONE")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(wbattributedCleaned_Layer, "NEW_SELECTION", "\"DIVISION\" = 'BTR WEST'")

# Process: Save To Layer File
arcpy.SaveToLayerFile_management(wbattributedCleaned_Layer__2_, BTR_W__lyr, "")
