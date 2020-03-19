
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dtb
import os
from app.classes import Intro, Nav, Card


### GLOBAL VARS & CONSTANTS ######################################
CONTENTDIR = os.path.abspath(os.path.dirname(__file__))+'/content'

PAGE_SIZE = 20
cards=[]

### NAVBAR ################################################
nav = Nav().html

### INTRODUCTION ###########################################
intro = Intro().html

### SECTION 01 - STORY INTRODUCTION ###########################################
cards.append( Card(header="Story Introduction", title="", text="Linear Regression", body=html.Div([
    html.P('''
          This story covers Linear Regression.
          '''
        ),  
])))

### SECTION 02 - BUSINESS UNDERSTANDING ###########################################
cards.append(Card(header="Business Understanding", title="", text="Text", 
    body=html.Div([
    html.P('''
        The purpose of the model is to predict resident house prices based on a number of attributes 
        (e.g. location, number of rooms, year of construction) using Linear Regression.
        '''
        )
])))

### SECTION 03 - DATA UNDERSTANDING ###########################################
CONTENTFILE = '/section_003/paragraph_001.md'

f = open(CONTENTDIR+CONTENTFILE)
content = f.read()
f.close()


body = html.Div([
    html.H3('Dataset'),
    dcc.Markdown(content),
    html.H3('Graphs'),
    html.Div([    
        html.Div(
        dcc.Dropdown(
            id='selectYearStart',
            options=[{'label': y, 'value': y} for y in range(2000,2020)],
            value='2001'
            ), className="col-sm"),
        html.Div(
            dcc.Dropdown(
                id='selectYearEnd',
                options=[{'label': y, 'value': y} for y in range(2000,2020)],
                value='2015'
            ), className="col-sm"),
        
        ], className="row"),
    html.Div(
        html.Div([
        dcc.Graph(id='my-graph-2'),
            
        ], className="col-lg")
            , className="row"),   
    html.Div([
           dcc.Graph( id='scatter-map',),  ]),

    html.H3('Raw Data'),
    html.Div([
            dtb.DataTable(
                    id='table-raw',
                    page_current=0,
                    page_size=PAGE_SIZE,
                    page_action='custom',
                    sort_action='custom',
                    sort_mode='single',
                    sort_by=[]
                )
        ]),
    html.H3('Statistics'),

    html.Div([
            dtb.DataTable(
                    id='table-stats',
                    page_current=0,
                    page_size=PAGE_SIZE,
                    page_action='custom',
                    sort_action='custom',
                    sort_mode='single',
                    sort_by=[]
                )
        ]),

])


cards.append(Card(header="Data Understanding", 
    title= "",    
    text="Text", 
    body=body))

### DATA PREPARATION ###########################################
cards.append(Card(header="Data Preparation", title= "", text="Text", body=html.Div([
    html.H2('Data Preparation')
])))

### MODELING ##################################################
cards.append(Card(header="Modeling", title= "", text="Text", body=html.Div([
    html.H2(' Modeling')
])))

### EVALUATION ###########################################
cards.append(Card(header="Evaluation", 
    title= "", 
    text="Text", 
    body=html.Div([
    html.H2('Evaluation')
])))


### DEPLOYMENT ###########################################
cards.append(Card(header="Deployment", 
    title= "", 
    text="Text", 
    body=html.Div([
    html.H2('Deployment')
])))


### CONCLUSION ###########################################
cards.append(Card(header="Conclusion", 
    title= "", 
    text="Text", 
    body=html.Div([
    html.H2('Conclusion')
])))



content = [ card.html for card in cards ] 

layout = html.Div([
    html.Div(nav,className="w-screen mt-0"),
    html.Div(intro,className="container-fluid"),
    html.Div(content,className="container-fluid"),


])

