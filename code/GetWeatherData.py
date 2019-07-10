# GetWeatherData.py
#
# script for automating the process of acquiring daily summary weather data
# from NOAA
#
# Matthew Garton - July 10, 2019

import requests
from datetime import datetime
import pandas as pd

# base url for NCEI-NOAA API
base_url = 'https://www.ncei.noaa.gov/access/services/data/v1'

# get today's date
today = datetime.today().strftime('%Y-%m-%d')

# set up request for API
req = requests.get(
    base_url,
    params={
        "dataset": "daily-summaries",
        "stations": "USC00144559", # Lawrence, Kansas
        "startDate": "1970-01-01", # Start Jan 1, 1970 (arbitrary decision for now)
        "endDate": today, # always pull data up to today
        "dataTypes": "PRCP,SNOW,SNWD,TMAX,TMIN", 
        # PRCP (tenths of mm), SNOW and SNWD (mm), TMAX/MIN (tenths of C)
        "format": "json",
    }
)

# make a pandas df out of the data
df = pd.DataFrame(req.json())

# format the dataframe
df.rename(columns={'DATE':'Date'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# convert all measurement columns to numeric type, keeping NaNs
for col in ['PRCP','SNOW','SNWD','TMAX','TMIN']:
    try:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    except:
        pass

# export to csv in data folder
df.to_csv(f'../data/kansas_daily_asof_{today}')