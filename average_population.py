# Finds the average population in a counties dataset
import arcpy

featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)


#featureClass = r"C:\Rwork\p_6\Lesson2\Pennsylvania\Pennsylvania\counties.shp"

rows = arcpy.SearchCursor(featureClass)
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

# Loop through each row and keep running total of population
# and records counted.
while row:
    totalPopulation += row.getValue(populationField) ###totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()
average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)
arcpy.AddMessage("Average population for a county is " + str(average))