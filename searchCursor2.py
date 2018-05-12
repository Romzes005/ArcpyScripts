import arcpy

inTable = r"C:\Rwork\p_6\Lesson2\Lesson2\CityBoundaries.shp"

rows = arcpy.SearchCursor(inTable)

# This loop goes through each row in the table
#  and gets a requested field value
field_names = [f.name for f in arcpy.ListFields(inTable)]

# print field_names

for row in rows:
    # currentCity = row.getValue(inField) #print currentCity
    print "++++++++++++++++++++"
    for col in field_names:
        currentCity = row.getValue(col)
        print str(col) + " -> " + str(currentCity)
