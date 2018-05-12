# Finds the average population in a counties dataset

import arcpy

featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)

average = 0
totalPopulation = 0
recordsCounted = 0

with arcpy.da.SearchCursor(featureClass, (populationField,)) as cursor:
    for row in cursor:
        totalPopulation += row[0]
        recordsCounted += 1

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
arcpy.AddMessage("Average population for a county is " + str(average))