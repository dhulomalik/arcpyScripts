# ---------------------------------------------------------------------------
# selectByLocationModelBuilderScript.py
# Created on: 2015-08-23 19:41:54.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Distribution_Transformer__2_ = "Distribution Transformer"
DistributionTransformer_Sele = "C:\\Users\\ajay\\Documents\\ArcGIS\\Default1.gdb\\DistributionTransformer_Sele"

# Process: Select
arcpy.Select_analysis(Distribution_Transformer__2_, DistributionTransformer_Sele, "[GISID] = '400090512' OR '400090513' OR '400090515'")

