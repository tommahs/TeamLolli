from authenticator import oauth
from general_functions import csv_read, csv_write


def adminrequest(file_to_send):
    print(csv_read(file_to_send))
    counter = 0
    while counter == 0:
        try:
            admin_answer = input('Input answer Accept/Decline : ')
            station = input('Input station where was message posted - ')
            # counter += 1
            if admin_answer == 'Accept':
                 r = oauth.request('statuses/update', {'status': filecsv.csv}) # content_csv, here goes file
                 if r.status_code == 200:
                     print('Succesfully sent message to twitterAPI')
                     counter += 1
                     continue
                 else:
                     print('An error has occured while sending message to twitterAPI please try again')
                     print(r)
                     continue
            elif admin_answer == 'Decline':
                try:
                    csv_write(filecsv.csv, oldlist, newlist) # content_csv, here goes file
                    print('Written data to log file!')
                    continue
                except:
                    print('Could not write to log file!')
                    continue



                ## Trying to tweet something, dont use this one yet for this is later used
        except:
            print('Something has gone wrong, please try again')
            continue



