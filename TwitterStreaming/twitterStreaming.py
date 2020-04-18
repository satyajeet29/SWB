from tweepy.streaming import StreamListener
from tweepy import Stream
from twitterAuth import twitterAuth as tA

import os
import datetime

#Variable to store output files
outputPath = '..//output//'

#Create a directory if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

#Location to be filtered based on Palo Alto Coordinates
locationFilterBoxList = [-122.12,34.8,-121.12,35.8]

class StdOutListener(StreamListener):
    def on_data(self, data):
        fileName = "tweets_"+str(datetime.datetime.now().date()).replace('-', '_')
        file = open(outputPath+fileName+'.txt', 'a')
        file.write(data+'\n')
        print(data)

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = tA.authorization()
    stream = Stream(auth, l)
    stream.filter(locations= locationFilterBoxList)