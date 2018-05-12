# Finds the average population in a counties dataset

import arcpy


#featureClass = r"C:\Rwork\p_6\Lesson2\Pennsylvania\Pennsylvania.gdb\counties"
#populationField = "POP1990"

featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)

with arcpy.da.SearchCursor(featureClass, (populationField,) , '"POP1990" >= 5000 AND "POP1990" <= 100000 ') as cursor:
    for row in cursor:
        print str(row[0])
        arcpy.AddMessage(str(row[0]))
