# ---------------------------------------------------------------------------
# testCreateFeatueGIS10.py
# Created on: 2011-06-06 16:19:02.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Feature_Class_Location = "D:\\"
forestBlocst_shp = "D:\\forestBlocst.shp"

# Process: Create Feature Class
arcpy.CreateFeatureclass_management(Feature_Class_Location, "testFeatureGIS10.shp", "POLYGON", "D:\\forestBlocst.shp", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 11258999068426.2;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")

