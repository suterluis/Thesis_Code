#This script will calculates the differences between years (2050-2006; 2050-1970; 2006-1970) for each GCM and each variable
# it then calculates the mean change from all gcms for each variable within each time year


import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\1970_2006_2050"
arcpy.env.overwriteOutput = True
print "workspace set"

rasters = arcpy.ListRasters("*")

for raster in rasters:
	gcms = ["canesm","csiro_","gfdl__","hadgem","ipsl__","noresm"]
	for gcm in gcms:
		variables = ["ta", "fu", "gt", "al", "pr", "fd", "ft", "wr", "ht"]
		for variable in variables:
			algebra50_06 = '"%s_2050%s"-"%s_2006%s"' %(gcm,variable,gcm,variable)
			save50_06 = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-2006\\%s_%s" %(gcm,variable)
			arcpy.gp.RasterCalculator_sa(algebra50_06,save50_06)
			print "Calculated %s 2050-2060 %s" %(gcm,variable)
			algebra50_70 = '"%s_2050%s"-"%s_1970%s"' %(gcm,variable,gcm,variable)
			save50_70 = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-1970\\%s_%s" %(gcm,variable)
			arcpy.gp.RasterCalculator_sa(algebra50_70,save50_70)
			print "Calculated %s 2050-1970 %s" %(gcm,variable)
			algebra06_70 = '"%s_2006%s"-"%s_1970%s"' %(gcm,variable,gcm,variable)
			save06_70 = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2006-1970\\%s_%s" %(gcm,variable)
			arcpy.gp.RasterCalculator_sa(algebra06_70,save06_70)
			print "Calculated %s 2006-1970 %s" %(gcm,variable)
		
print "Done Calculating Differences"


#reset workspace and average the 6 models together for each variable (2050-2006)
arcpy.env.workspace = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-2006"
arcpy.env.overwriteOutput = True
Average50_06 = arcpy.ListRasters("*")
for average in Average50_06:
	variables = ["ta", "fu", "gt", "al", "pr", "fd", "ft", "wr", "ht"]
	for variable in variables:
		algebra = '("canesm_%s"+"csiro_%s"+"gfdl_%s"+"hadgem_%s"+"ipsl_%s"+"noresm_%s")/6'%(variable,variable,variable,variable,variable,variable)
		save =  "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-2006\\GCM_Mean_%s" %(variable)
		arcpy.gp.RasterCalculator_sa(algebra,save)
		print "Averaged %s" %(variable)


		
#reset workspace and average the 6 models together for each variable (2050-1970)
arcpy.env.workspace = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-1970"
arcpy.env.overwriteOutput = True
Average50_70 = arcpy.ListRasters("*")
for average in Average50_70:
	variables = ["ta", "fu", "gt", "al", "pr", "fd", "ft", "wr", "ht"]
	for variable in variables:
		algebra = '("canesm_%s"+"csiro_%s"+"gfdl_%s"+"hadgem_%s"+"ipsl_%s"+"noresm_%s")/6'%(variable,variable,variable,variable,variable,variable)
		save =  "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2050-1970\\GCM_Mean_%s" %(variable)
		arcpy.gp.RasterCalculator_sa(algebra,save)
		print "Averaged %s" %(variable)


#reset workspace and average the 6 models together for each variable (2006-1970)
arcpy.env.workspace = "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2006-1970"
arcpy.env.overwriteOutput = True
Average06_70 = arcpy.ListRasters("*")
for average in Average06_70:
	variables = ["ta", "fu", "gt", "al", "pr", "fd", "ft", "wr", "ht"]
	for variable in variables:
		algebra = '("canesm_%s"+"csiro_%s"+"gfdl_%s"+"hadgem_%s"+"ipsl_%s"+"noresm_%s")/6'%(variable,variable,variable,variable,variable,variable)
		save =  "R:\\Streletskiy Research\\Luis_Files\\Thesis\\GCM_Results\\TIFFs\\2006-1970\\GCM_Mean_%s" %(variable)
		arcpy.gp.RasterCalculator_sa(algebra,save)
		print "Averaged %s" %(variable)


			
print "GCM Averages Calculated"