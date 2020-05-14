import pandas as pd
import numpy as np
import tweepy
import time
from TwitterStreaming.twitterAuthModule import MichaelTwitterAuth as mTA

np.set_printoptions(precision = 20, suppress = True)
path = "//Users//satyajeetpradhan//SWB_Covid_19//" #<<--Change path suitably
file = "tweet_IDs.csv"
tweet_IDS = pd.read_csv(path+file)
tweet_IDS['id'] = tweet_IDS['id'].astype(int)

auth = mTA.authorization()
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
textDict ={}
actualTest = []
#Search and extract for relevant values
for k, bucket in enumerate(testIDBin):
    try:
        #print("Trying: ",k)
        test = api.statuses_lookup(bucket)
        #print(test)
        print(k,'\t',"Count of tweets: ",len(test))
        successDict[k] = len(test)
        for string in test:
            textDict[string.id] = string.text
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

dfText = pd.DataFrame(list(textDict.items()),columns = ['id','text'])
tweet_IDS = tweet_IDS.merge(dfText, on='id', how='left')

#Write output with text retrieved
tweet_IDS.to_csv(path+"outputTextIDsR1.csv")
del tweet_IDS
