#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:18:02 2023

@author: yudichen
"""

import pandas as pd
import os
import glob

data_files = r"/Users/yudichen/Desktop/GU/ANLY 560/project_source-git/data/climate"
climate= pd.DataFrame()
climate= pd.concat(map(pd.read_csv,glob.glob(os.path.join(data_files,'32*.csv'))), ignore_index= True)
#climate = climate.fillna(0)

national = climate.groupby(by=["DATE"], dropna=True).mean()
national.to_csv("national_weather_condition.csv")