# ---------------------------------------------------------------------------
# selectByLocation.py
# Created on: 2011-07-07 00:03:33.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
New_Shapefile = "New_Shapefile.shp"
wbattributedCleaned = "wbattributedCleaned.shp"
Output_Layer = "New_Shapefile_Layer"
Output_Layer__2_ = "wbattributedCleaned_Layer1"
New_Shapefile_Layer = "New_Shapefile_Layer"
selectByLocation_lyr = "D:\\selectByLocation.lyr"

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(New_Shapefile, Output_Layer, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;Id Id VISIBLE NONE")

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(wbattributedCleaned, Output_Layer__2_, "", "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;FID_1 FID_1 VISIBLE NONE;CIRCLE CIRCLE VISIBLE NONE;DISTRICT DISTRICT VISIBLE NONE;DIVISION DIVISION VISIBLE NONE;RANGE RANGE VISIBLE NONE;BEAT BEAT VISIBLE NONE;MOUZA MOUZA VISIBLE NONE;JL_NO JL_NO VISIBLE NONE;PS PS VISIBLE NONE;F_BLOCK F_BLOCK VISIBLE NONE;F_COMP F_COMP VISIBLE NONE")

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(Output_Layer, "WITHIN", Output_Layer__2_, "", "NEW_SELECTION")

# Process: Save To Layer File
arcpy.SaveToLayerFile_management(New_Shapefile_Layer, selectByLocation_lyr, "")

