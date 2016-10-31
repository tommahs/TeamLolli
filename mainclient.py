######
# Main Client file.
#
###

# Twitter max characters = 140

#function for asking the firstname
def inputfirstnameclient():
    firstname = input("Firstname : ")
    return firstname
#function for asking the lastname
def inputlastnameclient():
    lastname = input("Lastname : ")
    return lastname
def inputmessage():
    text = input("Write your text below:\n")
    return text
def mainclient():



    print("{} {}: {}".format(firstname, lastname, text))
# mainclient()

def inputwritecsv():
    from datetime import datetime
    import csv
    with open('clients.csv', 'w', newline='') as csvfile:
        # reader = csv.reader(csvfile.csv, delimiter=';')
        writer = csv.writer(csvfile, delimiter=';')
        # writer.writerow(('firstname', 'lastname', 'text', 'date'))
        loop = 1
        while loop == 1:
            try:
                firstname = inputfirstnameclient()
                if firstname == 'einde':
                    break
                lastname = inputlastnameclient()
                text = inputmessage()
                date = datetime.time
                writer.writerow((firstname, lastname, text, date))
            except TypeError:
                loop = 0
inputwritecsv()

