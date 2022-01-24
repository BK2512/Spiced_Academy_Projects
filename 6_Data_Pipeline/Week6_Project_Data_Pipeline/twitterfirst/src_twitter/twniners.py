import tweepy
from credentials import *
import logging
import pymongo

clientmo = pymongo.MongoClient(host="Mongoniner", port=27017)
db = clientmo.twitter
collectionniner=db.coll_niner

##### AUTHENTICATION #####
client = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY,consumer_secret=API_KEY_SECRET,
access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)

if client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')

query2 = '#Niners -is:retweet' # with -is -> keine retweets - is -> mit retweets


search_tweets = client.search_recent_tweets(query=query2,tweet_fields=['id','created_at','text'], max_results=20) 
#print(search_tweets)
file = open('Niner_tweets.txt',mode='w',encoding="utf-8")
for tweet in search_tweets.data:
    logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')
    #file = open('Niner_tweets.txt',mode='a',encoding="utf-8") # --> Für ein Textfile
    #file.write(tweet.text)
    #file.close()
    
    #Regex?
    doc_tweet={"text":tweet.text}
    logging.critical(f"\n---- INSERTING A NEW Tweet DOCUMENT INTO THE 'collectionniner' ----\n")
    collectionniner.insert_one(document=doc_tweet)
    if collectionniner.find_one(doc_tweet):
        logging.critical(f"\n---- Tweet DOCUMENT SUCCESSFULLY INSERTED ----\n")