import os
import datetime as dt

import pandas as pd

DATASETS = os.path.abspath(os.path.dirname(__file__))

class Data(object):
    def get_raw(self,selectYearStart=1900, selectYearEnd=2200):
        df=pd.read_csv(DATASETS+'/data.csv')
        COLUMNS = ['bathrooms', 'bedrooms', 'finishedsqft', 'lastsolddate', 'lastsoldprice', 'latitude', 'longitude',  'totalrooms', 'usecode', 'yearbuilt']
        #print(df.dtypes)
        df['lastsolddate']=pd.to_datetime(df['lastsolddate'])
        filterDateStart = dt.datetime(int(selectYearStart), 1, 1)
        filterDateEnd   = dt.datetime(int(selectYearEnd), 1, 1)
        return df[COLUMNS].loc[(df.lastsolddate >= filterDateStart) & (df.lastsolddate <= filterDateEnd)].sort_values(by='lastsolddate')


    def get_stats(self, df):
        return df.describe().reset_index()

