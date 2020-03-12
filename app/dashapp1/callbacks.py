from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output
from app.dashapp1.data.data  import Data
import dash_table as dtb


def register_callbacks(dashapp):


    @dashapp.callback(Output('my-graph-2', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph_2(selected_dropdown_value):
        d = Data()
        df = d.get_raw(selected_dropdown_value)

        return {
            'data': [{
                'x': df.lastsolddate,
                'y': df.lastsoldprice,
                'type':'bar'
            }],
            'layout': {'margin': {'l': 0, 'r': 100, 't': 0, 'b': 100}}
        }

    @dashapp.callback(
        [
            Output('table-raw', 'columns'),
            Output('table-raw', 'data')
        ],
        [
            Input('table-raw', "page_current"),
            Input('table-raw', "page_size"),
            Input('table-raw', 'sort_by'),
            Input('my-dropdown', 'value')
         ])

    def update_raw(page_current, page_size, sort_by, selected_dropdown_value):
        d = Data()
        df = d.get_raw(selected_dropdown_value)
        
        if len(sort_by):
            dfs = df.sort_values(
                sort_by[0]['column_id'],
                ascending=sort_by[0]['direction'] == 'asc',
                inplace=False
            )
        else: # No sort 
            dfs = df

        columns = [{'name': i, 'id': i, 'deletable': True} for i in sorted(dfs.columns) ]

        data = dfs.iloc[page_current*page_size:(page_current+ 1)*page_size].to_dict('records')

        return columns, data


    @dashapp.callback(
        [
            Output('table-stats', 'columns'),
            Output('table-stats', 'data')
        ],
        [
            Input('my-dropdown', 'value')
         ])

    def update_stats(selection=None):
        d = Data()
        df = d.get_raw()
        
        df_stats = d.get_stats(df)
        
        columns = [{'name': i, 'id': i, 'deletable': True} for i in df_stats.columns ]

        data = df_stats.to_dict('records')
       

        return columns, data