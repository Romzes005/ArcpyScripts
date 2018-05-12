# Finds the average population in a counties dataset

import arcpy

featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)

'''
where_clause = '"NAME"='+"'Krim'"

rows = arcpy.SearchCursor(featureClass, where_clause, fields=populationField)
row = rows.next()

while row:
    print row.getValue("NAME")
    row = rows.next()
'''

with arcpy.da.SearchCursor(featureClass, (populationField,) , '"NAME"='+"'Krim'") as cursor:
    for row in cursor:
        print arcpy.addMessege(tr(row[0]))
