
# coding: utf-8


import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import datetime

print(datetime.datetime.now().time())



ckey = 
csecret = 
atoken = 
asecret = 



#murcia = [-1.157420, 37.951741, -1.081202, 38.029126] #Check it out, is a very nice city!



class listener(StreamListener):

    def on_data(self, data):
        file =  open('tweets_bachelet.dat', 'a')
        # Twitter returns data in JSON format - we need to decode it first
        try:
            decoded = json.loads(data)
        except Exception as e:
            print(e) #we don't want the listener to stop
            return True
        
        if decoded.get('geo') is not None:
            location = decoded.get('geo').get('coordinates')
        else:
            location = '[,]'
        
        
        text = decoded['text'].replace('\n',' ')
        user = '@' + decoded.get('user').get('screen_name')
        created = decoded.get('created_at')
        tweet = '{};{};{};{}\n'.format(user,location,created,text)
        
        file.write(tweet)
        print(tweet)
        file.close()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    print('Starting')
    
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=['bachelet','Bachelet','Chanchelet'])




