import pandas as pd
import os
outputPath = "/Users/satyajeetpradhan/SWB_Covid_19/outputPath/".replace('/','//')
subDir = ['PaloAlto','WashingtonDC','SunnyVale','set0','set1','set2','set3','set4','set5','USA']
masterCSVPath = "/Users/satyajeetpradhan/SWB_Covid_19/".replace('/','//')
#dummy datarame to which datasets would be appended
df = pd.DataFrame(None, columns=['TweetID', 'TimeStamp', 'Device','Retweet', 'HashTags', 'Ext URL', 'isQuote', 'Location', 'FullText'])

for path in subDir:
    lpath = outputPath + path + '//'
    fileList = os.listdir(lpath)
    fileList.sort()

    for file in fileList:
        fileParse = lpath + file
        temp = pd.read_csv(fileParse)
        df = df.append(temp)
        df = df.drop_duplicates()

df = df.drop(columns = ['Unnamed: 0']).drop_duplicates().reset_index(drop = True)
print("No of unique tweets: ",df.shape)

df.to_csv(masterCSVPath+'MasterFile.csv')
del df


