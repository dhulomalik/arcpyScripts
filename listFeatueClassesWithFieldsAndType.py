import arcpy

logfile = open(r'C:\Users\ajay\Documents\gis\TMP\ListFCs_ListFieldNames_ListFieldTypes.log', 'w')

def log_results(message):
    print(message)
    logfile.write(message)
    logfile.flush()
    return

def main():
    try:
        #wk = arcpy.env.workspace = 'Database Connections/ORCL - SDE@SRVRNAME.sde'
        #wk = arcpy.env.workspace = 'Database Connections\New.sde'
        #wk='C:\Users\ajay\Documents\gis\PuVVNL_VARANASI_DIV_5_8OCT15 - Copy.mdb'
        wk = arcpy.env.workspace = 'Database Servers\AJAY-PC_SQLEXPRESS.gds\CheckOutNew (VERSION:dbo.DEFAULT)'
        fdsList = arcpy.ListDatasets("*")
        #fcList = arcpy.ListFeatureClasses("*")
        fcList = arcpy.ListFeatureClasses(feature_dataset=fdsList[0])
        fcList.sort()

        if not arcpy.Exists(wk):
            log_results("\n" + " SDE Connection File DOES NOT EXIST!!\n")
            
        else:
            fcCnt = 0
            fldCnt = 0

            for fc in fcList:
                fcCnt += 1
                desc = arcpy.Describe(fc)
                log_results ("\n Feature Class Name : {0}  \n Geometry Type      : {1}  \n Has Spatial Index  : {2}  \n Spatial Reference  : {3}".format(fc,desc.shapeType,str(desc.hasSpatialIndex),desc.spatialReference.name))
                #field = [f.name for f in arcpy.ListFields(fc)]
                fields = arcpy.ListFields(fc)
                fldCnt = 0
                for field in fields:
                    log_results ("\n    Field Name : {0: <24}  Field Type : {1: <20}  Field Length : {2}".format(field.name, field.type, field.length))
                    fldCnt += 1
                log_results ("\n # of Fields in Feature Class '{0}' = {1} \n".format(fc, fldCnt))

        log_results ("\n TOTAL # OF FEATURE CLASSES LISTED = {0}".format(fcCnt))
        log_results ("\n\n COMPLETED!! \n")

        logfile.close()

    except arcpy.ExecuteError:
        log_results (arcpy.GetMessages(2))

    except Exception as e:
        log_results (e[0])

if __name__ == '__main__':
    main()
