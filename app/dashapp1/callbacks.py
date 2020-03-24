from datetime import datetime as dt
import pandas as pd

#Dash
from dash.dependencies import Input
from dash.dependencies import Output
import dash_table as dtb

#Plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

#App
from app.dashapp1.data.data  import Data
from app.dashapp1.colors import colors


def register_callbacks(dashapp):

    ### MAIN MAP
    @dashapp.callback(
        
            Output('main-map', 'figure')
        ,
        [
            Input('selectDummyMiddleMap', 'value')
         ])
    def update_map( selectDummyMiddleMap=1):
        t_0 = dt.now()
        d = Data()
        df = d.get_data_confirmed()

        colours=['#91221A']
        hover_data=['Count']
 
        fig = px.scatter_geo(df, 
                            lat="Lat", 
                            lon="Long", 
                            color_discrete_sequence=colours,
                            hover_name="Country", 
                            hover_data=hover_data,
                            size="Count",
                            animation_frame="DateSort",
                            opacity=0.7,
                            size_max=100, #Max size for bubble. Other bubble sizes are derived from this
                            projection="equirectangular") #'https://plot.ly/python-api-reference/generated/plotly.express.scatter_geo.html
        fig.update_geos(
            resolution=110, #50 or 110
            showcoastlines=True,    coastlinecolor=colors.get('coastline','white'),
            showland=True,          landcolor=colors.get('land', 'black'),
            showocean=True,         oceancolor=colors.get('ocean','blue'),
            showlakes=False,        lakecolor=colors.get('lake','blue'),
            showrivers=False,       rivercolor=colors.get('river','blue'),
        
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
        dfs=dfs.sort_values(by=['CountConfirmed'], ascending=False)
        
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
    def update_total_confirmed_cases( selectCountry="Italy"):
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
    def update_total_deaths( selectCountry="Italy"):
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
    def update_total_recovered( selectCountry="Italy"):
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
    def update_main_graph(selectCountry="Italy"):
        if selectCountry==None: selectCountry="Italy"
        t_0 = dt.now()
        
        d   = Data()
        df  = d.get_data_combined(most_recent_only=False)
    
        t_1 = dt.now()

        print('Elapsed time: ' , t_1 - t_0)
        fig = go.Figure()
        scatter_confirmed=go.Scatter(
            x=df[(df['Country']==selectCountry)]['Date'],
            y=df[(df['Country']==selectCountry)]['CountConfirmed'],
            name='CountConfirmed',
            line=dict(color=colors.get('marker_confirmed'), width=1),
            mode='lines',
            text='CountConfirmed',
            connectgaps=True
            )
        
        scatter_deaths=go.Scatter(
            x=df[(df['Country']==selectCountry)]['Date'],
            y=df[(df['Country']==selectCountry)]['CountDeaths'],
            name='CountDeaths',
            line=dict(color=colors.get('marker_deaths'), width=1),
            mode='lines',
            text='CountDeaths',
            connectgaps=True,
            )
        
        scatter_recovered=go.Scatter(
            x=df[(df['Country']==selectCountry)]['Date'],
            y=df[(df['Country']==selectCountry)]['CountRecovered'],
            name='CountRecovered',
            line=dict(color=colors.get('marker_recovered'), width=1),
            mode='lines',
            text='CountRecovered',
            connectgaps=True
            )
        
        fig.add_trace(scatter_confirmed)
        fig.add_trace(scatter_deaths)
        fig.add_trace(scatter_recovered)
        fig.update_layout(title=selectCountry, showlegend=True,  height=700, template='plotly_dark')



        return fig

    
