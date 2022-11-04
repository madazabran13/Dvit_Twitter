import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input, State
import pandas as pd
import twitter  # pip install python-twitter
from app import app, api


mentions_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Número de resultados"),
                        dcc.Dropdown(
                            id="count-mentions",
                            multi=False,
                            value=50,
                            options=[
                                {"label": "50", "value": 50},
                                {"label": "100", "value": 100},
                                {"label": "200", "value": 200},
                                {"label": "300", "value": 300},
                                {"label": "400", "value": 400},
                                {"label": "500", "value": 500},
                            ],
                            clearable=False,
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        html.Label("Busqueda"),
                        dcc.Input(
                            id="input-handle",
                            type="text",
                            placeholder="Mensaje a buscar",
                            value="python",
                        ),
                    ],
                    width=3,
                ),
            ],
            className="mt-4",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Button(
                            id="hit-button",
                            children="Buscar",
                            style={"background-color": "#366A96", "color": "white"},
                        )
                        
                    ],
                    width=2,
                )
            ],
            className="mt-2",
        ),
        dbc.Row(
            [
                dbc.Col([dcc.Graph(id="myscatter", figure={})], width=6),
                dbc.Col([dcc.Graph(id="myscatter2", figure={})], width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            id="notification",
                            children="",
                            style={"textAlign": "center"},
                        )
                    ],
                    width=12,
                )
            ]
        ),
         dbc.Row([dbc.Col([html.P('© Desarrollado por: Miguel Daza - Daniel Prasca - Heimis Miranda.',  style={"textAlign": "center"})])])
    ]
)


# pull data from twitter and create the figures
@app.callback(
    Output(component_id="myscatter", component_property="figure"),
    Output(component_id="myscatter2", component_property="figure"),
    Output(component_id="notification", component_property="children"),
    Input(component_id="hit-button", component_property="n_clicks"),
    State(component_id="count-mentions", component_property="value"),
    State(component_id="input-handle", component_property="value"),
)

def display_value(nclicks, num, acnt_handle):
    results = api.GetSearch(
        raw_query=f"q=%40{acnt_handle}&src=typed_query&count={num}"
    )       #       q=%40MoveTheWorld%20until%3A2021-08-05%20since%3A2021-01-01&src=typed_query

    twt_followers, twt_likes, twt_count, twt_friends, twt_name = [], [], [], [], []
    for line in results:
        twt_likes.append(line.user.favourites_count)
        twt_followers.append(line.user.followers_count)
        twt_count.append(line.user.statuses_count)
        twt_friends.append(line.user.friends_count)
        twt_name.append(line.user.screen_name)

        print(line)

    d = {
        "followers": twt_followers,
        "likes": twt_likes,
        "tweets": twt_count,
        "friends": twt_friends,
        "name": twt_name,
    }
    df = pd.DataFrame(d)
    print(df.head())

    most_followers = df.followers.max()
    most_folwrs_account_name = df["name"][df.followers == most_followers].values[0]
    
    scatter_fig = px.scatter(
        df, x="followers", y="likes", trendline="ols", hover_data={"name": True}
    )
    scatter_fig2 = px.scatter(
        df, x="friends", y="likes", trendline="ols", hover_data={"name": True}
    )
    message = f'La cuenta de Twitter @{most_folwrs_account_name} menciona #{acnt_handle} tiene el mayor número de seguidores: ( {most_followers} ).'
    return scatter_fig, scatter_fig2, message

#'© Desarrollado por: Miguel Daza - Daniel Prasca - Heimis Miranda.'