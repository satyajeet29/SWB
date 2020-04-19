# Mainly focussed around streaming data on Palo Alto

from TwitterStreaming.twitterAuthModule import twitterAuth as tA
#from TwitterStreaming.gitAuthModule import gitAuth as gA

from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import Cursor
from tweepy import API

import os
import datetime


#Variable to store output files
outputPath = '..//SWB//outputSampleHigh//'

#Create a directory if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

auth = tA.authorization()
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#Obtain Geo Code Location of Palo Alto California
#places = api.geo_search(query="USA", granularity="country")
places = api.geo_search(query="Palo Alto,CA", granularity="city")
place_id = places[0].id

#preventiveString, riskString, elderlyString, sentiments, misc = gA.returnSearchString()

searchString = 'place:'+place_id+' #COVID-19 OR "COVID-19" OR "pandemic" OR "Corona"'

cursor = Cursor(api.search, q=searchString, count=20, lang="en", tweet_mode='extended')
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

maxCount = 1000
count = 0

for tweet in cursor.items():
    count+=1
    fileName = "tweets_"+str(datetime.datetime.now()).replace('-', '_').replace(' ', '_').replace(':', '_')
    file = open(outputPath+fileName+'.txt', 'a')
    file.write(str(tweet) + '\n')
    print(count)
    print(tweet)
    print("\n")
