import pandas as pd
from github import Github

#Function to convert a given data file to bytes
def bytesToDF(bytesDataFile):
    from io import StringIO
    s =str(bytesDataFile,'utf-8')
    data = StringIO(s)
    return pd.read_csv(data)




path = "/Users/satyajeetpradhan/Config/"

file = open(path+'Github.txt','r')

c = 0

for line in file:
    c = c+1
    if c == 1:
        username = str(line.partition('=')[2].strip())
    elif c == 2:
        password = str(line.partition('=')[2].strip())
    else:
        break

g = Github(username, password)

del username, password

repo = g.get_repo("keriwheatley/swb-covid-19-twitter-repo")

contents = repo.get_contents("")

dfHashTags = bytesToDF(repo.get_contents(contents[2].path)[2].decoded_content)

def StringCombine(col_name):
    stringList = ['#'+x for x in dfHashTags[col_name]]
    string =''
    for stringVal in stringList:
        string = string +' OR '+stringVal
    return string[3:]

#preventiveList = ['#'+x for x in dfHashTags['preventative_measures']]
#riskSymptomList = ['#'+x for x in dfHashTags['risks_symptoms']]

preventiveString = StringCombine('preventative_measures')
riskString = StringCombine('risks_symptoms')
elderlyString = StringCombine('elderly')
sentiments = StringCombine('sentiments')
misc = StringCombine('miscellaneous')

def returnSearchString():
    return preventiveString, riskString, elderlyString, sentiments, misc







