#!Python3

import tweepy 
import json
import os
import sys
import webbrowser

Indian_sub = [63.02,6.75,97.47,28.8,64.24,28.84,80.5,35.67]
#location is given in long,lat format;the order is (southwest corner,northeast corner).


print("Enter consumer key \n")
consumer_key = input()
print("Enter consumer secret \n")
consumer_secret = input()


#getting necessary authorization
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
#redirecting to give permission
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')
webbrowser.open(redirect_url)
#here you should copy the pin 


print("Enter the authorisation pin: \n")
pin = input()
print(pin)

token = auth.get_access_token(verifier=pin)
#generating access_token and access_key
access_key = auth.access_token
access_secret = auth.access_token_secret
#print(access_key,access_secret)

auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)


class myListener(tweepy.StreamListener):
    def __init__(self):
        self.num_tweets = 0   #for generating specified number of tweets
    
    def on_data(self, data):
        decoded = json.loads(data)
        str1 = str(decoded)
        if self.num_tweets < num:
            with open('india_data.txt','a') as ind_data:
                ind_data.write("\n Tweet number: " + str(self.num_tweets+1) + "\n\n")
                ind_data.write(str1)
                self.num_tweets += 1
                #print(os.path.getsize("india_data.txt"))
                return True
        else :
            return False

    def on_error(self, status_code):
        print(status_code)
        
print("Enter the Number of Tweets you want to generate")
num = int(input())
mylistener = myListener()
stream =  tweepy.Stream(auth = api.auth, listener=mylistener)
stream.filter(locations=Indian_sub)

