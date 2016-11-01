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
    # error = 0
    # while error == 0:
    try:
        fname = inputquestion('First name') #Check length, 10 characters max
        if len(fname) > 10:
            print('Name is too long')
            # Error system needed
        else:
            text = inputquestion('Tweet') #Check length, 120 char max
            if len(text) > 120:
                print('Text is too long')
            # Error system needed
            date = definedate()
            userinputlst = [fname, text, date, station]
            return userinputlst
    except TypeError:
        print('Something has gone wrong, please try again')




def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def send():
    input('Clicked on Send!')

######
# client menu
# loops
# asks for user input
# combine the userinput into the client list from csv
# writes clientlist to csv
# print DONE
####
def clientmenu():
    import general_functions
    station = 'Utrecht'
    clientmenuloop = 0
    station = general_functions.stationabbreviation(station)
    while clientmenuloop == 0:
        newlst = userinput(station)
        general_functions.csv_writelist('clients', 'clients', newlst)
        send()
clientmenu()

