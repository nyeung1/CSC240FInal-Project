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

authenticate("Passwords.txt")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)






api = tweepy.API(auth)
list = []
#public_tweets = api.home_timeline()
#public_tweets = api.user_timeline('Jonathanlai18')

#for tweet in public_tweets:

 #   list.append(tweet.text)

#for status in tweepy.Cursor(api.user_timeline).items():
  
    #print(status.text)
places = api.geo_search(query="USA", granularity="country")

United_states = places[0].id
tweets = api.search(q= "Coronavirus place:%s" % United_states,lan = 'en' , count = 7000)
#x = api.search(q = "Coronavirus" , lang = 'en',count = 7000)

for tweet in tweets:
    print tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place"


#for tweet in x:
   ##todo #pre process tweet and if in englsh it is relevant keep track of user and look user
    #print(tweet.user.screen_name)
    #print(tweet.text)


class MyStreamListener(tweepy.StreamListener):

     def on_status(self, status):
       print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(api.auth,myStreamListener)
myStream.filter(track=['Coronavirus'])



#todo Look at how to seperate stream by langauge to ignore spanish and location.



tweets_data_path = "twitter_data.txt"
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['Username'] = list(map(lambda tweet: tweet['user']['screen_name'], tweets_data))
tweets['Timestamp'] = list(map(lambda tweet: tweet['created_at'], tweets_data))
tweets.head()
