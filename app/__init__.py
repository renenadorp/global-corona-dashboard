
import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

from config import BaseConfig
import os
import copy
import datetime as dt

import pandas as pd
import dash
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc 
import dash_table

import plotly.express as px


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):

    ### App1 = Story 1 #################################################
    from app.dashapp1.layout import layout
    from app.dashapp1.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp1 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/story1/',
                         assets_folder=get_root_path(__name__) + '/story1/assets/',
                         meta_tags=[meta_viewport],
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    with app.app_context():
        dashapp1.title = 'Medium Data Science Journey - Story 1'
        dashapp1.layout = layout
        register_callbacks(dashapp1)

    _protect_dashviews(dashapp1)


    ### App2 = Story 2 #################################################
    from app.dashapp2.layout import layout
    from app.dashapp2.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp2 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/story2/',
                         assets_folder=get_root_path(__name__) + '/story2/assets/',
                         meta_tags=[meta_viewport],
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    with app.app_context():
        dashapp2.title = 'Medium Data Science Journey - Story 2'
        dashapp2.layout = layout
        register_callbacks(dashapp2)

    _protect_dashviews(dashapp2)


def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)
