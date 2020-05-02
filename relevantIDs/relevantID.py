import pandas as pd
import numpy as np
import tweepy
import time
np.set_printoptions(precision = 20, suppress = True)
path = "//Users////SWB_Covid_19//"  #<<--Change path suitably
file = "tweet_IDs.csv"
tweet_IDS = pd.read_csv(path+file)

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#break tweets into buckets of 100 tweets in each bucket, note last bucket might have less tweets
testIDBin = []
counter =0
arrayCovered = 0
temp =[]
testID = [int(x) for x in tweet_IDS.id]
for ids in testID:
    temp.append(ids)
    counter+=1
    arrayCovered+=1
    if arrayCovered >= len(testID):
        testIDBin.append(temp)
        break
    elif counter == 100:
        testIDBin.append(temp)
        temp = []
        counter = 0


totalResponses = 0
successDict = {}

#Search and extract for relevant values
for k, bucket in enumerate(testIDBin):
    try:
        #print("Trying: ",k)
        test = api.statuses_lookup(bucket)
        #print(test)
        print(k,"Count of tweets: ",len(test))
        successDict[k] = len(test)
        for string in test:
            file = open(path+'idBasedOutput.txt', 'a')
            file.write(str(string) + '\n')
    except:
        print("\n")
        #print("Not found",k)
        #successDict[k] = 'Not Found'

#print(successDict)
successRate = []

print('bin#','\t','#tweets','\t','#binsize','\t','success')
for keys in list(successDict.keys()):
    print(keys,'\t' ,successDict[keys], '\t' ,len(testIDBin[keys]), '\t' ,successDict[keys]/len(testIDBin[keys]))
    successRate.append(successDict[keys]/len(testIDBin[keys]))

print('\n')
d1 = np.array(successRate)
print("-------------------------------------------------------------")
print("----------------------Success Statistics---------------------")
print("Max success rate in 100 count size bin: ",d1.max())
print("Mean success rate in 100 count size bin: ",d1.mean())
print("Min success rate in 100 count size bin: ",d1.min())
print("-------------------------------------------------------------")