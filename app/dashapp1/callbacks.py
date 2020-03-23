from datetime import datetime as dt

import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output
from app.dashapp1.data.data  import Data
import dash_table as dtb
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go



def register_callbacks(dashapp):

    ### MAIN MAP
    @dashapp.callback(
        
            Output('main-map', 'figure')
        ,
        [
            Input('selectCountry', 'value')
         ])
    def update_map( selectCountry="Netherlands"):
        t_0 = dt.now()
        d = Data()
        df = d.get_data_confirmed()

        colours=['#91221A']
        hover_data=['Count']
 
        fig = px.scatter_geo(df, lat="Lat", lon="Long", color_discrete_sequence=colours,
                            hover_name="Country", 
                            hover_data=hover_data,
                            size="Count",
                            animation_frame="DateSort",
                            opacity=0.7,
                            size_max=100,
                            projection=selectCountry) #'https://plot.ly/python-api-reference/generated/plotly.express.scatter_geo.html
        fig.update_geos(
            resolution=50,
            showcoastlines=True, coastlinecolor="#9c9c9b",
            showland=True, landcolor="#2a2a28",
            showocean=True, oceancolor="#030f19",
            showlakes=False, lakecolor="Blue",
            showrivers=False, rivercolor="Blue"
        
        )
        fig.update_layout(showlegend=False,  height=700, template='plotly_dark')

        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)

        return fig

    ### MAIN TABLE
    @dashapp.callback(
        [
            Output('main-table', 'columns'),
            Output('main-table', 'data')
        ],
        [
            Input('main-table', "page_current"),
            Input('main-table', "page_size"),

         ])
    def update_main_table(page_current, page_size):
        d   = Data()
        dfs=d.get_data_combined()
        dfs=dfs.sort_values(by=['CountConfirmed'], ascending=False).reset_index()
        
        columns = [{'name': i, 'id': i, 'deletable': True} for i in dfs.columns ]
        
        data = dfs.iloc[page_current*page_size:(page_current+ 1)*page_size].to_dict('records')


        return columns, data

    ### CONFIRMED BY COUNTRY
    @dashapp.callback(
        [
            Output('table-confirmed-cases', 'columns'),
            Output('table-confirmed-cases', 'data')
        ],
        [
            Input('table-confirmed-cases', "page_current"),
            Input('table-confirmed-cases', "page_size"),
            Input('table-confirmed-cases', 'sort_by'),

         ])
    def update_confirmed_cases(page_current, page_size, sort_by="Count"):
        d   = Data()
        df  = d.get_data_confirmed()[[ 'Country', 'Count', 'Date']]
        max_date=df['Date'].max()
        dfs = df[df.Date==max_date]
        
        dfs = dfs.groupby('Country')['Count'].sum().reset_index(name='Count')


        dfs = dfs.sort_values(by='Count',
            ascending=False,
            inplace=False
        )[['Count', 'Country']]

        columns = [{'name': i, 'id': i, 'deletable': True} for i in dfs.columns ]

        data = dfs.iloc[page_current*page_size:(page_current+ 1)*page_size].to_dict('records')

        return columns, data

    ### TOTAL CONFIRMED 
    @dashapp.callback(
        
            Output('total-confirmed-cases', 'children')
        ,
        [
            Input('selectCountry', 'value')
         ])
    def update_total_confirmed_cases( selectCountry="Netherlands"):
        t_0 = dt.now()
        
        d   = Data()
        df  = d.get_data_confirmed()[[ 'Country', 'Count', 'Date']]
        max_date=df['Date'].max()
        dfs = df[df.Date==max_date]
        total_cases = dfs['Count'].sum()

        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)

        return total_cases
  
    ### TOTAL DEATHS    
    @dashapp.callback(
        
            Output('total-deaths', 'children')
        ,
        [
            Input('selectCountry', 'value')
         ])
    def update_total_deaths( selectCountry="equirectangular"):
        t_0 = dt.now()
        
        d   = Data()
        df  = d.get_data_deaths()[[ 'Country', 'Count', 'Date']]
        max_date=df['Date'].max()
        dfs = df[df.Date==max_date]
        total_cases = dfs['Count'].sum()

        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)

        return total_cases

    ### TOTAL RECOVERED
    @dashapp.callback(
        
            Output('total-recovered', 'children')
        ,
        [
            Input('selectCountry', 'value')
         ])
    def update_total_recovered( selectCountry="Netherlands"):
        t_0 = dt.now()
        
        d   = Data()
        df  = d.get_data_recovered()[[ 'Country', 'Count', 'Date']]
        max_date=df['Date'].max()
        dfs = df[df.Date==max_date]
        total_cases = dfs['Count'].sum()

        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)

        return total_cases

    ### MAIN GRAPH
    @dashapp.callback(
        
            Output('main-graph', 'figure')
        ,
        [
            Input('selectCountry', 'value')
         ])
    def update_main_graph(selectCountry="Netherlands"):
        t_0 = dt.now()
        
        d   = Data()
        df  = d.get_data_combined(most_recent_only=False)
        print(df.columns)
        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)
        figure= go.Scatter(
            x=df['Date'],
            y=df['CountConfirmed'],
            text='CountConfirmed'
            )
        return figure

    
