
import os
import datetime as dt
import numpy as np
import pandas as pd

pd.options.display.max_rows = 99999999

class Data(object):
    def get_data_confirmed(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountConfirmed", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        
        df_pivot['State'] = np.where(df_pivot['State'].isna(), df_pivot['Country'], df_pivot['State'])
        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountConfirmed"]
        df_pivot['CountConfirmedPrevious'] = (df_pivot.sort_values(by=['Country', 'State', 'Date'], ascending=True)
                       .groupby(['Country', 'State'])['CountConfirmed'].shift(1))
        df_pivot['CountConfirmedIncrease'] = df_pivot['CountConfirmed']-df_pivot['CountConfirmedPrevious']

        return df_pivot.reset_index().fillna(0)[df_pivot['Count']>=0]

    def get_data_deaths(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountDeaths", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        df_pivot['State'] = np.where(df_pivot['State'].isna(), df_pivot['Country'], df_pivot['State'])

        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountDeaths"]
        df_pivot['CountDeathsPrevious'] = (df_pivot.sort_values(by=['Country', 'State', 'Date'], ascending=True)
                       .groupby(['Country', 'State'])['CountDeaths'].shift(1))
        df_pivot['CountDeathsIncrease'] = df_pivot['CountDeaths']-df_pivot['CountDeathsPrevious']
        return df_pivot.reset_index().fillna(0)[df_pivot['Count']>=0]

    def get_data_recovered(self):
       
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
        dates = [c for c in df.columns if '20' in c]
        df_pivot=pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates)
        df_pivot.rename(columns={"variable": "Date", "value": "CountRecovered", "Country/Region":"Country", "Province/State":"State"}, inplace=True)
        df_pivot['State'] = np.where(df_pivot['State'].isna(), df_pivot['Country'], df_pivot['State'])

        df_pivot[['Month','Day', 'Year']] =df_pivot.Date.str.split(pat = "/", expand=True)
        df_pivot['Year'] = '20' + df_pivot['Year'].astype(str)
        df_pivot['DateSort'] = df_pivot['Date']
        df_pivot['Date'] = pd.to_datetime(df_pivot[['Year', 'Month' , 'Day']])
        df_pivot['Count'] = df_pivot["CountRecovered"]
        return df_pivot.fillna(0)[df_pivot['Count']>=0]

    def get_data_combined(self, most_recent_only=True):
        df_confirmed  = self.get_data_confirmed()[['Country', 'State', 'Date', 'CountConfirmed', 'CountConfirmedIncrease']]
        df_deaths     = self.get_data_deaths()[['Country', 'State', 'Date', 'CountDeaths', 'CountDeathsIncrease']]
        #df_recovered  = self.get_data_recovered()[['Country', 'State', 'Date', 'CountRecovered']]

        if most_recent_only:
            
            max_date_confirmed=df_confirmed['Date'].max()

            #Select most recent date
            df_confirmed = df_confirmed[df_confirmed.Date==max_date_confirmed]
            df_deaths    = df_deaths[df_deaths.Date==max_date_confirmed]
            #df_recovered = df_recovered[df_recovered.Date==max_date_confirmed]

        #Concatenate datasets: confirmed, deaths, recovered
        dfc= pd.concat([df_confirmed.set_index(['Date','Country','State'], inplace=False), 
                        df_deaths.set_index(['Date','Country','State'], inplace=False), 
                        #df_recovered.set_index(['Date','Country','State'], inplace=False)
                        ], 
                        axis=1)
        dfc = dfc.groupby(['Date','Country']).sum()
        dfc['MortalityRate']= (((dfc['CountDeaths']/dfc['CountConfirmed'])*100)).round(3)

        return dfc.reset_index().fillna(0)

    def get_countries(self):   
        df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        countries=sorted(df['Country/Region'].unique())
        return countries
