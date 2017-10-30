import twitter
import json
from prettytable import PrettyTable
from collections import Counter
CONSUMER_KEY = 'dmVWx8zQHcoFFtPL715VK9Ros'
CONSUMER_SECRET = '5YIRLpxx3M0KJMub5QtV7y7414fvxh65fNzm2ah1qizHuEWFvj'
OAUTH_TOKEN = '784597229554262016-90jngCQnPRFVWkxE6JpYqWn8I9fkeMI'
OAUTH_TOKEN_SECRET = 'zboaMf9FyQPW6PwzLVLmSUzE1EzOPog3vHsPEncYtOnyN'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
q = '#mumbaiindians' 

count = 1000000

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]
# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print pt
