
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import dash_table as dtb

class Card(object):

    def __init__(self,header, title, text, body):

        self.html= html.Div([html.Div(
        [
            html.H5(header, className="card-header "),
            html.Div([
                html.H5(title, className="card-title"),
                html.P(body,className="card-text"),
            ],
            className="card-body"
            )
        ],className="card "),
        html.P()])


### GLOBAL VARS & CONSTANTS ######################################
PAGE_SIZE = 10
cards=[]
### NAVBAR ################################################

page_nav = dbc.NavbarSimple(
    children=[
        # dbc.NavItem(dbc.NavLink("Stories", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Story 1", header=True),
                dbc.DropdownMenuItem("Story 2", href="#"),
                dbc.DropdownMenuItem("Story 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Stories",
        ),
    ],
    brand="My Data Science Journey",
    brand_href="#",
    color="secondary",
    dark=True,
)

### TITLE ################################################

page_title = html.H1('Story 1 - Regression Analysis')

### INTRODUCTION ###########################################
cards.append( Card(header="Introduction", title="", text="Text", body=html.Div([
    html.P('''
        This page is part of the series "My Data Science Journey", published as stories on Medium:
        - Story 1 (this one): Regression Analysis
        - Story 2: TBD

        '''
        ),  
])))

### BUSINESS UNDERSTANDING ###########################################
cards.append(Card(header="Business Understanding", title="", text="Text", 
    body=html.Div([
    html.P('''
        The purpose of this notebook is to predict resident house prices based on a number of attributes 
        (e.g. location, number of rooms, year of construction) using Linear Regression.
        '''
        )
])))

### DATA UNDERSTANDING ###########################################
body = html.Div([
    html.H2('Dataset'),
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
    html.H2('Graph'),
    html.Div([    
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    html.Div([
        dcc.Graph(id='my-graph-2'),
        
    ])
    ]),
    html.H2('Table'),

    html.Div([
            dtb.DataTable(
                    id='datatable',
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

### DATA MODELING ###########################################
cards.append(Card(header="Modeling", title= "", text="Text", body=html.Div([
    html.H2('Data Modeling')
])))

### EVALUATION ###########################################
cards.append(Card(header="Evaluation", 
    title= "", 
    text="Text", 
    body=html.Div([
    html.H2('Evaluation')
])))



page_footer = html.Div('Footer')

page = [page_nav] + [page_title] + [ card.html for card in cards ] + [page_footer]

layout = html.Div(page, className="container")

