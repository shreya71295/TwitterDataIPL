'''
Twitter Stream Listener
'''


# tweepy setup
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import os
import json


access_token = "3589614620-dIGIQzB8ZaM5yHJVSJG6VwC9Rt6GX052XEJpRSb"
access_token_secret = "xXI1g0gJvMTChrb96kMk1KkS2QG8536P84f8Y5oPh3jWJ"
consumer_key = "hRlUftiYjx7NIBPfPHfdzK1FC"
consumer_secret = "7DjRNP0HFYGY12C2S9SpoUEerPCiiDCFRcobJpSNRHWcvTt8kL"


#Listener Class Override
class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):

		saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

		while (time.time() - self.time) < self.limit:

			try:

				self.tweet_data.append(data)

				return True


			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()

	def on_error(self, status):

		print status

	def on_disconnect(self, notice):

		print 'bye'



#Beginning of the specific code
start_time = time.time() #grabs the system time

keyword_list = ['ipl','2016','win'] #track list


auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
auth.set_access_token(access_token, access_token_secret)


twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Listener


