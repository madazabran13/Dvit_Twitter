#Segunda entrega

from twarc import Twarc2, expansions
import json
import authentication as credentials
import time

# Replace your bearer token below
client = Twarc2(bearer_token=credentials.Bearer_Token)
usuario = 'midudev'

def main():
    while True:
        user_timeline = client.timeline(user=usuario)
        tweets(user_timeline)
        time.sleep(30)


def tweets(user_timeline):
    for page in user_timeline:

        result = expansions.flatten(page)
        for tweet in result:
            guardar = json.dumps(tweet, indent=4)
            guardado = open("data/segunda_entrega.json", "w")
            guardado.write(guardar)
            guardado.close()
            leer_tweets()
        leer_contexto()
    


def leer_tweets():
    leer = open('data/segunda_entrega.json', 'r')
    data = json.load(leer)
    leer.close()
    Trascribir(json.dumps(data['author'], indent=4))
    leer_user()


def Trascribir(parametro):
    save = open('data/segunda_entrega.json', 'w')
    save.write(parametro)
    save.close()


def leer_user():
    leer = open('data/segunda_entrega.json', 'r')
    data = json.load(leer)
    leer.close()
    Trascribir(json.dumps(data['public_metrics'], indent=4))
    


def leer_contexto():
    leer = open('data/segunda_entrega.json', 'r')
    data = json.load(leer)
    followers = data['followers_count']
    following = data['following_count']
    tweet = data['tweet_count']
    listed = data['listed_count']
    leer.close()
    print("Seguidores: ",followers," Seguido: ",following," tweets: ",tweet," listed: ",listed)

# codigo principal
if __name__ == "__main__":
    main()