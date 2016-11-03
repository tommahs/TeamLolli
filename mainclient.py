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

# def userinput(station):
#     from general_functions import inputquestion
#     try:
#         fname = inputquestion('First name') #Check length, 10 characters max
#         if len(fname) > 10:
#             print('Name is too long')
#             userinputlst = 1
#             return userinputlst
#         else:
#             text = inputquestion('Tweet') #Check length, 120 char max
#             if len(text) > 120:
#                 print('Text is too long')
#                 userinputlst = 2
#                 return userinputlst
#             date = definedate()
#             userinputlst = [fname, text, date, station]
#             return userinputlst
#     except TypeError:
#         print('Something has gone wrong, please try again')


def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def send(newlst):
    import general_functions
    # general_functions.csv_writelist('clients', 'clients', newlst, 1)
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
from tkinter import *
from tkinter.scrolledtext import ScrolledText
def clientmenu():
    import general_functions
    station = 'Utrecht' #input
    clientmenuloop = 0
    station = general_functions.stationabbreviation(station)
    while clientmenuloop == 0:
        afsluiten = False
        root = Tk()
        root.title('NS Reizigers mening')

        svar_naam = StringVar(root, value='voorbeeld naam')

        # Functie beoordeel zorgt voor een output van True of False, aan de hand daarvan if, else statement maken.


        def beoordeel(goedgekeurd, newlst):
            print(entry_message.get(1.0, END))
            if goedgekeurd == True:
                send(newlst)
                print('Bedankt!')
            elif goedgekeurd == False:
                print('Koen zuigt')
        background_image = PhotoImage(file="GUI/NS_logo.png")
        background_label = Label(root, image=background_image)
        background_label.grid(rowspan=30, columnspan=12)
        root.resizable(False, False)

        label_titel = Label(root, text='NS bericht approval', bg='#FFCC18')
        label_titel.config(font=('times', 24))
        label_titel.grid(row=0, columnspan=12, sticky='n')

        label_2 = Label(root, text='Naam : ', bg='#FFCC18')
        label_2.config(font=('times', 24))
        label_2.grid(row=1, column=2, sticky='ne')

        label_3 = Label(root, text='Bericht : ', bg='#FFCC18')
        label_3.config(font=('times', 24))
        label_3.grid(row=2, column=2, sticky='ne')

        entry_naam = Entry(root, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
        entry_naam.config(font=('times', 20), width=40)
        entry_naam.grid(row=1, column=3, columnspan=4, sticky='nw')

        entry_message = ScrolledText(root, width=40, height=4, bg='#e6e6e6')
        entry_message.config(font=('times', 18))
        entry_message.grid(row=2, column=3, columnspan=6, sticky='ew')
        entry_message.insert(INSERT, '')

        svar_bericht = entry_message.get(1.0, END)

        svar_date = definedate()
        svar_station = station
        newlst = [svar_naam, svar_bericht, svar_date, svar_station]
        print(newlst)

        cancel = lambda: beoordeel(False, newlst)
        send = lambda: send(newlst)

        button_cancel = Button(root, text='Cancel', bg="red", command=cancel)
        button_send = Button(root, text='Verstuur', bg="Green", command=send)

        button_cancel.config(font=('times', 32))
        button_cancel.grid(row=11, column=1)

        button_send.config(font=('times', 32))
        button_send.grid(row=11, column=10)
        root.mainloop()
        # if newlst == '1':
        #     print('Name is too long')
        #     clientmenuloop = 1
        # elif newlst == '2':
        #     print('Text is too long')
        #     clientmenuloop = 1
        # else:
        #     send(newlst)
        #     general_functions.popuptext('Thank you for giving us valuable feedback to work with!')
        #     clientmenuloop = 1
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