#Primera entrega del proyecto: buscador de tweets

import tweepy

#Cadenas para la autenticacion para hacer requerimientos
api_key = 'ktI94wQ3fM5PbHIdLriMwWE4z'
API_Key_Secret = 'DE4ZNxYhVF4dGxnsHrN2T9kGg0AAUHKQKzChcjF8tczJDpkqE6'   
Access_Token = '1558818772483440641-r4JM5XMQ9cGaNaFChWEZybDhCalkab'
Access_Token_Secret = 'E24MPwkVAfBlNHvGDN3WXM3e4kSLNS3ZHzw6aGn7ZqHRf' 
Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAACrvhQEAAAAAKU%2BSlUYHeHnG%2BhUNBn5ABgAVbmQ%3D38VwL15mf1Hw1A9ohZO49QtOYBHvL2PuWPcSMktVIRsZp0b4Jp'

    
#Cliente de tweepy
api = tweepy.Client(consumer_key=api_key,consumer_secret=API_Key_Secret,access_token=Access_Token,access_token_secret=Access_Token_Secret,bearer_token=Bearer_Token)

#Buscador
busqueda = "#python OR #progrmacion OR #lenguajedeprogramacion"

#Obtengo en unavaribale los resultados de esa busqueda,un maximo de resultados y usuario
datos = api.search_recent_tweets(query=busqueda, max_results=50, expansions=['author_id'])
# data = tweepy.Cursor(api.search_spaces,query=busqueda, max_results=50,  tweet_mode='extended', expansions=['author_id'])

#Recorro cada resultado trayendo el usuario y mensaje en la terminal
for tweet in datos.data:
    print('Datos (Usuario/Mensaje):')
    print(tweet.text,"\n")