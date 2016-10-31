from authenticator import oauth

r = oauth.request('statuses/user_timeline', {'count': 2,'screen_name' : 'MarijnBecking'})
def requestadmin(status):
    for item in r.get_iterator():
        if 'text' in item:
            message = item['text']
            date_created_message = item['created_at']

