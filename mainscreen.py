from authenticator import oauth

r = oauth.request('statuses/user_timeline', {'count': 2,'screen_name' : 'MarijnBecking'})
for item in r.get_iterator():
    if 'text' in item:
        print(item['text'])
