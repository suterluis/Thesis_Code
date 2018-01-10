# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# climate__raster.py
# Created on: 2018-01-10 10:04:44.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: climate__raster <Z_value_field> <output> <X_Field> <Y_Field> <HadGEM_2006_2050_csv> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os

print "imported"

#set workspace
arcpy.env.workspace = "R:\\Streletskiy Research\\Luis_Files\\Thesis\GCM_Results\\CSVs\\2006_2050"
arcpy.env.overwriteOutput = True


# Script arguments
file = "CanESM_2006_2050.csv"

Z_value_field = ["ta", "h_snow", "fu", "magt", "altr", "altr_alt", "pr", "fdi", "ftc", "winter_road", "heating_period"]
X_Field = "lat"
Y_Field = "lon"
spRef  = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision"
xy_output = "temp_layer"

print "variables set"

arcpy.MakeXYEventLayer_management(file, X_Field, Y_Field, xy_output, spRef)
print "xy made"

save_file = "R:\\Streletskiy Research\\Luis_Files\\Thesis\GCM_Results\\TIFFs\\2006_2050\\CanESM_'%s'" %(Z_value)
for Z_value in Z_value_field:
	arcpy.gp.NaturalNeighbor_sa(xy_output, Z_value, save_file, "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GIS\\Rasterization_Files\\1x1_standard") %(Z_value)
	
print "Done"
	




