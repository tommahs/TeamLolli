######
# Main Client file.
# 1. Ask input from user, add tweetcounter + location
# 2. Write to csv file
# 3. Check if
###

# Twitter max characters = 140

######
# Asking user input
####

def userinput(station):
    from general_functions import inputquestion
    try:
        fname = inputquestion('First name') #Check length, 10 characters max
        if len(fname) > 10:
            print('Name is too long')
            userinputlst = 1
            return userinputlst
        else:
            text = inputquestion('Tweet') #Check length, 120 char max
            if len(text) > 120:
                print('Text is too long')
                userinputlst = 2
                return userinputlst
            date = definedate()
            userinputlst = [fname, text, date, station]
            return userinputlst
    except TypeError:
        print('Something has gone wrong, please try again')


def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def send(newlst):
    import general_functions
    general_functions.csv_writelist('clients', 'clients', newlst, 1)
    input('Clicked on Send!')

######
# client menu
# loops
# asks for user input
# Defines current stations abbriviation
# combine the userinput into the client list from csv
# writes clientlist to csv
# print DONE
####

def clientmenu():
    import general_functions
    station = 'Utrecht' #input
    clientmenuloop = 0
    station = general_functions.stationabbreviation(station)
    while clientmenuloop == 0:
        newlst = userinput(station)
        if newlst == '1':
            print('Name is too long')
            clientmenuloop = 1
        elif newlst == '2':
            print('Text is too long')
            clientmenuloop = 1
        else:
            send(newlst)
            general_functions.popuptext('Thank you for giving us valuable feedback to work with!')
            clientmenuloop = 1
clientmenu()


# # Test to write input into clients.csv
# from general_functions import *
#
# Test to add new tweet to clients.csv
# mainclient.clientmenu()
# Test to check to combine clients.csv and ReadyForAck.csv if clientsvalue not yet known voor
# csv_writelist('ReadyForAck','ReadyForAck', 'clients', 2)
# input()
# Test to remove values in logfile from ReadyForAck
# csv_writelist('ReadyForAck', 'ReadyForAck', 'logfile', 3)
# input()


# Logging