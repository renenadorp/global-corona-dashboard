import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

class Nav(object):

    def __init__(self,label='Stories'):

        self.html= dbc.NavbarSimple(
        children=[
        #dbc.NavItem(dbc.NavLink("Stories", href="/story2/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Story 1 - Linear Regression", href="/story1",external_link=True,),
               
                dbc.DropdownMenuItem("Story 2", href="/story2",external_link=True,),
               
                dbc.DropdownMenuItem("Story 3", href="/story3",external_link=True,),
               
                
            ],
            nav=True,
            in_navbar=True,
            label=label,
        ),
    ],
    brand="My Machine Learning Journey",
    brand_href="/",
    color="light",
    dark=False,
    )

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
        html.P()
        ])

class Intro(object):

    def __init__(self):

        self.html= html.Div(
         dcc.Markdown(
            '''
            This page is part of the series "My Machine Learning Journey", published as stories on Medium:

            * Story 1 (this one): Regression Analysis
            * Story 2: TBD
            '''
            )
        )
        

 