import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('data/captador_tweets.csv')

#print(df)
#print(df.vacuna_nombre.nunique())
#print(df.vacuna_nombre.unique())

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H1('Lenguajes de programación'),
        html.Img(src='image/logo.png')
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Selecciona el lenguaje', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'lenguajes-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Usuario', 'value' : 'Id'},
                                {'label' : 'Texto', 'value' : 'Texto'}
                                
                            ]
                        )
        ])
    ])

   

],)


if __name__ == ('__main__'):
    app.run_server(debug=True)