from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output
from app.dashapp1.data.data  import Data
import dash_table as dtb
import plotly.graph_objs as go



def register_callbacks(dashapp):


    @dashapp.callback(Output('my-graph-2', 'figure'), [Input('selectYearStart', 'value'), Input('selectYearEnd', 'value')])
    def update_graph_2(selectYearStart, selectYearEnd):
        d = Data()
        df = d.get_raw(selectYearStart, selectYearEnd)

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
            Input('table-raw'      , "page_current"),
            Input('table-raw'      , "page_size"),
            Input('table-raw'      , 'sort_by'),
            Input('selectYearStart', 'value'),
            Input('selectYearEnd'  , 'value')
         ])

    def update_raw(page_current, page_size, sort_by, selectYearStart, selectYearEnd):
        d = Data()
        df = d.get_raw(selectYearStart, selectYearEnd)
        
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
            Input('selectYearStart', 'value')
         ])

    def update_stats(selection=None):

        d = Data()
        df = d.get_raw()
        
        df_stats = d.get_stats(df)
        
        columns = [{'name': i, 'id': i, 'deletable': True} for i in df_stats.columns ]

        data = df_stats.to_dict('records')
       

        return columns, data


    @dashapp.callback(
        
            Output('scatter-map', 'figure')
        ,
        [
            Input('selectYearStart', 'value'),
            Input('selectYearEnd'  , 'value')
         ])

    def update_scatter_map( selectYearStart, selectYearEnd):
        d = Data()
        df = d.get_raw(selectYearStart, selectYearEnd)[['latitude', 'longitude']]
        
        #columns = [{'name': i, 'id': i, 'deletable': True} for i in sorted(df.columns) ]

        trace = go.Scatter(y = df['latitude'], x = df['longitude'],
                    name = 'Location',
                    mode='markers')
        layout = go.Layout(title     = '',
                           hovermode = 'closest')
        figure = go.Figure(data = [trace], layout=layout)

        return figure


