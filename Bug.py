import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
import pandas as pd  

def authenticate(Path):
    lol = open(Path,'r')
    global consumer_key
    global consumer_secret
    global access_token
    global access_token_secret
    temp = []
    for line in lol:
        temp.append(line.split(None, 1)[0])

    consumer_key = temp[0]

    consumer_secret = temp[1]

    access_token = temp[2]

    access_token_secret = temp[3]
##Login to Twitter API using Tweepy
authenticate("Passwords.txt")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)






api = tweepy.API(auth)


places = api.geo_search(query="USA", granularity="country")

United_states = places[0].id
#tweets = api.search(q= "COVID-19 place:%s" % United_states,lan = 'en' , count = 10000,tweet_mode = 'extended')
#tweets = api.search(q="COVID-19",lan= 'en', count= 1000)
query = "COVID-19 place:%s" % United_states
max_tweets = 1000
tweets = [status for status in tweepy.Cursor(api.search, q=query,lan = 'en',tweet_mode = 'extended').items(max_tweets)]
columns = ['Username','Id','Tweet',"Location","geocode"]
df = pd.DataFrame(columns= columns)

for tweet in tweets:
   # print    tweet.user.screen_name + str(tweet.user.id) + "| " +  tweet.text + " | " + tweet.user.location + "| " + tweet.place.name if tweet.place else "Undefined place"
    df = df.append(pd.Series([tweet.user.screen_name, str(tweet.user.id), tweet.full_text,tweet.user.location,tweet.place.name], index=df.columns), ignore_index="True")

#new_df.to_csv("Database.csv") ##Dosent work
print(df)
df.to_csv("Dataset10.csv", sep='\t', encoding = 'utf-8')
   ##todo #pre process tweet and if in englsh it is relevant keep track of user and look user




































