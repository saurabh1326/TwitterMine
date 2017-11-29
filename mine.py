from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "2933696482-A4735XFIFA3t1GTWc0mRyjfilrY6oc6nvOCznz7"
access_token_secret = "IC2gHRJM75I9zzOX4O08OA1zS60lVE0OViYDhdQhI0urg"
consumer_key = "7nKbr3iKVBBWRDaDEGP9wyyDk"
consumer_secret = "gvOgHbow2gZylVFpaIioEkYXrvnFc0Lu7p2kpoJF3u699fXzA2"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
    



    
    
    
    