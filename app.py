import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 65000)
DEBUG = os.getenv("DEBUG", True)


app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server
