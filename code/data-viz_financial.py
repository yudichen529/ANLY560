# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import glob
import altair as alt

#open the folder that contains all information
path="/Users/yudichen/Desktop/GU/ANLY 560/project_source-git/data/financial/"

#open all financial information
files = glob.glob(path+"*.csv")

content = []
for file in files:
    df = pd.read_csv(file,index_col=None)

    content.append(df)

all_info=pd.concat(content)
all_info=all_info.groupby('Unnamed: 0').sum().reset_index()
all_info.replace(0,np.nan , inplace=True)

select_col = [i for i in all_info.columns if i.endswith(('Adjusted','Volume',"0"))]

price_vol = all_info[select_col]
price_vol = price_vol.rename(columns={df.columns[0]:'date'})

###############################################################################

price_vaccine = pd.melt(price_vol, id_vars='date', value_vars=['JNJ.Adjusted','PFE.Adjusted','MRNA.Adjusted'])
volume_vaccine = pd.melt(price_vol, id_vars='date', value_vars=['JNJ.Volume','PFE.Volume','MRNA.Volume'])
vaccine = price_vaccine.merge(volume_vaccine,on='date',how="inner")
vaccine = vaccine.drop_duplicates(["date",'variable_x'])
vaccine[['ticker','b']] = vaccine.variable_x.str.split(".",expand=True)
vaccine = vaccine.drop(['variable_x','variable_y','b'],axis=1)
vaccine = vaccine.rename(columns={'value_x':'price','value_y':'volume'})

vaccine = vaccine[vaccine['ticker'].isin(['PFE','JNJ','MRNA'])]
vaccine['date']=vaccine['date']
domain_pd = pd.to_datetime(["2013-01-01", "2022-12-31"]).astype(int) / 10 ** 6

selector = alt.selection_single(empty="all",fields=['ticker'])
scale = alt.Scale(
    domain=['PFE','JNJ','MRNA'],
    range=['#0093d0','#d71500','#00d03b'])
color = alt.Color("ticker:N", scale=scale)

base = alt.Chart(vaccine).properties(width=800,height=250).add_selection(selector)

lines = (
    base.mark_line()
    .encode(
        alt.X("date:T",title="Date"),
        alt.Y("price:Q",title="Adjusted Stock Price in USD ($)"),
        color = alt.condition(selector,color,alt.value("lightgray")),
        tooltip = [
            "ticker",
            alt.Tooltip("date:T", title="date"),
            alt.Tooltip("price:N", title="USD($)"),
            ],
        ).properties(width=800,height=300, title="Time-Series for Stock Price")
    ).interactive()


hist = (
    base.mark_bar(thickness=100).
    encode(
        alt.X("date:T",title="Date"),
        alt.Y("volume:Q",title="Trade Volume (Number of Stock)"),
        color=alt.Color('ticker:N',scale=scale),
        tooltip=[
            alt.Tooltip("date:T",title="date"),
            alt.Tooltip("volume:N",title="volume traded"),
            ],
        )
    .properties(height=200,title="Number of Stock Traded in a Given Day")
    .transform_filter(selector)
    )

fig = (lines&hist)

fig = (fig.properties(
    title={
        "text":['Stock Market Performances for Major Vaccine Production Companies'],
        "subtitle":["During 2013 to 2022"],
        }
    )
    .configure_axis(grid=False)
    .configure_title(fontSize=14,anchor="middle")
   )

fig.save("vaccine_viz.html")

###############################################################################

price_airline = pd.melt(price_vol, id_vars='date', value_vars=['AAL.Adjusted','DAL.Adjusted','UAL.Adjusted'])
volume_airline = pd.melt(price_vol, id_vars='date', value_vars=['AAL.Volume','DAL.Volume','UAL.Volume'])
airline = price_airline.merge(volume_airline,on='date',how="inner")
airline = airline.drop_duplicates(["date",'variable_x'])
airline[['ticker','b']] = airline.variable_x.str.split(".",expand=True)
airline = airline.drop(['variable_x','variable_y','b'],axis=1)
airline = airline.rename(columns={'value_x':'price','value_y':'volume'})

airline = airline[airline['ticker'].isin(['AAL','DAL','UAL'])]
airline['date']=airline['date']
domain_pd = pd.to_datetime(["2013-01-01", "2022-12-31"]).astype(int) / 10 ** 6

