import re
import ast
import json
import pandas as pd
def fileParse(file):
    f = open(file,'r', encoding = 'utf-8')
    text = str(f.read())
    textLines = text.splitlines()
    patternJsonExtract = r"(_json=)({'created_[\W\w]*?'lang':\s'[\w]*\'}?)"

    jsonPattern = r"(_json=)({[\W\w]*'lang': 'en'})"

    #failArray = [] # to store arrays that couldn't be converted to JSON
    #jsonArray = [] # to store arrays that we were able to convert to JSON
    #for k, line in enumerate(textLines):
    #    try:
    #        parseJson = re.findall(jsonPattern, line)
    #        jsonArray.append(ast.literal_eval(json.loads(json.dumps(parseJson[0][1]))))
    #    except:
    #        failArray.append(k)

    jsonExtract = []
    for line in textLines:
        temp = re.findall(patternJsonExtract, line)
        jsonExtract.append([x[1] for x in temp])


    def cleanJsonTexts(x):
        x = x.replace('\'', '"').replace('False', '"False"').replace('True', '"True"').replace('None', '"None"')
        # Extract device urls
        patternDeviceFullString = r'<a href="[\w\:\/\.\"\s\=]*>[\w{\s|\-}]*<\/a>'
        devFullURL = re.findall(patternDeviceFullString, x)
        devUnSplitURL = re.findall(patternDevice, x)
        devSplitURL = [i[1] for i in devUnSplitURL]
        # Clean up URLS
        if len(devFullURL) > 0:
            for k, string in enumerate(devFullURL):
                x = x.replace(devFullURL[k], devSplitURL[k])

        return x


    #process to clean failed array
    patternFullText = r'("full_text": ")([\w\W]*?)(", "truncated")'
    patternHashTag = r'("hashtags":)([\w\W]*?)(, "symbols")'
    patternLocation = r'("location": ")([\w\W]*?)(", "description")'
    patternExpURL = r'("expanded_url": ")([\w\W]*?)(", "display_url": [\w\W]* "metadata":)'
    patternRetweet = r'("retweeted": ")([\w\W]*?)(", "possibly_sensitive")'
    patternDevice = r'("source": ")([\w\W]*?)(", "in_reply_to_status_id":)'
    patternTweetID = r'("id": )([0-9]{19}?)'
    patternTime = r'("created_at": ")([\W\w]*?)(", "id":)'
    patternIsQuote = r'("is_quote_status": ")([\W\w]*?)(",)'
    fullText = []; hashTag = []; location = []; url = []; retweet = []; device = []; tweetID = []; time = []; isQuote = [];

    cleanJSONExtract = []
    for extract in jsonExtract:
        cleanJSONExtract.append([cleanJsonTexts(i) for i in extract])

    for extract in cleanJSONExtract:
        tText = []; tTag = []; tLocation = []; turl = []; tretweet = []; tdevice = []; tTweetID = []; tTime = []; tisQuote = [];
        for tweet in extract:
            tText.append(re.findall(patternFullText, tweet)[0][1].strip())
            tTag.append(re.findall(patternHashTag, tweet)[0][1].strip())
            tLocation.append(re.findall(patternLocation, tweet)[0][1].strip())

            if len(re.findall(patternExpURL, tweet)) > 0:
                turl.append(re.findall(patternExpURL, tweet)[0][1].strip())
            else:
                turl.append('No url')

            if len(re.findall(patternRetweet, tweet)) > 0:
                tretweet.append(re.findall(patternRetweet, tweet)[0][1].strip())
            else:
                tretweet.append('Not found')

            tdevice.append(re.findall(patternDevice, tweet)[0][1].strip())
            tTweetID.append(re.findall(patternTweetID, tweet)[0][1].strip())
            tTime.append(re.findall(patternTime, tweet)[0][1].strip())
            tisQuote.append(re.findall(patternIsQuote, tweet)[0][1].strip())

        fullText.append(tText); hashTag.append(tTag); location.append(tLocation); url.append(turl)  # Needs bit more cleaning
        retweet.append(tretweet); device.append(tdevice); tweetID.append(tTweetID); time.append(tTime); isQuote.append(tisQuote)

        tArray = []
        for k, text in enumerate(fullText):
            for ind, t1 in enumerate(text):
                temp = []
                temp.append(k)
                temp.append(tweetID[k][ind])
                temp.append(time[k][ind])
                temp.append(device[k][ind])
                temp.append(retweet[k][ind])
                if len(ast.literal_eval(hashTag[k][ind])) > 0:
                    temp.append([x['text'] for x in ast.literal_eval(hashTag[k][ind])])
                else:
                    temp.append(["No hashtags"])
                temp.append(url[k][ind])
                temp.append(isQuote[k][ind])
                temp.append(location[k][ind])
                temp.append(text[ind])
                tArray.append(temp)

    df = pd.DataFrame(tArray, columns=['StringIndex', 'TweetID', 'TimeStamp', 'Device', \
                                       'Retweet', 'HashTags', 'Ext URL', 'isQuote', 'Location', 'FullText'])

    df['File'] = file.split('//')[-1]
    df['CodeSet'] = file.split('//')[-2]

    dfUnique = df.drop(columns=['StringIndex']).copy()
    dfUnique['HashTags'] = dfUnique['HashTags'].astype(str)
    dfUnique = dfUnique.drop_duplicates().reset_index(drop=True)

    return df, dfUnique

