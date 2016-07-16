# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# IteratorModelBuilderExperimentTables.py
# Created on: 2016-07-16 12:40:01.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
PuVVNL_VARANASI_DIV6_2DEC15-Copy_mdb = "C:\\Users\\ajay\\Documents\\gis\\VARANASI_DIV6\\PuVVNL_VARANASI_DIV6_2DEC15-Copy.mdb"

# Process: Iterate Tables
arcpy.IterateTables_mb(PuVVNL_VARANASI_DIV6_2DEC15-Copy_mdb, "", "", "RECURSIVE")
