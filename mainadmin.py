from authenticator import oauth
from general_functions import csv_read, csv_writelist

def updatelist():
    from general_functions import csv_read, csv_writelist
    csv_writelist('ReadyForAck','ReadyForAck', 'clients', 2)
    pending = csv_read('ReadyForAck.csv')
    return pending

def adminmenu():
    import general_functions
    station = 'stationtest.csv'
    accepted = 'accepted.csv'
    station_old = 'stationtest_old.csv'
    accepted_old = 'accepted_old.csv'
    counter = 0
    while counter == 0:
        Tweets = updatelist()
        for eachtweet in Tweets:  # eachtweet 0 = naam, 1 is bericht, 2 is datum, 3 is stationafkorting
            print(eachtweet)
            admin_answer = input('Accept message? Accept/Decline, \nType refresh if no message printed : ')
            if admin_answer == '0': # Accepted
                try:
                    ##
                    tweet = '{} {}: {} #{}'.format(eachtweet[2], eachtweet[0], eachtweet[1], eachtweet[3].upper())
                    print(tweet)
                except:
                    print('ietsgaatfout')
            elif admin_answer == '1':    #(Rejected)
                try:
                    # write to logfile
                    # remove tweet from ReadyForAck
                    general_functions.csv_writelist('logfile', 'logfile', eachtweet, 1)
                    general_functions.csv_writelist('ReadyForAck', 'ReadyForAck', 'logfile', 3)
                except:
                    "ietsgaatfout"
adminmenu()
