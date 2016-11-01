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



mainadmin()