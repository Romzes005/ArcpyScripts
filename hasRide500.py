# Selects park and ride facilities with over a certain number of parking spots
# and exports them to a new feature class using CopyFeatures

import arcpy
parkingSpaces = 500
arcpy.env.workspace=r"C:\Rwork\p_6\Lesson3PracticeExercises\Lesson3PracticeExercises\Lesson3PracticeExerciseC\Washington.gdb"

# Set up the SQL expression to query the parking capacity
parkingQuery = '"Approx_Par" > ' + str(parkingSpaces)

# Make a feature layer of park and rides that applies the SQL expression
arcpy.MakeFeatureLayer_management("ParkAndRide", "ParkAndRideLayer", parkingQuery)

# Copy the features to a new feature class and clean up
arcpy.CopyFeatures_management("ParkAndRideLayer", "BigParkAndRideFacilities")
arcpy.Delete_management("ParkAndRideLayer")
