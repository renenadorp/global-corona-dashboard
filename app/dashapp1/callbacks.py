from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output
from app.dashapp1.data.data  import Data
import dash_table as dtb


def register_callbacks(dashapp):
    
    # @dashapp.callback(Output('my-graph-1', 'figure'), [Input('my-dropdown', 'value')])
    # def update_graph_1(selected_dropdown_value):
    #     df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
    #     return {
    #         'data': [{
    #             'x': df.index,
    #             'y': df.Close
    #         }],
    #         'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    #     }

    @dashapp.callback(Output('my-graph-2', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph_2(selected_dropdown_value):
        d = Data()
        df = d.get_data(selected_dropdown_value)

        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }

    @dashapp.callback(
        [
            Output('datatable', 'columns'),
            Output('datatable', 'data')
        ],
        [
            Input('datatable', "page_current"),
            Input('datatable', "page_size"),
            Input('datatable', 'sort_by'),
            Input('my-dropdown', 'value')
         ])

    def update_table(page_current, page_size, sort_by, selected_dropdown_value):
        d = Data()
        df = d.get_data(selected_dropdown_value)
        
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