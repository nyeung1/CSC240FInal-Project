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





tweets = api.search(q="Face Mask",count= 200,tweet_mode ='extended',lang ='en')
#tweets = [status for status in tweepy.Cursor(api.search, q=query,lan = 'en',tweet_mode = 'extended').items(max_tweets)]
columns = ['Username','Id','Tweet',"Location"]
df = pd.DataFrame(columns= columns)

for tweet in tweets:
     #print    tweet.user.screen_name + str(tweet.user.id) + "| " +  tweet.text + " | " + tweet.user.location + "| " + tweet.place.name if tweet.place else "Undefined place"
     df = df.append(pd.Series([tweet.user.screen_name, str(tweet.user.id), tweet.full_text,tweet.user.location], index=df.columns), ignore_index="True")

#new_df.to_csv("Database.csv") ##Dosent work
print(df)
df.to_csv("Dataset13.csv", sep='\t', encoding = 'utf-8')
   ##todo #pre process tweet and if in englsh it is relevant keep track of user and look user




































