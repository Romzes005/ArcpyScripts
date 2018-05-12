# This script clips all datasets in a folder
import arcpy

inFolder = r"C:\Rwork\p_6\Lesson2\Lesson2"
resultsFolder = r"C:\Rwork\p_6\Lesson2\Lesson2\PractiseData\Result"
clipFeature = r"C:\Rwork\p_6\Lesson_1\Lesson1\Nebraska.shp"

# List feature classes
arcpy.env.workspace = inFolder
featureClassList = arcpy.ListFeatureClasses()

# Loop through each feature class and clip
for featureClass in featureClassList:
    # Make the output path by concatenating strings
    outputPath = resultsFolder + "/" +  featureClass
    # Clip the feature class
    arcpy.Clip_analysis(featureClass, clipFeature, outputPath)
