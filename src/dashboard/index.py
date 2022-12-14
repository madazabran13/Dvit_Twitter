import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import twitter  # pip install python-twitter
from app import app, api
from app import  api
from mentions import mentions_layout
from perfiles import perfiles_layout
import statsmodels.api as sm

app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Dashboard", tab_id="tab-mentions", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                
            ],
            id="tabs",
            active_tab="tab-mentions",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([ 
    html.Div([
        # html.Hr(),
        html.H1('Dvit: Analisis de resultados en Twitter',
                style={"textAlign": "center",
                       'color': 'white',
                       'padding-top': '20px',
                       'margin-left': '2%', 
                       'display': 'inline-block'
                       }),
        html.Img(srcSet='https://bit.ly/3h8c3fY',
                 style={'position': 'relative',
                    'float': 'right',
                    'right': '-0.03px',
                    'height': '76px',
                    
                    }),
    ], style={"textAlign": "center",
                           'height':'80px',
                           'margin':'0px -80 10px',
                            'background-color':'#366A96',
                           'border-radius':'5px',
                           'display':'block',},),
   
    # html.Img(srcSet='https://bit.ly/3thM6O1',
    #          style={'width':'50%',}),
   
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

], style={'display':'block', 'flex-direction':'column'})

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)

def switch_tab(tab_chosen):
    if tab_chosen == "tab-mentions":
        return mentions_layout
    elif tab_chosen == "tab-perfiles":
        return perfiles_layout
    return html.P("Esto no deber??a mostrarse por ahora....")

if __name__=='__main__':
    app.run_server(debug=True)