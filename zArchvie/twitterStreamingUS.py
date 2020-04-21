#import sys
#sys.path.insert(0,'/twitterAuthModule/')
import numpy as np
from TwitterStreaming.twitterAuthModule import twitterAuth as tA

from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import os
import datetime

#Variable to store output files
outputPath = '..//SWB//outputSample//'

#Create a directory if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)



class StdOutListener(StreamListener):
    def on_data(self, data):
        fileName = "tweets_"+str(datetime.datetime.now().date()).replace('-', '_')
        file = open(outputPath+fileName+'.txt', 'a')
        file.write(data+'\n')
        print(data)

        return True

    def on_error(self, status):
        print(status)


#if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = tA.authorization()
stream = Stream(auth, l)

auth = tA.authorization()
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#Obtain Geo Code Location of Palo Alto California
places = api.geo_search(query="USA", granularity="country")
place_id = places[0].id

#preventiveString, riskString, elderlyString, sentiments, misc = gA.returnSearchString()

searchString = 'place:'+place_id+' #COVID-19 OR "COVID-19" OR "pandemic" OR "Corona"'

cursor = Cursor(api.search, q=searchString, count=20, lang="en", tweet_mode='extended')
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)





#Location to be filtered based on USA
api = API(auth)
places = api.geo_search(query="USA", granularity="country")
#places = api.geo_search(query="Palo Alto, CA", granularity="city")
a = np.array(places[0].bounding_box.coordinates[0])
b = [min(a[1,:]), min(a[:,1]), max(a[1,:]), max(a[:,1])]
stream.filter(locations=b)
#stream.filter(track=['#COVID19',"Covid 19","Corona", "Pandemic", "Virus"])