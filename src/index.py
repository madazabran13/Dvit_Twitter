import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('data/captador_tweets.csv')
app = dash.Dash('Dvit')

app.layout = html.Div([
    
    html.Header([
        html.H1('Lenguajes de programación'),
        html.Img(src='image/logo.png')
    ], className = 'banner'),

],)

if __name__ == ('__main__'):
    app.run_server(debug=True)