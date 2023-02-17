#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:05:22 2023

@author: yudichen
"""

import pandas as pd

covid = pd.read_csv("/Users/yudichen/Desktop/GU/ANLY 560/project_source-git/data/COVID/COVID-19_Vaccinations_in_the_United_States_Jurisdiction.csv")

distribution = covid.groupby('Date').sum()[[i for i in covid.columns if i.startswith('Distributed')]].reset_index()
distribution = distribution.iloc[:,:7]

analytical = pd.melt(distribution,id_vars='Date',value_vars=[i for i in distribution.columns if i.startswith('Distributed_')])
analytical[['a','Distributor']] = analytical.variable.str.split('_',1,expand=True)
analytical = analytical.drop(['a','variable'],axis=1)
analytical = analytical.rename(columns={'value':'num_vaccine'})

analytical.to_csv("analytical-covid-distribution_vaccine.csv",index=False)

covid['Date'] = pd.to_datetime(covid['Date'])
administrated = covid[covid['Date'] =='2/1/2023']

states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

administrated = administrated[administrated['Location'].isin(states)]
administrated.to_csv("analytical-covid-administrated_vaccine.csv",index=False)


completion = covid[covid.Location =='US']
cols = ['Date','Administered_Dose1_Recip',"Series_Complete_Yes","Additional_Doses","Second_Booster"]
completion = completion[(completion.columns&cols)]
completion = pd.melt(completion,id_vars='Date',value_vars=cols)
completion.to_csv("analytical-covid-completion_vaccine.csv",index=False)
