# Mainly focussed around streaming data on Washington DC
index = 4
from TwitterStreaming.twitterAuthModule import twitterAuth as tA
#from TwitterStreaming.gitAuthModule import gitAuth as gA

from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import Cursor
from tweepy import API

placeSearch =['place:26b9557935d73cba OR place:4b58830723ec6371 OR place:272f29aa61fa05d3 OR place:00f751614d8ce37b OR place:afe336fdd7d1b837 OR place:99e789320196ef6a OR place:a3d48e0ce0736723 OR place:5ef5b7f391e30aff OR place:4ccb1b26b2b91248 OR place:afe336fdd7d1b837 OR place:2ecc2108e9d5d658 OR place:f28195f8b183abcd OR place:04016a4890553832 OR place:5cd8f0461e40432c OR place:3df4f427b5a60fea'
              ,'place:30344aecffe6a491 OR place:5015e56ad6f23c9e OR place:5a110d312052166f OR place:d9d3e9c476e0c0dc OR place:0354c827bfda68de OR place:afe336fdd7d1b837 OR place:00b2a7b60c2a6879 OR place:56cf7df6e9683a79 OR place:ec689e69912965d0 OR place:a5c0eba140e25cbb OR place:490bdb082950484f OR place:b46f044cb28493c6 OR place:3df4f427b5a60fea OR place:6fafb06c49df870f'
              ,'place:1153d1a598a817b1 OR place:ea049ae1073a8f35 OR place:5358b6f78dd95ef6 OR place:3ad0f706b3fa62a8 OR place:a35b62af9d82aa08 OR place:014e8cf1001670bd OR place:a2de7c70b82b0ca0 OR place:b0ccc334a6d569d3 OR place:6ef29a7e78ca38a5 OR place:629b15360c8e51ae OR place:010781586e4d76f9 OR place:5cda0a6ac9cf8725 OR place:f6514a91adf25ce4 OR place:7b5667de9caf1b92'
              ,'place:c84cc6061e2af8da OR place:3ad0f706b3fa62a8 OR place:50df1c2f85d2654d OR place:6a4364ea6f987c10 OR place:b19a2cc5134b7e0a OR place:3df4f427b5a60fea OR place:ad4876a662119b74 OR place:61f1d75eb5064808 OR place:c7b003d493c9e5ee OR place:526d2258fff0f7ad OR place:a409256339a7c6a1 OR place:36237ab3643ff2be OR place:ccb1d10a24cf562a OR place:6a71821001635bbd'
              ,'place:4ccacb29ffb3b3df OR place:a769d8f00b12878d OR place:9b101e0451f073b6 OR place:59bb4e6ce17a8b66 OR place:d70cebab5f549266 OR place:0941c439c73f4f7b OR place:e872bcd2497287a7 OR place:432daa3153c5fef9 OR place:5abe94c7f05eb014 OR place:5718a1611923e3e7 OR place:45cadd6ef118ec9f OR place:e4aee3ab11ef52a6 OR place:5ecbd073f39c00fa OR place:239aa72871ae24ab'
              ,'place:8af346f16e955392 OR place:4cfc3d6749b55aca OR place:6a4364ea6f987c10 OR place:00173a837b85dc2b OR place:000a76c020fc19ce OR place:6407905aa8012e44 OR place:276336654aa4f87a OR place:e4e19cea709c4d76 OR place:fa3435044b52ecc7 OR place:3b0eea538598dc42 OR place:8ad73577c2722154 OR place:9902fe95fc7596a7 OR place:77fcb96a24077038 OR place:159279f05be2ade4'
             ]
#['Albany', 'Santa Clara', 'Millbrae', 'Richmond', 'NapaCounty seat', 'Emeryville', 'Moraga', 'Berkeley', 'San Ramon', 'FairfieldCounty seat', 'Pinole', 'American Canyon', 'San Pab#lo', 'Calistoga', 'San RafaelCounty seat']
#['Fremont', 'Woodside', 'South San Francisco', 'Corte Madera', 'Campbell', 'OaklandCounty seat', 'Tiburon', 'San Anselmo', 'Concord', 'Clayton', 'Menlo Park', 'Saratoga', 'San JoseCounty seat', 'Hercules']
#['Belmont', 'Orinda', 'San Bruno', 'East Palo Alto', 'Walnut Creek', 'Cloverdale', 'Los Gatos', 'Yountville', 'Milpitas', 'Suisun City', 'Oakley', 'Rohnert Park', 'Ross', 'Vallejo']
#['Portola Valley', 'Palo Alto', 'Vacaville', 'Los Altos', 'Mountain View', 'San FranciscoCounty seat', 'Pleasanton', 'San Leandro', 'Sausalito', 'Healdsburg', 'Redwood CityCounty seat', 'Cupertino', 'Benicia', 'Daly City']
#['Pittsburg', 'Pacifica', 'Antioch', 'Foster City', 'Pleasant Hill', 'Dixon', 'Morgan Hill', 'San Mateo', 'Larkspur', 'St. Helena', 'Sunnyvale', 'Fairfax', 'Hayward', 'Petaluma']
#['Union City', 'Piedmont', 'Los Altos Hills', 'Half Moon Bay', 'Hillsborough', 'El Cerrito', 'Lafayette', 'Colma', 'Newark', 'Novato', 'Gilroy', 'Belvedere', 'Mill Valley', 'Livermore']

import os
import datetime
import time
def backline():
    print('\r', end='')                     # use '\r' to go back


#Variable to store output files
outputPath = '..//SWB//outputSampleHigh//'

#Create a directory if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

auth = tA.authorization()
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#Obtain Geo Code Location of Palo Alto California
#places = api.geo_search(query="USA", granularity="country")
#places = api.geo_search(query="Washington DC", granularity="city")
#place_id = places[0].id

#preventiveString, riskString, elderlyString, sentiments, misc = gA.returnSearchString()

searchString = placeSearch[index]+' #COVID-19 OR "COVID-19" OR "pandemic" OR "Corona"'

cursor = Cursor(api.search, q=searchString, count=20, lang="en", tweet_mode='extended')
api = API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

maxCount = 1000
count = 0

for tweet in cursor.items():
    count+=1
    fileName = "tweets_"+str(index)+"_"+str(datetime.datetime.now().date()).replace('-', '_')
    file = open(outputPath+fileName+'.txt', 'a')
    file.write(str(tweet) + '\n')
    print(count,end='')
    backline()