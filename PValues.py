# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:57:45 2020

@author: Artem
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
merge_df = pd.DataFrame()

path = 'C:/Users/gorba/.spyder-py3/WORKS/pvaudes/' # name the path of the files 
from os import listdir 
files = listdir(path) 
txt = [x for x in files if x.endswith('.xlsx')] # make a list of all files that we will use
for x in txt:
    df = pd.read_excel(path + x)
    df.set_index('Variable', inplace=True)
    
    df_sort = df.loc[['Seasonal flood runoff (with groundwater)', # names of colums that we will agregate in files
    'Rain-flood runoff (with groundwater)',
    'Thaw-flood runoff (without groundwater)',
    'Maximum annual discharge during seasonal flood wave',
    'Minimum 10-day window discharge during winter',
    'Minimum 10-day window discharge during summer',
    'Maximum thaw-flood discharge',
    'Number of thaw-flood events',
    'Maximum rain-flood discharge',
    'Number of rain-flood events',
    ], 'M1':'M2']
    
    df_sort = df_sort.astype(float) # agrigate data in one file
    df_sort['M_mean'] =  df_sort['M2'] - df_sort['M1']
    df_sort.reset_index(inplace = True)
    df_sort['Post'] = x
    df_sort.groupby('Post')
    
    df_pivot = df_sort.pivot(index='Post', columns='Variable') # transoniring table 
    #print(df_pivot.columns)
    merge_df = pd.concat([merge_df, df_pivot], axis = 0)
#merge_df.reset_index(inplace = True)  
merge_df.to_excel("output_PVaudes_NEW.xlsx")#, index=True)#, merge_cells = True)

