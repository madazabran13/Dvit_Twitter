import dash
import dash_bootstrap_components as dbc
import twitter
import tweepy
import statsmodels.api as sm

api = twitter.Api(consumer_key = "vVeVBF6tElV22IKfNuS4UtKvB", consumer_secret = "kD6CD1LAc8W59T0IJmIpNe7RVClGH33JYVpR9CRWkGo1yAGPzv", access_token_key = "1543831621995986945-om4tOYAdD1Zorxobr7TS2O2l1npTHf", access_token_secret = "sxQR0xEy1wjlbFgzIO60g8ZPeDUFQxPW8HqxbjHYI3d4v")

# consumer_key = "vVeVBF6tElV22IKfNuS4UtKvB"
# consumer_secret = "kD6CD1LAc8W59T0IJmIpNe7RVClGH33JYVpR9CRWkGo1yAGPzv"
# access_token_key = "1543831621995986945-om4tOYAdD1Zorxobr7TS2O2l1npTHf"
# access_token_secret = "sxQR0xEy1wjlbFgzIO60g8ZPeDUFQxPW8HqxbjHYI3d4v"

# api = twitter.Api(consumer_key,consumer_secret, access_token_key, access_token_secret)

# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token_key,access_token_secret)
# api = tweepy.API(auth)


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
