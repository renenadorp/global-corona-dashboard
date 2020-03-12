import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 

class Nav(object):

    def __init__(self,label='Stories'):

        self.html= html.Div([
        dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Intro", href="#Introduction", external_link=True)),
            dbc.NavItem(dbc.NavLink("Business", href="#Business Understanding", external_link=True)),
            dbc.NavItem(dbc.NavLink("Data", href="#Data Understanding", external_link=True)),
            dbc.NavItem(dbc.NavLink("Prep", href="#Data Preparation", external_link=True)),
            dbc.NavItem(dbc.NavLink("Model", href="#Modeling", external_link=True)),
            dbc.NavItem(dbc.NavLink("Eval", href="#Evaluation", external_link=True)),
            dbc.NavItem(dbc.NavLink("Deploy", href="#Deployment", external_link=True)),
            dbc.NavItem(dbc.NavLink("Conclusion", href="#Conclusion", external_link=True)),
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
    brand="Machine Learning: A Journey",
    brand_href="/",
    brand_external_link=True,
    color="dark",
    dark=True,
    fixed="top"
    )  
    ,
  ])

class Card(object):

    def __init__(self,header, title, text, body):

        self.html= html.Div([html.Div(
        [
            html.A(id=header),
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
        [
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            dcc.Markdown(
            '''
            This page is part of the series "Machine Learning: A Journey", published as stories on Medium:

            * Story 1 (this one): Regression Analysis
            * Story 2: TBD
            '''
            )
        ]
        
        )
        