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

oauth = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# Requesting tweets from specific user: !! https://twitter.com/MarijnBecking
r = oauth.request('statuses/user_timeline', {'count': 2,'screen_name' : 'MarijnBecking'})

for item in r.get_iterator():
    if 'text' in item:
        print(item) #On top of the term item can be placed an term from within the dict by doing a: item['*specified element']



# From this we get an "dict line with every element"(json)

## Trying to tweet something, dont use this one yet for this is later used
## r = oauth.request('statuses/update', {'status': 'simple tweet'})
## print('SUCCES' if r.status_code == 200 else 'FAILURE')

# # Getting 50 recent tweets
# r = oauth.request('statuses/home_timeline', {'count':50})
# for item in r.get_iterator():
#     if item['text'] == 'tweet prog':
#         print(item)

     # if 'text' in item:
     #     print(item['text'])


#########
# Tom Test
# Reading tweets, sorting them based on the Hashtags


#####
# The following function reads the tweets, compares them to a value in a defined lst,
# and gives back the hashtag, text and date/time of creation
####
r = oauth.request('statuses/user_timeline', {'count': 50}) #define ammount of wanted data from twitter
tweets = []
hashtaglst = ['ZombieHype', 'ShinyThing'] # using a list for the hashtags
def tweetreader(lst):
    for item in r.get_iterator(): # Grab data from twitter
        entities = item['entities'] # Accessing the subdictionary
        hashtagslst = entities['hashtags'] # Is apparently a list of dictionaries
        if 'text' in item: #if there is text in an item :
            try: # Try/except to get rid of invalid data
                for eachhtdict in hashtagslst: # for each hashtagdict in hashtaglist
                    if eachhtdict['text'] in lst: # If the hashtag in dictionary['text] is in the list:
                        print('hashtag: #{} \ntext : {}'.format(eachhtdict['text'], item['text'])) # print the hashtag & text
                        print(item['created_at']) #print date/time of creation
            except: # If the try fails with an error, do the following:
                if IndexError: #if there isnt an hashtag in hashtags, it means that the list is empty, and gives an IndexError
                    continue # Continue the for-loop
tweetreader(hashtaglst)
# str day month year, text
# counter for checking the