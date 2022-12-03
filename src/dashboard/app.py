import dash
import dash_bootstrap_components as dbc
import twitter
import tweepy

consumer_key = "tslgpq7gwhnWw3QYarXMCPwlc"
consumer_secret = "rNYyeEwmVmW95qIQUl1IJWynCTsbSjkdj7SK0AhM0jfu1YvPeO"
access_token_key = "1543831621995986945-Xx4GMorGlisGtw0GbalYSSZyCo7NjM"
access_token_secret = "GNszLt2bXXC7LjuF9F7ErqxF54hW1B2b8auChXDyQycqL"

api = twitter.Api(consumer_key,consumer_secret, access_token_key, access_token_secret)

# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token_key,access_token_secret)
# api = tweepy.API(auth)


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
