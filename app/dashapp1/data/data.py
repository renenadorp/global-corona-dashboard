import os
import datetime as dt

import pandas as pd

DATASETS = os.path.abspath(os.path.dirname(__file__))

class Data(object):
    def get_data_confirmed(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountConfirmed", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountConfirmed"]

        return df_pivot

    def get_data_deaths(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountDeaths", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountDeaths"]

        return df_pivot

    def get_data_recovered(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountRecovered", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountRecovered"]

        return df_pivot

    def get_countries(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
        countries=df['Country/Region'].unique()
        return countries

