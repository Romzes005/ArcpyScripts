import arcpy

featureClass = r"C:\Rwork\p_6\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\Cities"

# Get a list of field objects

#fields = arcpy.ListFields(fc, 'CAPITAL')
'''
for field in fields:
    # Check the field name, perform a calculation when finding the field 'Flag'
    #
    if field.name == 'CAPITAL':
        # Set the NEW value for the field and exit loop
        #
        arcpy.CalculateField_management(featureClass, 'CAPITAL', '1')
        break
'''

desc = arcpy.Describe(featureClass)

for field in desc.fields:
    print field.name