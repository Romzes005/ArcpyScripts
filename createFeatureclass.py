import arcpy

try:
    arcpy.env.workspace = r"C:\Rwork\p_6\Lesson2\Lesson2\PractiseData\Precip"

    template = "C:\Rwork\p_6\Lesson2\Lesson2\PractiseData\Precip2008Readings.shp"

    for year in range(2009, 2013):
        newfile = "Precip" + str(year) + "Readings.shp"
        arcpy.CreateFeatureclass_management(arcpy.env.workspace, newfile, "POINT", template,
                                            "DISABLED", "DISABLED", template)

except:
    print arcpy.GetMessages()
