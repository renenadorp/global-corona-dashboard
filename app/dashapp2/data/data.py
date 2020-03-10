from datetime import datetime as dt

import pandas as pd
import pandas_datareader as pdr

class Data(object):
    def get_data(self,selected_dropdown_value):
        #print('STORY 2')
        return pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())

