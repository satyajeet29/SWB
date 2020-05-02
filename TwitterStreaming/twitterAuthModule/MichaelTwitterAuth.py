from tweepy import OAuthHandler

#Paths:
#path = "twitterAuthorization//"             #path has been put in a way so that it can be run from terminal
path = "..//twitterAuthorization//"
authFile = open(path+"MichaelTwitterAuth.txt",'r')
line = [line for line in authFile]

def parser(lineString, index):
    return str(line[index].split("=")[1].strip())


#Authorization tokens:
consumer_key = parser(line,0)
consumer_secret = parser(line,1)
access_token = parser(line,2)
access_token_secret = parser(line,3)

def authorization():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth