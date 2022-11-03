# Buscador por filtro y cantidad

#Importo las librerias 
import tweepy
import time
import authentication as authentication

#Autenticacion de tweepy
auth = tweepy.OAuthHandler(authentication.consumer_key, authentication.consumer_secret)
auth.set_access_token(authentication.access_token, authentication.access_token_secret)
api = tweepy.API(auth)
    
#La palabra que se buscará y la cantidad de tweets a buscar
keyboard = input('Escribe la palabra a buscar: ')
  
#Ciclo para conseguir los tweets y guardarlos en un archivo txt  
limit = 400
id = None 
count = 0 
while count <= 100:
    #Obtener tweets
    for tweet in tweepy.Cursor(api.search_tweets,q=keyboard, tweet_mode='extended',max_id=id).items(limit):
        print('El texto es: ' + tweet.full_text)
        print('Numero de retweets es: ' + str(tweet.retweet_count))
        print('\n')
        if tweet.full_text.startswith('RT'):
            count = count + 1
            continue
        f = open('data/buscador_tweets.txt','a',encoding='utf-8')
        f.write('\n Usuario: '+ tweet.user.screen_name +'\n Mensaje: '+ tweet.full_text  + '\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n \n')
        f.close()
        print(tweet.full_text)
        print()
        count = count + 1
    id = tweet.id
    print(count)
    time.sleep(1)   
