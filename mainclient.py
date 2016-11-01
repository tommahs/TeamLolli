######
# Main Client file.
# 1. Ask input from user, add tweetcounter + location
# 2. Write to csv file
# 3. Check if
###

# Twitter max characters = 140
#
######
# Asking user input
####
def userinput():
    global fname, lname, text, date
    from general_functions import inputquestion
    # error = 0
    # while error == 0:
    try:
        fname = inputquestion('First name') #Check length, 10 characters max
        if len(fname) > 10:
            print('Name is too long')
            # Error system needed
        text = inputquestion('Tweet') #Check length, 120 char max
        if len(text) > 120:
            print('Text is too long')
        # Error system needed
        date = definedate()
    except TypeError:
        print('Something has gone wrong, please try again')



def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def send():
    print('Send')

def inputwritecsv(fname, text, date):
    import csv
    with open('clients.csv', 'w', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(('firstname', 'text', 'date'))
        line1 = (fname, text, date)
        writer.writerow(line1)
    print("Write succesfull!")
    csvfile.close()

def clientmenu():
    global clientcounter
    clientcounter = 0
    clientmenuloop = 0
    while clientmenuloop == 0:
        userinput()
        inputwritecsv(fname, text, date)
        clientcounter +=1


# clientmenu()