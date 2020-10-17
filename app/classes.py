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
                    dbc.DropdownMenuItem("Dataset",      href="https://github.com/CSSEGISandData/COVID-19",external_link=True,),
                    dbc.DropdownMenuItem("Dashboard - CSSE",         href="https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6",external_link=True,),
                    dbc.DropdownMenuItem("Dashboard - Healthmap"   , href="https://www.healthmap.org/covid-19/",external_link=True,),   
                    dbc.DropdownMenuItem("Dashboard - PowerBI Community COVID-19 Dashboard"   , href="https://community.powerbi.com/t5/COVID-19-Data-Stories-Gallery/COVID-19-Dashboard-From-Data-to-Insights/td-p/995011",external_link=True,),   
                   
                   
                   
                   
                    ],
                nav=True,
                in_navbar=True,
                label="Menu",
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

        self.html= \
            dbc.Card(
                [
                    dbc.CardHeader(header
    
                    ),
                    dbc.CardBody(html.P(body, id="card-content-"+header, className="card-text")),
                ]
            )


class TabCard(object):
    def __init__(self, name, tabcards=None):

        self.html = \
            dbc.Card(
                    [
                        dbc.CardHeader(
                            dbc.Tabs(
                                [ dbc.Tab(dbc.CardBody(html.P(tabcard["tab_body"], id="card-content-"+tabcard["tab_label"], className="card-text")), label = tabcard["tab_label"], tab_id="tab-"+name+"-"+str(i) ) for i, tabcard in enumerate(tabcards) ],
                                id="card-tabs-"+name,
                                card=True,
                                active_tab="tab-"+name+"-0",
                            )
                        ),
                    ]
                )


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
        