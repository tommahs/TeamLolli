from authenticator import oauth
from general_functions import csv_read, csv_writelist

def updatelist():
    from general_functions import csv_read, csv_writelist
    clients = csv_read('clients.csv')
    for eachclient in clients:
        csv_writelist('ReadyForAck', 'ReadyForAck', eachclient)
    pending = csv_read('ReadyForAck.csv')
    return pending

def adminmenu():
    counter = 0
    while counter == 0:
        try:
            Tweets = updatelist()
            for eachtweet in Tweets:  # eachtweet 0 = naam, 1 is bericht, 2 is datum, 3 is tijd
                print(eachtweet[0], eachtweet[1], eachtweet[2], eachtweet[3])
                admin_answer = input('Accept message? Accept/Decline, \nType refresh if no message printed : ')
                confirmation = input('Are you sure? Yes/No')
                # station = input('Input station where was message posted - ')
                # counter += 1
                if admin_answer == 'Accept' and confirmation == 'Yes':
                     csv_writelist(acceptedfile, oldfile, newlst)            # WRITING TO ACCEPTED FILE
                     csv_writelist(station, oldfile, newlst)                 # REWRITING STATION FILE TO REMOVE MESSAGE
                     r = oauth.request('statuses/update', {'status': '!!!'}) # TWEETING CONTENT OF MESSAGE
                     if r.status_code == 200:
                         print('Succesfully sent message to twitterAPI')     # CONFIRMATION FOR ADMIN
                         continue
                     else:                                                   # IF AN ERROR OCCURS
                         print('An error has occured while sending message to twitterAPI please try again')
                         print('ERROR CODE : ', r)                           # ERROR CODE
                         continue
                elif admin_answer == 'Accept' and confirmation == 'No':
                    continue
                elif admin_answer == 'Decline' and confirmation == 'Yes':
                    try:
                        csv_writelist(station, oldfile, newlst)              # REWRITING REJECTED FILE TO ADD MESSAGE
                        print('Written data to log file!')
                        continue
                    except:
                        print('Could not write to log file!')
                        continue
                elif admin_answer == 'Decline' and confirmation == 'No':
                    continue
                elif admin_answer == 'Refresh':                              # REFRESHING LIST OF MESSAGES
                    counter += 1
                    continue
        except:
            print('Something has gone wrong, please try again')
            continue
adminmenu()