# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# lisDatasetsAndCopyModelBuilder.py
# Created on: 2016-07-16 18:00:51.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
CheckOutNew__VERSION_dbo_DEFAULT_ = "Database Servers\\AJAY-PC_SQLEXPRESS.gds\\CheckOutNew (VERSION:dbo.DEFAULT)"
Dataset = "Database Servers\\AJAY-PC_SQLEXPRESS.gds\\CheckOutNew (VERSION:dbo.DEFAULT)\\CheckOutNew.DBO.Landbase"
Dataset_Copy = "C:\\Users\\ajay\\Documents\\ArcGIS\\Default.gdb\\Dataset_Copy"

# Process: Iterate Datasets
arcpy.IterateDatasets_mb(CheckOutNew__VERSION_dbo_DEFAULT_, "", "", "NOT_RECURSIVE")

# Process: Copy
arcpy.Copy_management(Dataset, Dataset_Copy, "")
