try:
    import json
except ImportError:
    import simplejson as json

from TwitterAPI import TwitterAPI

# Variables that contains the user credentials to access Twitter API
consumer_key = '4y80L7AkxgHOUWgmxCmtmsa5H'
consumer_secret = 'vJqX4rfOzI0xUviCzTZvacVmAjRGINdSFQlrmFuHydWdAHj29w'
access_token_key = '751746308-MhnwFjcA1xkdgf0FTsDmbfiF0Bjv89ZEzhqrnDH6'
access_token_secret = 'OXm1d9oAqSuO4FEjqZR4kwOy4gJITJEWGxCsM5K6vIw1o'

oauth = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret )

# Requesting tweets from specific user: !! https://twitter.com/MarijnBecking
r = oauth.request('statuses/user_timeline', {'count':2,'screen_name':'MarijnBecking'})
for item in r.get_iterator():
    if 'text' in item:
        print (item['text'])

## Trying to tweet something, dont use this one yet for this is later used
## r = oauth.request('statuses/update', {'status': 'simple tweet'})
## print('SUCCES' if r.status_code == 200 else 'FAILURE')

# # Getting 50 recent tweets
# r = oauth.request('statuses/home_timeline', {'count':50})
# for item in r.get_iterator():
#     if 'text' in item:
#         print (item['text'])

