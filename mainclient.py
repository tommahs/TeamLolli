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
    loop = 1
    while loop == 1:
        with open('clients.csv', 'w', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(('firstname', 'lastname', 'text', 'date'))
            writer.writerow(fname, lname, text, date)
        print("Write succesfull!")
    return loop


def clientmenu():
    clientmenuloop = 0
    while clientmenuloop == 0:
        userinput()

        inputwritecsv(fname, lname, text, date)

clientmenu()
# import datetime
# date = datetime.datetime.now().strftime("20%y-%m-%d %H:%M")
# print(date)