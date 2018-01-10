# Thesis_Code
These are the buggy processes I have put up for review while automating the processing for my Thesis code.


Process: Take a list of CSVs (global climate model outputs), create XY event layer for each, and then create a set of raster for a list of variables contained in each  XY event layer.

Problem:  Having issues iterating the proccess through my list of CSVs and Variables. For loops maybe not working?

Success so far: "Climate_Raster_alt" - by loading just 1 CSV, I was able to get the full process to execute, but it only made a raster for the first Z variable: 'ta' 
There is obviously  still some kind off issue with my for looping

This represents a work in progress. Once complete, the full code will be made available. 
