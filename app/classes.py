import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Nav(object):

    def __init__(self,label='='):

        self.html= html.Div([
        dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("CSSE",         href="https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6",external_link=True,),
                    dbc.DropdownMenuItem("Healthmap"   , href="https://www.healthmap.org/covid-19/",external_link=True,),                
                    ],
                nav=True,
                in_navbar=True,
                label="Other Corona Dashboards",
            ),           
            ],
    brand="Global Corona Dashboard",
    brand_href="/",
    brand_external_link=True,
    color="dark",
    dark=True,
    # fixed="top"
    ),
    html.Div(style={'margin-top':'5px'})  
    
  ], className="w-screen")

class Card(object):

    def __init__(self,header, title, text, body):

        self.html= html.Div([html.Div(
        [
            html.A(id=header),
            html.H5(header,    className="card-header "),
            html.Div([
                html.H5(title, className="card-title"),
                html.P(body,   className="card-text"),
            ],
            className="card-body"
            )
        ],className="card "),
        html.P()
        ])

class Intro(object):

    def __init__(self):
        CONTENTFILE = BASEDIR+'/intro.md'

        f = open(CONTENTFILE)
        content = f.read()
        f.close()

        self.html= html.Div(
        [   html.P(),
            dcc.Markdown(
            content
            )
        ]
        
        )
        