import json
import pandas as pd
#Variables
path = "//Users//satyajeetpradhan//SWB_Covid_19//" #<<----Please change it to your file location on local system
file = "covid19_stream2.json"

#Read data files
f = open(path+file, 'r')
tweetString = str(f.read())
tweetStringList = tweetString.splitlines()

# First attempt of extracting clean tweets by reading each line
tweetArray = []
failIndex = []
c = 0
for tweetLine in tweetStringList:

    try:
        tweetArray.append(json.loads(tweetLine))
    except:
        failIndex.append(c)
    c += 1

print("Number of successful tweets jsoned to dict:",'{:,}'.format(len(tweetArray)))

#Extract tweet strings that couldn't be appended
unCleanedTweets =[]
for fail in failIndex:
    if len(tweetStringList[fail]) > 0:
        unCleanedTweets.append(tweetStringList[fail])

#1st attempt to parse unparsed tweets by combining two consecutive tweets
finalCleaningListTweets =[]
for i in range(0,len(unCleanedTweets)-1, 2):
    try:
        tweetArray.append(json.loads(unCleanedTweets[i] + unCleanedTweets[i+1]))
    except:
        finalCleaningListTweets.append(unCleanedTweets[i])
        finalCleaningListTweets.append(unCleanedTweets[i+1])

print("Number of successful tweets jsoned to dict:",'{:,}'.format(len(tweetArray)))
print("Number of Tweets unparsed:",'{:,}'.format(len(finalCleaningListTweets)))

#2nd attempt to parse unparsed tweets by combining three consecutive tweets
finalCleaningListTweetsR1 =[]
for i in range(0,len(finalCleaningListTweets)-1, 3):
    try:
        tweetArray.append(json.loads(finalCleaningListTweets[i]
                                         + finalCleaningListTweets[i+1]
                                            + finalCleaningListTweets[i+2]))
    except:
        finalCleaningListTweetsR1.append(finalCleaningListTweets[i])
        finalCleaningListTweetsR1.append(finalCleaningListTweets[i+1])
        finalCleaningListTweetsR1.append(finalCleaningListTweets[i+2])

print("Number of successful tweets jsoned to dict:",'{:,}'.format(len(tweetArray)))




#4th attempt to parse unparsed tweets by combining four consecutive tweets
finalCleaningListTweetsR2 = []
for i in range(0,len(finalCleaningListTweetsR1)-3,4):
    testString = finalCleaningListTweetsR1[i]\
                            +finalCleaningListTweetsR1[i+1]\
                                +finalCleaningListTweetsR1[i+2]\
                                    +finalCleaningListTweetsR1[i+3]
    try:
        json.loads(testString)
    except json.JSONDecodeError as jex:
        splitVal = int(str(jex).split('char')[-1].replace(')','').strip())
        #print(json.loads(testString[:splitVal]))
        try:
            tweetArray.append(json.loads(testString[:splitVal]))
            #print(json.loads(testString[splitVal:]))
            tweetArray.append(json.loads(testString[splitVal:]))
        except:
            finalCleaningListTweetsR2.append(finalCleaningListTweetsR1[i])
            finalCleaningListTweetsR2.append(finalCleaningListTweetsR1[i+1])
            finalCleaningListTweetsR2.append(finalCleaningListTweetsR1[i+2])
            finalCleaningListTweetsR2.append(finalCleaningListTweetsR1[i+3])

print("Number of successful tweets jsoned to dict:",'{:,}'.format(len(tweetArray)))

testString = "".join(finalCleaningListTweetsR2)
splitVal = 0
counter = 0
while len(testString) > 0:
    #print(counter)
    counter+=1
    if len(testString) == 0:
        break
    else:
        try:
            trial = json.loads(testString)
            tweetArray.append(trial)
            testString = testString[len(str(trial)):]
        except json.JSONDecodeError as jex:
            splitVal = int(str(jex).split('char')[-1].replace(')','').strip())
            if splitVal == 0:
                break
            try:
                tweetArray.append(json.loads(testString[:splitVal]))
                testString = testString[splitVal:]
            except json.JSONDecodeError as jex2:
                splitVal = int(str(jex).split('char')[-1].replace(')','').strip())
                print('error',splitVal)
                if splitVal == 0:
                    break

print("Number of successful tweets jsoned to dict:",'{:,}'.format(len(tweetArray)))

#Decalre structure of dataframe
df = pd.DataFrame(columns = ['text','id_str','lang'])

unparsed =[]
for tweet in tweetArray:
    try:
        df = df.append({'text':tweet['text'],'id_str':tweet['id_str'],'lang':tweet['lang']}, ignore_index=True)
        print("Data Frame shape: ",df.shape)
    except:
        unparsed.append(tweet)

print("Number of tweets that couldn't be parsed:",'{:,}'.format(len(unparsed)))
df.to_csv(path+"ParsedTweets.csv") #Please change the path to suitable location on your system when the output gets written
print("Parsed files stored to CSV")
del df, unparsed
