import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging
import re

s = SentimentIntensityAnalyzer()

time.sleep(20)

clientmo = pymongo.MongoClient(host="Mongoniner", port=27017)
db = clientmo.twitter
collectionniner=db.coll_niner


docs=collectionniner.find(limit=30)

pg=create_engine('postgresql://postgres:postgres@pg:5432/pgdb',echo=True,client_encoding='utf8')

pg.execute("""
CREATE TABLE IF NOT EXISTS tweet_table (
    id BIGSERIAL,
    transformed_text TEXT,
    sentiment NUMERIC
);

""")

#def load(clean_text,sentiment):
    #pg.execute(f'INSERT INTO tweet_table (transformed_text,sentiment) values ({clean_text},{sentiment});')
    #query='INSERT INTO tweet_table (transformed_text,sentiment) VALUES ({clean_text},{sentiment});'
    #pg.execute(query,(clean_text,sentiment))
    #logging.critical(f"Tweet AND SENTIMENT {sentiment} LOADED INTO POSTGRES")

for doc in docs:
    logging.critical("""\n---Tweet EXTRACTED---\n{}""".format(doc['text']))
    text=doc['text']
    clean_text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    clean_text=' '.join(re.findall('(?u)\\b\\w+\\b',clean_text.lower())) # Cleaning Data
    sentiment=s.polarity_scores(clean_text) # Sentiment Score
    print(sentiment)
    score=sentiment['compound']
    def load(clean_text,sentiment):
        pg.execute(f"""
    INSERT INTO tweet_table (transformed_text, sentiment)
    VALUES ('{clean_text}', '{sentiment}');
    """
    )
    logging.critical(f"TWEET AND SENTIMENT {sentiment} LOADED INTO POSTGRES")
    
    load(clean_text,sentiment=score)