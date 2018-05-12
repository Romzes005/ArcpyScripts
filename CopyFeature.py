# Copies all feature classes from one folder to another
import arcpy

try:
    arcpy.env.workspace = "C:\\Rwork\\p_6\\Lesson_1\\Lesson1"

    # List the feature classes in the Lesson 1 folder
    fcList = arcpy.ListFeatureClasses()

    # Loop through the list and copy the feature classes to the Lesson 2 PracticeData folder
    for featureClass in fcList:
        arcpy.CopyFeatures_management(featureClass, "C:\\Rwork\\p_6\Lesson2\\Lesson2\\PractiseData\\" + featureClass)

except:
    print "Script failed to complete"
    print arcpy.GetMessages(2)
