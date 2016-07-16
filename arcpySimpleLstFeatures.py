import arcpy
from arcpy import env

# Set the workspace. List all of the feature classes that start with 'G'
#
env.workspace = "C:/Users/ajay/Documents/gis/VARANASI_DIV6/PuVVNL_VARANASI_DIV6_2DEC15-Copy.mdb"
fcds = arcpy.ListDatasets()
