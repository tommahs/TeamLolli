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
# r = oauth.request('statuses/user_timeline', {'count': 2,'screen_name' : 'MarijnBecking'})
#
# for item in r.get_iterator():
#     if 'text' in item:
#         print(item['text']) #On top of the term item can be placed an term from within the dict by doing a: item['*specified element']
#
# print(r.text)

# From this we get an "dict line with every element"(json)

## Trying to tweet something, dont use this one yet for this is later used
station = 'utrecht'
r = oauth.request('statuses/update', {'status': 'simple tweet #NS'+ station})
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


### WORK IN PROGRESS
# str day month year, text
# counter for checking the tweet #
# customtweetcount = 0
# shortstation = 'UTR'
# tweetlst = []

# Optimalize the date, Sort each tweet in the corresponding dictionary for different regions
# for item in r.get_iterator():
#     customtweetcount +=1
#     monthdict = {'Jan': 1, 'Feb': 2, 'Mar': 3,
#                  'Apr': 4, 'May': 5, 'Jun': 6,
#                  'Jul': 7, 'Aug': 8, 'Sep': 9,
#                  'Oct': 10, 'Nov': 11, 'Dec': 12
#                  }
#     if 'text' in item:
#         datetime = item['created_at']
#         datelst = datetime.split(sep=' ')
#         day = int(datelst[2])
#         monthname = datelst[1]
#         monthnum = int(monthdict[monthname])
#         year = int(datelst[5])
#         time = datelst[3]
#         datelst = time, day, monthname, year
#         line1 = {'Tweetnum' : customtweetcount,
#                  'Year': year,
#                  'Month': monthnum,
#                  'Day': day,
#                  'Time': time,
#                  'Text': item['text'],
#                  'Hashtag' : shortstation
#                  }
#         tweetlst.append(line1)
# print(tweetlst)
