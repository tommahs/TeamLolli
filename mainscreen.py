from authenticator import oauth


screenlist = []

# Creating empty list for function

def showmainscreen(amount_of_messages):
    r = oauth.request('statuses/user_timeline', {'count': amount_of_messages,'screen_name' : 'MarijnBecking'})
    for item in r.get_iterator():
        if 'id_str' in item:
            s1 = item['text']
            s2 = item['created_at']
            station = item['entities']['hashtags']
            for d in station:
                s3 = d['text']
            screenlist.append([s1,s2,s3])
            continue
    return screenlist

# Function to search twitter and form information into the format for the screen inside the station
# Made into a function for later use

# #stationnaam meegeven



