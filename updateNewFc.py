# Selects park and ride facilities in a given target city and
# exports them to a new feature class
import arcpy
targetCity = "Federal Way" # Name of target city
arcpy.env.workspace=r"C:\Rwork\p_6\Lesson3PracticeExercises\Lesson3PracticeExerciseC\Washington.gdb"
parkAndRide = "ParkAndRide" # Name of P & R feature class
cities = "CityBoundaries" # Name of city feature class

# Set up the SQL expression of the query for the target city
cityQuery = '"NAME" = ' + "'" + targetCity + "'"

# Make feature layers for the cities and park and rides
arcpy.MakeFeatureLayer_management(cities, "CitiesLayer", cityQuery)
arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")

# Select all park and rides in the target city
arcpy.SelectLayerByLocation_management("ParkAndRideLayer", "CONTAINED_BY", "CitiesLayer")

# Copy the features to a new feature class and clean up
arcpy.CopyFeatures_management("ParkAndRideLayer", "TargetParkAndRideFacilities")

arcpy.Delete_management("ParkAndRideLayer")
arcpy.Delete_management("CitiesLayer")
