
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dtb
from app.classes import Intro, Nav, Card


### GLOBAL VARS & CONSTANTS ######################################
PAGE_SIZE = 20
cards=[]

### NAVBAR ################################################
nav = Nav().html

### INTRODUCTION ###########################################
intro = Intro().html

### STORY INTRODUCTION ###########################################
cards.append( Card(header="Story Introduction", title="", text="Linear Regression", body=html.Div([
    html.P('''
          This story covers Linear Regression.
          '''
        ),  
])))

### BUSINESS UNDERSTANDING ###########################################
cards.append(Card(header="Business Understanding", title="", text="Text", 
    body=html.Div([
    html.P('''
        The purpose of the model is to predict resident house prices based on a number of attributes 
        (e.g. location, number of rooms, year of construction) using Linear Regression.
        '''
        )
])))

### DATA UNDERSTANDING ###########################################
body = html.Div([
    html.H3('Dataset'),
    dcc.Markdown(
    '''
    The data used for this notebook is taken from the GitHub repository of Rui Chang, 
    and can be found [here](https://raw.githubusercontent.com/RuiChang123/Regression_for_house_price_estimation/master/final_data.csv).
    The article on Medium by Rui Chang using this dataset (also applying linear regression) can be found [here](https://towardsdatascience.com/linear-regression-in-python-predict-the-bay-areas-home-price-5c91c8378878)

    The dataset contains the following information about houses sold in San Francisco:
    * address
    * info
    * z_address
    * bathrooms
    * bedrooms
    * finishedsqft
    * lastsolddate
    * lastsoldprice
    * latitude
    * longitude
    * neighborhood
    * totalrooms
    * usecode
    * yearbuilt
    * zestimate
    * zindexvalue
    * zipcode
    * zpid
    '''),
    html.H3('Graph'),
    html.Div([    
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Randstad', 'value': 'RAND.AS'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    html.Div([
        dcc.Graph(id='my-graph-2'),
        
    ])
    ]),
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
        ])
])
cards.append(Card(header="Data Understanding", 
    title= "",    
    text="Text", 
    body=body))

### DATA PREPARATION ###########################################
cards.append(Card(header="Data Preparation", title= "", text="Text", body=html.Div([
    html.H2('Data Preparation')
])))

### MODELING ###########################################
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
    html.H2('Conclustion')
])))



page = [nav]+[intro]+[ card.html for card in cards ] 

layout = html.Div(page, className="container-fluid")

