#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:30:28 2023
@author: yudichen
"""
import pandas as pd
import numpy as np
import glob
import plotly.graph_objects as go

#open the folder that contains all information
path="/Users/yudichen/Desktop/GU/ANLY 560/project_source-git/data/climate/"

#open all financial information
files = glob.glob(path+"*.csv")

temp = []

for i in files:
    if "maxtemp"  in i:
        temp.append(i)
    if "mintemp" in i:
        temp.append(i)

content = []
for file in temp:
    df = pd.read_csv(file,index_col=None)
    content.append(df)

all_info=pd.concat(content)

label= ["max_western"]*265 +['min_western']*265+['max_eastern']*265+['min_central']*265+['max_southern']*265+['min_eastern']*265+['max_central']*265+['min_southern']*265
all_info['label']=label

analytical = pd.pivot(all_info, index='Date',columns='label',values='Value').reset_index()
#analytical['Date'] = pd.to_datetime(analytical['Date'],format="%Y-%m")
analytical['Date'] = pd.to_datetime(analytical['Date'].astype(str),format="%Y%m").dt.strftime("%Y-%m")

###############################################################################

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.max_western),
               name='Max_Temp_Western',
               line=dict(color="#900D09")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.min_western),
               name='Min_Temp_Western',
               line=dict(color="#BC544B", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.max_eastern),
               name='Max_Temp_Eastern',
               line=dict(color="#0047AB")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.min_eastern),
               name='Min_Temp_Eastern',
               line=dict(color="#00B7EB", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.max_central),
               name='Max_Temp_Central',
               line=dict(color="#117755")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.min_central),
               name='Min_Temp_Central',
               line=dict(color="#98BF64", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.max_southern),
               name='Max_Temp_Southern',
               line=dict(color="#CC5500")))

fig.add_trace(
    go.Scatter(x=list(analytical.Date),
               y=list(analytical.min_eastern),
               name='Min_Temp_Southern',
               line=dict(color="#FFA500", dash="dash")))

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                method="update",
                args=[{"visible":[True, True, True, True, True, True, True, True]},
                      {"title":"Max and Min Temperature for All Regions in US"}]),
                
                dict(label="Western",
                     method="update",
                     args=[{"visible":[True, True, False, False, False, False, False, False]},
                           {"title":"Max and Min Temperature for Western US"}]),
                
                dict(label="Eastern",
                     method="update",
                     args=[{"visible":[False, False, True, True, False, False, False, False]},
                           {"title":"Max and Min Temperature for Eastern US"}]),
                
                dict(label="Central",
                     method="update",
                     args=[{"visible":[False, False, False, False, True, True, False, False]},
                           {"title":"Max and Min Temperature for Central US"}]),
                
                dict(label="Southern",
                     method="update",
                     args=[{"visible":[False, False, False, False, False, False, True, True]},
                           {"title":"Max and Min Temperature for Western US"}]),
                ]))])
fig.update_layout(title_text="Max and Min Temperature for All Regions in US")
fig.update_xaxes(title_text='Date')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(title_text='Temperature (°F)')
fig.update_yaxes(showgrid=False)

fig.write_html("data-viz_temp.html")
