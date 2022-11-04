import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import dash_table
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd
import twitter  # pip install python-twitter
from app import app, api
import nltk
from wordcloud import WordCloud

def f(row):
    return "[{0}]({0})".format(row["url"])

# layout of second (trends) tab ******************************************
perfiles_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Integrantes")
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='table-div', children="")
        ], width=6),
        # dbc.Col([
        #     html.Div(id='figure-div', children=''),
        # ], width=6),
    ], className="mt-3",),
    dcc.Interval(id='tabla', interval=1000*300, n_intervals=0)
])


# pull trending tweets and create the table ******************************
@app.callback(
    Output(component_id="table-div", component_property="children"),
    Input(component_id="tabla", component_property="n_intervals"),
)
def display_trend(tabla):
    cedulas,nombres,apellidos = ['Ced1','Ced2','Ced3'], ['Miguel','Daniel','Heimis'], ['Daza','Prasca','Miranda']
    
    d = {
        "Cedula": cedulas,
        "Nombres": nombres,
        "Apellidos": apellidos,
    }
    df = pd.DataFrame(d)
    
    return dash_table.DataTable(
        id='datatable-trends',
        columns=[
            {"name": i, "id": i}
            if i == "trending" or i == "volume"
            else {"name": i, "id": i, 'type': 'text', "presentation":"markdown"}
            for i in df.columns
        ],
        data=df.to_dict('records'),
        markdown_options=dict(html=True, link_target='_blank'),
        page_action='native',
        page_size=6,
        style_cell={
            'whiteSpace': 'normal',
            'height': 'auto',
            'overflow': 'hidden',
            'minWidth': '50px', 'width': '80px', 'maxWidth': '120px',
        },
    )
