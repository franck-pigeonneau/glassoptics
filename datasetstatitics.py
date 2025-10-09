#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:59:51 2024

@author: fpigeonneau
"""

import numpy as np
from matplotlib import pyplot as plt
from glassdata import GlassData

def pdfy(y,PATH,propertyname):
    N=np.size(y)
    Nbins=int(np.sqrt(N))
    pdfproperty,bin_edges=np.histogram(y,bins=Nbins,range=(np.min(y),np.max(y)),\
                                       density=True)
    binsize=bin_edges[1]-bin_edges[0]
    mid_points=bin_edges[:-1]+0.5*binsize

    plt.figure()
    plt.bar(mid_points,pdfproperty,width=binsize,color='k',edgecolor='k',\
            linewidth=1,fill=False)
    plt.xlabel(propertyname,fontsize=14)
    plt.ylabel(r'PDF of '+propertyname,fontsize=14)
    plt.savefig(PATH+'pdf'+propertyname+'.pdf',dpi=300,bbox_inches='tight')
#end pdfy

# Name of the database of glass
filedb='DataSet/V.csv'
PATH='Figures/'
db=GlassData(filedb)
db.bounds()

plt.figure()
plt.bar(db.oxide,db.occurence,color='k')
plt.xticks(rotation=90,fontsize=14)
plt.ylabel('$N$',fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(PATH+'noccurencevsoxide'+db.nameproperty+'.png',dpi=300,bbox_inches='tight')

plt.figure()
plt.bar(db.oxide,db.xmax,color='k')
plt.xticks(rotation=90,fontsize=14)
plt.ylabel('max$(x_i)$',fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(PATH+'xmolarmaxvsoxide'+db.nameproperty+'.png',dpi=300,bbox_inches='tight')

pdfy(db.y,PATH,db.nameproperty)
