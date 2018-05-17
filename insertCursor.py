#add new field in feature class
import arcpy

fc = r"C:\Rwork\p_6\Lesson3PracticeExercises\Lesson3PracticeExerciseB\USA.gdb\citiesCopy"
newField = ["NAME","CAPITAL"]

with arcpy.da.InsertCursor(fc, newField) as cursor:
        cursor.insertRow(["Kiev",3])
        del cursor
print "All done!"
