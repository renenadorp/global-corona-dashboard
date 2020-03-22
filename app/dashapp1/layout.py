
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dtb
import os
from app.classes import Intro, Nav, Card
from app.dashapp1.data.data  import Data
import plotly.graph_objects as go

### GLOBAL VARS & CONSTANTS ######################################
colors = {
    'background'        : '#222222',
    'ocean'             : '#222222',
    'land'              : '#222222',
    'text'              : '#7FDBFF',
    'marker_confirmed'  : '#91221A',
    'text_confirmed'    : '#d42c1f',
    'text_recovered'    : '#67c94d',
    'text_active'       : '#f09135',
    'text_deaths'       : '#fffff'
}

PAGE_SIZE = 20

d=Data()
countries=d.get_countries()

### NAVBAR ###################################################
nav = Nav().html

### TOTAL CASES BY COUNTRY #################################
body_total_confirmed_cases = \
       html.Div(
                [
                    html.H1('..',
                        id="total-confirmed-cases",
                        style={
                            'textAlign': 'center',
                            'color': colors['text_confirmed']
                        }
                    )
                ]         )
card_total_confirmed_cases =Card(header="Total Confirmed Cases", title= "", text="Text", body=body_total_confirmed_cases)

### CONFIRMED CASES BY COUNTRY #################################
body_confirmed_cases = \
    html.Div([
            dtb.DataTable(
                    id='table-confirmed-cases',
                    page_current=0,
                    page_size=PAGE_SIZE,
                    page_action='custom',
                    sort_action='custom',
                    sort_mode='single',
                    sort_by=[],
                    style_header={'backgroundColor': colors['background']},
                    style_cell={
                        'backgroundColor': colors['background'],
                        'color': '#d6d6d6',
                        'font-size':15,
                        'border': '0px',
                        'maxWidth':0,
                        'textOverflow': 'ellipsis'
                    },
                    style_data_conditional=[{
                        'if': {'column_id': 'Count'},
                        'backgroundColor': colors['background'],
                        'font-weight':'bold',
                        'font-size':20,

                        'color': colors['text_confirmed'],
                        },
                        {
                        'if': {
                            'column_id': 'Country',
                            'filter_query': '{Country} = "Netherlands"'
                        },
                        
                        'color': colors['text_confirmed'],
                        'font-weight': 'bold',
                         }
                        ]
                )
        ])
card_confirmed_cases =Card(header="Confirmed Cases", title= "", text="Text", body=body_confirmed_cases)

### GOBAL SPREAD ################################################
#projections = ['equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff',  'sinusoidal']
body_globe = html.Div([

                html.Div(dcc.Graph(id='bubble-map' , config={'displayModeBar': False}, 
                figure={
                        'layout':go.Layout(
                            template = 'plotly_dark',

                            height=700,

                            annotations=[
                                        go.layout.Annotation(
                                            text='Please wait for the map to load',
                                            align='center',
                                            showarrow=False,
                                            xref='paper',
                                            yref='paper',
                                            x=0.5,
                                            y=0.5,
                                            bordercolor='black',
                                            borderwidth=0
                                        )
                                    ]

                    )
			        }
                )),  
                html.Div([    
                html.Div(
                    dcc.Dropdown(
                        id='selectCountry',
                        options=[{'label': c, 'value': c} for c in countries],
                    )
                    ,className="invisible"),              
                ]), 
        ])  
card_globe =Card(header="Global Spread", title= "", text="Text", body=body_globe)

### TOTAL DEATHS #############################################
body_total_deaths = \
       html.Div(
                [
                    html.H1('..',
                        id="total-deaths",
                        style={
                            'textAlign': 'center',
                            'color': colors['text_deaths']
                        }
                    )
                ]         )
card_total_deaths =Card(header="Total Deaths", title= "", text="Text", body=body_total_deaths)


## TOTAL RECOVERED #############################################
body_total_recovered = \
       html.Div(
                [
                    html.H1('..',
                        id="total-recovered",
                        style={
                            'textAlign': 'center',
                            'color': colors['text_recovered']
                        }
                    )
                ]         )
card_total_recovered =Card(header="Total Recovered", title= "", text="Text", body=body_total_recovered)

### PAGE LAYOUT #############################################
layout = html.Div([
    html.Div(nav
    ,className="w-screen mt-0"),
    html.Div([

        html.Div(
            [
                ## LEFT COLUMN
                html.Div([
                    html.Div(card_confirmed_cases.html)
                    ], 
                className="col"),        
                
                # MIDDLE COLUMN
                html.Div(
                    card_globe.html 
                ,className="col-8"),

                ## RIGHT COLUMN
                html.Div([
                card_total_confirmed_cases.html,
                card_total_deaths.html,
                card_total_recovered.html,
                ], className="col"),        
                
            ]
            , className="row"),   

        ]       
    ,className="container-fluid"),
    ]
    )



