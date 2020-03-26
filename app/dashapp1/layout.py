
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dtb
import plotly.graph_objects as go
import os
from app.classes import Intro, Nav, Card, TabCard
from app.dashapp1.data.data  import Data
from app.dashapp1.colors import colors

### GLOBAL VARS & CONSTANTS ######################################

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
                ),
            html.Div([    
                html.Div(
                dcc.Dropdown(
                    id='selectDummyLeft',
                    options=[{'label': c, 'value': c} for c in [1]],
                )
                ,className="invisible"),              
            ])
        ])
card_confirmed_cases =Card(header="Confirmed Cases", title= "", text="Text", body=body_confirmed_cases)

### MAP ################################################
body_map = \
    html.Div([
            html.Div(dcc.Graph(id='main-map' , config={'displayModeBar': False}, 
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
                    id='selectDummyMiddleMap',
                    options=[{'label': c, 'value': c} for c in [1]],
                )
                ,className="invisible"),              
            ])
             
    ])  

body_table = \
    html.Div([
            dtb.DataTable(
                    id='main-table',
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
                ),
            html.Div([    
                html.Div(
                dcc.Dropdown(
                    id='selectDummyMainTable',
                    options=[{'label': c, 'value': c} for c in [1]],
                )
                ,className="invisible"),              
            ])
        ])

body_graph = \
    html.Div([
            html.Div([    
            html.Div(
                dcc.Dropdown(
                    id='selectCountry',
                    options=[{'label': c, 'value': c} for c in countries],
                    style={'background-color':colors.get('background', 'black'), 'color': colors.get('text_dropdown', 'grey')}
                )
                ,className="visible"),              
            ]),
            dcc.Graph(id='main-graph' , config={'displayModeBar': False}, 
            figure={
                    'layout':go.Layout(
                        template = 'plotly_dark',

                        height=700,

                        annotations=[
                                    go.layout.Annotation(
                                        text='Please wait....',
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
            )
        ], className=""
    )

tabcards_main = \
    [ 
        {"tab_label": "Map"         , "tab_body": body_map},
        {"tab_label": "Table"       , "tab_body": body_table},
        {"tab_label": "Graph"       , "tab_body": body_graph}
    ]

card_main =TabCard(name="CardMain",  tabcards=tabcards_main)

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
                html.Div([card_main.html]
                     
                ,className="col-8"), 
                
                
                ## RIGHT COLUMN
                html.Div([
                card_total_confirmed_cases.html,
                card_total_deaths.html,
                #card_total_recovered.html,
                ], className="col"),        
                
            ]
            , className="row"),   

        ]       
    ,className="container-fluid"),
    ]
    )



