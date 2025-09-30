#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:12:57 2023

This script is used to created a data set from a csv file saved from Interglad V8.

    filename : String
        Name of the database built from the database Interglad V8.
        xtotal : Float
        Bound admited in the sum of oxides for each glass sample.
        probamin : Float
        Minimum of the probability of occurence of oxide or proprety.
        probamax : Float
        Maximum of the probability of occurence of oxide or proprety.
        xminor : Float
        Minimum value of the oxide to be considered to be significant.
        minoxidefraction : Float
        Minimum fraction of glasses with a specific oxide in the composition
        Plot : Boolean
        Parameter giving the choice to plot the pdf of the property.
        
@author: Franck Pigeonneau
"""

from glassdata import GlassData

# Preparing data
filename='DataSet/ndInterglad.csv'
xtotal=0.98
xminor=0.01
probamin=0.02
probamax=0.99
filteringoxide=False
minoxidefraction=0.
Plot=True
db=GlassData()
db.nameproperty='nd'
db.datacleaning(filename,xtotal,probamin,probamax,xminor,minoxidefraction,filteringoxide,Plot)

# save of the clean and filtered data
filesavedata='DataSet/'+db.nameproperty+'.csv'
db.savedata(filesavedata)
