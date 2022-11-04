import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import twitter  # pip install python-twitter
from app import app, api
from app import  api
from mentions import mentions_layout



# our app's Tabs *********************************************************
app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Menciones", tab_id="tab-mentions", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ],
            id="tabs",
            active_tab="tab-mentions",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([ 
    html.Hr(),
    dbc.Row(dbc.Col(html.H1("Dvit: Analisis de resultados en Twiter",
                            style={"textAlign": "center"}), width=12),
            ),
    html.Hr(),
    html.Div([
        html.Img(src='assets/logo.png')
    ],),
   
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

])

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)

def switch_tab(tab_chosen):
    if tab_chosen == "tab-mentions":
        return mentions_layout
    return html.P("Esto no debería mostrarse por ahora....")

if __name__=='__main__':
    app.run_server(debug=True)