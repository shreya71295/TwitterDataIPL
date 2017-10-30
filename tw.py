#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "784597229554262016-90jngCQnPRFVWkxE6JpYqWn8I9fkeMI"
access_token_secret = "zboaMf9FyQPW6PwzLVLmSUzE1EzOPog3vHsPEncYtOnyN"
consumer_key = "dmVWx8zQHcoFFtPL715VK9Ros"
consumer_secret = "5YIRLpxx3M0KJMub5QtV7y7414fvxh65fNzm2ah1qizHuEWFvj"


#This is a basic listener that just prints received tweets to stdout.
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
    stream.filter(track=['ipl', '2016', 'win'])

