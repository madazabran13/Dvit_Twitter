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



# app.layout = html.Div([    
#     html.Hr(),
#     html.Div([
#         html.H1('Dvit: Analisis de resultados en Twiter',style={"textAlign": "center"}),
#         html.Img(srcSet='https://bit.ly/3thM6O1',
#             ),
#     ], className= 'banner'),
    
#     html.Hr(),
# ], id='content', style={'display':'flex', 'flex-direction':'column'})



app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Dashboard", tab_id="tab-mentions", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Perfiles", tab_id="tab-perfiles", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ],
            id="tabs",
            active_tab="tab-mentions",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([ 
    
    
    # dbc.Row(dbc.Col(html.H1("Dvit: Analisis de resultados en Twiter",
    #                         style={"textAlign": "center"}), width=12),
    #         ),
    
    # style = {"textAlign": "center",'height':'75px','margin':'0px -10px 10px''background-color':'#5a6ac5','border-radius':'2px','display':'block'}
    html.Div([
        # html.Hr(),
        html.H1('Dvit: Analisis de resultados en Twiter',
                style={"textAlign": "center",
                       'color': '0966cf',
                       'padding-top': '20px',
                       'margin-left': '2%', 
                       'display': 'inline-block'
                       }),
        html.Img(srcSet='https://bit.ly/3E2QDdl',
                 style={'position': 'relative',
                    'float': 'right',
                    'right': '30px',
                    'height': '75px',
                    
                    }),
    ], style={"textAlign": "center",
                           'height':'70px',
                           'margin':'0px -80 10px',
                        #    'background-color':'#50759e',
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
    return html.P("Esto no debería mostrarse por ahora....")

if __name__=='__main__':
    app.run_server(debug=True)