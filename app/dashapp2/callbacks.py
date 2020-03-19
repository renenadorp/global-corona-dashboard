from datetime import datetime as dt

import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output
from app.dashapp2.data.data  import Data
import dash_table as dtb
import plotly.express as px


def register_callbacks(dashapp):



    @dashapp.callback(
        
            Output('bubble-map', 'figure')
        ,
        [
            Input('selectRegion', 'value')
         ])

    def update_map( region=None):
        d = Data()
        df = d.get_data()
        
 
        fig = px.scatter_geo(df, lat="Lat", lon="Long", color="Country/Region",
                            hover_name="Province/State", size="CountConfirmed",
                            animation_frame="DateSort",
                        
                            projection="equirectangular") #'https://plot.ly/python-api-reference/generated/plotly.express.scatter_geo.html
        print('FIGURE CREATED')
        return fig.update_layout(showlegend=False)




    