selector = alt.selection_single(empty="all",fields=['ticker'])
scale = alt.Scale(
    domain=['AAL','DAL','UAL'],
    range=['#0078d2','#9b1631','#9966cc'])
color = alt.Color("ticker:N", scale=scale)

base = alt.Chart(airline).properties(width=800,height=250).add_selection(selector)

lines = (
    base.mark_line()
    .encode(
        alt.X("date:T",title="Date"),
        alt.Y("price:Q",title="Adjusted Stock Price in USD ($)"),
        color = alt.condition(selector,color,alt.value("lightgray")),
        tooltip = [
            "ticker",
            alt.Tooltip("date:T", title="date"),
            alt.Tooltip("price:N", title="USD($)"),
            ],
        ).properties(width=800,height=300, title="Time-Series for Stock Price")
    ).interactive()


hist = (
    base.mark_bar(thickness=100).
    encode(
        alt.X("date:T",title="Date"),
        alt.Y("volume:Q",title="Trade Volume (Number of Stock)"),
        color=alt.Color('ticker:N',scale=scale),
        tooltip=[
            alt.Tooltip("date:T",title="date"),
            alt.Tooltip("volume:N",title="volume traded"),
            ],
        )
    .properties(height=200,title="Number of Stock Traded in a Given Day")
    .transform_filter(selector)
    )

fig = (lines&hist)

fig = (fig.properties(
    title={
        "text":['Stock Market Performances for Major Airline Companies'],
        "subtitle":["During 2013 to 2022"],
        }
    )
    .configure_axis(grid=False)
    .configure_title(fontSize=14,anchor="middle")
   )

fig.save("airline_viz.html")

###############################################################################

price_hotel = pd.melt(price_vol, id_vars='date', value_vars=['IHG.Adjusted','MAR.Adjusted','H.Adjusted','HLT.Adjusted'])
volume_hotel = pd.melt(price_vol, id_vars='date', value_vars=['IHG.Volume','MAR.Volume','H.Volume','HLT.Volume'])
hotel = price_hotel.merge(volume_hotel,on='date',how="inner")
hotel = hotel.drop_duplicates(["date",'variable_x'])
hotel[['ticker','b']] = hotel.variable_x.str.split(".",expand=True)
hotel = hotel.drop(['variable_x','variable_y','b'],axis=1)
hotel = hotel.rename(columns={'value_x':'price','value_y':'volume'})

hotel = hotel[hotel['ticker'].isin(['IHG','MAR','H','HLT'])]
hotel['date']=hotel['date']
domain_pd = pd.to_datetime(["2013-01-01", "2022-12-31"]).astype(int) / 10 ** 6

selector = alt.selection_single(empty="all",fields=['ticker'])
scale = alt.Scale(
    domain=['IHG','MAR','H','HLT'],
    range=['#d96932','#b41f3a','#58b1ce','#b09a61'])
color = alt.Color("ticker:N", scale=scale)

base = alt.Chart(hotel).properties(width=800,height=250).add_selection(selector)

lines = (
    base.mark_line()
    .encode(
        alt.X("date:T",title="Date"),
        alt.Y("price:Q",title="Adjusted Stock Price in USD ($)"),
        color = alt.condition(selector,color,alt.value("lightgray")),
        tooltip = [
            "ticker",
            alt.Tooltip("date:T", title="date"),
            alt.Tooltip("price:N", title="USD($)"),
            ],
        ).properties(width=800,height=300, title="Time-Series for Stock Price")
    ).interactive()


hist = (
    base.mark_bar(thickness=100).
    encode(
        alt.X("date:T",title="Date"),
        alt.Y("volume:Q",title="Trade Volume (Number of Stock)"),
        color=alt.Color('ticker:N',scale=scale),
        tooltip=[
            alt.Tooltip("date:T",title="date"),
            alt.Tooltip("volume:N",title="volume traded"),
            ],
        )
    .properties(height=200,title="Number of Stock Traded in a Given Day")
    .transform_filter(selector)
    )

fig = (lines&hist)

fig = (fig.properties(
    title={
        "text":['Stock Market Performances for Major Hotel Groups'],
        "subtitle":["During 2013 to 2022"],
        }
    )
    .configure_axis(grid=False)
    .configure_title(fontSize=14,anchor="middle")
   )

fig.save("hotel_viz.html")
