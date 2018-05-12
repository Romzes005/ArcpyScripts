import arcpy

fc = r"C:\Users\Sheol\Desktop\2013-14\2015-2016\ProgramGIS\ArcPy\Lesson2\PracticeData\USA.gdb\CitiesCopy"

# Get a list of field objects
#
fields = arcpy.ListFields(fc, 'CAPITAL')

for field in fields:
    # Check the field name, perform a calculation when finding the field 'Flag'
    #
    if field.name == 'CAPITAL':
        # Set the NEW value for the field and exit loop
        #
        arcpy.CalculateField_management(fc, 'CAPITAL', '1')
        break
