######
# Main.py is the program starting each process apart from eachother.
# mainclient.py, mainadmin.py and mainscreen.py can be run apart from eachother.
#
####


def updatelist():
    from general_functions import csv_read, csv_writelist
    clients = csv_read('clients.csv')
    for eachclient in clients:
        print(eachclient)
        csv_writelist('ReadyForAck', 'ReadyForAck', eachclient)
    pending = csv_read('ReadyForAck.csv')
    return pending

def mainadmin():
    loop = 1
    while loop == 1:
        Tweets = updatelist()
        for eachtweet in Tweets: #eachtweet 0 = naam, 1 is bericht, 2 is datum, 3 is tijd
            print(eachtweet[0], eachtweet[1], eachtweet[2], eachtweet[3])
        loop = 0

mainadmin()