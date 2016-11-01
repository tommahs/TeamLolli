from authenticator import oauth


screenlist = []

# Creating empty list for function

def showmainscreen(amount_of_messages):
    r = oauth.request('statuses/user_timeline', {'count': amount_of_messages,'screen_name' : 'MarijnBecking'})
    for item in r.get_iterator():
        if 'id_str' in item:
            screenlist.append(item['text'])
            screenlist.append(item['created_at'])
            continue
    return screenlist

# Function to search twitter and form information into the format for the screen inside the station
# Made into a function for later use





