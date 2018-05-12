import arcpy
arcpy.env.workspace = r"C:\Rwork\p_6\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb"
arcpy.CopyFeatures_management("Cities", "CitiesCopy")
fc = r"C:\Rwork\p_6\Lesson2PracticeExercise\Lesson2PracticeExercise\USA.gdb\CitiesCopy"

# Set local variables
fieldName = "CAPITAL_RANGE"
fieldPrecision = 3
fieldAlias = "range_cap"

# Get a list of field objects
fields = arcpy.ListFields(fc)
expression = "getRange(float(!CAPITAL!))"
codeblock = """def getRange(capital):
    if capital < 0:
        return 0
    return 1"""

if fieldName not in fields:
    arcpy.AddField_management(fc, fieldName, "SHORT", fieldPrecision, field_alias=fieldAlias, field_is_nullable="NULLABLE")
    arcpy.CalculateField_management(fc, fieldName, expression, "PYTHON_9.3", codeblock)
