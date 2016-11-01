######
# Main Client file.
#
###

# Twitter max characters = 140
def userinput():
    global fname, lname, text, date
    from general_functions import inputquestion
    try:
        fname = inputquestion('First name')
        if fname == 'einde':
            loop = 0
        else:
            lname = inputquestion('Last name')
            text = inputquestion('tweet')
            date = definedate()
    except TypeError:
        loop = 0


def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def send():
    global usercount

def inputwritecsv(fname, lname, text, date):
    import csv
    with open('clients.csv', 'w', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(('firstname', 'lastname', 'text', 'date'))
        line1 = (fname, lname, text, date)
        writer.writerow(line1)
    print("Write succesfull!")

def checkdifferences():
    from general_functions import csv_read, csv_write
    clientcontent = csv_read('clients.csv')
    admincontent = csv_read('ReadyForAck.csv')
    for each in clientcontent:
        if each not in admincontent:
            csv_write(ReadyForAck.csv)



def clientmenu():
    global clientcounter
    clientcounter = 0
    clientmenuloop = 0
    while clientmenuloop == 0:
        userinput()
        inputwritecsv(fname, lname, text, date)
        clientcounter +=1


clientmenu()