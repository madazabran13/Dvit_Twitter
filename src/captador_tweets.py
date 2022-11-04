#Capatdor de tweets - guarda en archivo csv

#Importo las librerias
import tweepy
import csv #Import csv
from datetime import date, datetime
import os
import authentication as authentication

#Defino una funcion almacenar para guardar los tweets
def almacenar_tweet( status):
            csvFile = open('data/captador_tweets.csv', 'a', encoding= 'utf-8', newline='')
            csvWriter = csv.writer(csvFile)
            if status is not False and status.text is not None:
                try:
                    texto = status.extended_tweet["full_text"]
                except AttributeError:
                    texto = status.text
                texto = texto.replace('\n', ' ')
                print(texto)
                linea = [status.created_at,status.id, texto, status.source, status.truncated,status.in_reply_to_status_id, status.in_reply_to_user_id,status.in_reply_to_screen_name, status.geo, status.coordinates,status.place,status.contributors, status.lang, status.retweeted]
                linea = linea
                csvWriter.writerow(linea)
            print("Almacenamos Tweet")
            csvFile.close()
            print("fin")

#Condicional que me capta los tweets
if __name__ == '__main__':
    print("===== Captador de tweets =====")
    # Get an API item using tweepy
    auth = tweepy.OAuthHandler(authentication.consumer_key, authentication.consumer_secret)
    auth.set_access_token(authentication.access_token, authentication.access_token_secret)
    api = tweepy.API(auth)

    if os.path.isfile(
                    'data/captador_tweets.csv'):
               print('Preparado el fichero')
    else:
                print('El no archivo existe.');
                csvFile = open('data/captador_tweets.csv', 'w', encoding= 'utf-8',  newline='')
                csvWriter = csv.writer(csvFile)
                cabecera=['--- Fecha_creación --- ',' --- Id --- ',' --- Texto --- ',' --- Fuente --- ',' ---Truncado --- ',' --- Respuesta_al_tweet --- ',' --- Respuesta_al_usuario_id --- ',' --- Respuesta_al_usuario_nombre --- ']
                csvWriter.writerow(cabecera)
                csvFile.close()
                print("Creación de la cabecera")

    start_date = datetime(2020, 10, 10, 12, 00, 00)
    end_date = date.today()

    for tweet in tweepy.Cursor(api.search_tweets, q="programacion OR python OR java" ,lang="es",since=start_date ,until= end_date ).items():
                print(tweet.created_at, tweet.text)
                almacenar_tweet(tweet)
    # End
    print("Terminado")