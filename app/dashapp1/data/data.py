import os
from datetime import datetime as dt

import pandas as pd

DATASETS = os.path.abspath(os.path.dirname(__file__))

class Data(object):
    def get_data(self,selected_dropdown_value):
        df=pd.read_csv(DATASETS+'/data.csv')
        COLUMNS = ['bathrooms', 'bedrooms', 'finishedsqft', 'lastsolddate', 'lastsoldprice', 'latitude', 'longitude',  'totalrooms', 'usecode', 'yearbuilt']
        print(df.dtypes)
        df['lastsolddate']=pd.to_datetime(df['lastsolddate'])
        return df[COLUMNS].sort_values(by='lastsolddate')

