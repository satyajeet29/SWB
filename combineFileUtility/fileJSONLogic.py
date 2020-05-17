import pandas as pd
import ast, json, re

def jsonParse(file):
    f = open(file, 'r')
    text = str(f.read())
    textLines = text.splitlines()
    jsonPattern = r"(_json=)({[\W\w]*'lang': 'en'})"

    failArray = []
    jsonArray = []
    for k, line in enumerate(textLines):
        try:
            parseJson = re.findall(jsonPattern, line)
            jsonArray.append(ast.literal_eval(json.loads(json.dumps(parseJson[0][1]))))
        except:
            failArray.append(k)

    #print("success:",len(jsonArray), ", failure: " ,len(failArray))

    tweetID = []; fullText = []; hashTag = []; location = []; url = []; retweet = []; device = []; time = []; isQuote = [];

    for jsonVal in jsonArray:
        tweetID.append(jsonVal['id'])
        fullText.append(jsonVal['full_text'])
        try:
            hashTag.append([x['text'] for x in jsonVal['entities']['hashtags']])  # check for length
        except:
            hashTag.append(['No hashtags'])

        try:
            location.append(jsonVal['place']['full_name'])
        except:
            location.append("No Information")

        try:
            url.append(jsonVal['entities']['urls'])
        except:
            url.append("No URL")

        retweet.append(jsonVal['retweeted'])
        device.append(jsonVal['source'])
        time.append(jsonVal['created_at'])
        isQuote.append(jsonVal['is_quote_status'])

    tArray = []
    for k, text in enumerate(fullText):
        temp = []
        temp.append(k)
        temp.append(tweetID[k])
        temp.append(time[k])
        temp.append(device[k])
        temp.append(retweet[k])
        temp.append(hashTag[k])
        temp.append(url[k])
        temp.append(isQuote[k])
        temp.append(location[k])
        temp.append(text)
        tArray.append(temp)

    df = pd.DataFrame(tArray, columns=['StringIndex', 'TweetID', 'TimeStamp', 'Device', \
                                       'Retweet', 'HashTags', 'Ext URL', 'isQuote', 'Location', 'FullText'])

    df = df.drop(columns=['StringIndex'])
    df['HashTags'] = df['HashTags'].astype(str)
    df['Ext URL'] = df['Ext URL'].astype(str)
    df = df.drop_duplicates().reset_index(drop=True)

    print("success:", len(jsonArray), ", failure: ", len(failArray), "unique:", df.shape)
    return df
