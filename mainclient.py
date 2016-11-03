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


def sendtofile(newlst):
    import general_functions
    general_functions.csv_writelist('clients', 'clients', newlst, 1)
    print('Clicked on Send!')

# Functie beoordeel zorgt voor een output van True of False, aan de hand daarvan if, else statement maken.
# def beoordeel(newlst):
#         send(newlst)
#     if goedgekeurd == True:
#         send(newlst)
#         print('Bedankt!')
#     elif goedgekeurd is False:
#         message = entry_message.get(1.0, END)
#         return message
######
# Client menu
# Loops
# Asks for user input
# Defines current stations abbriviation
# Combine the userinput into the client list from csv
# Writes clientlist to csv
# Print DONE
####
from tkinter import *
from tkinter.scrolledtext import ScrolledText
def clientmain(msg):
    import general_functions
    station = 'Utrecht'  # input
    station = general_functions.stationabbreviation(station)
    client = Tk()
    client.wm_title(msg)

    label_titel = Label(client, text='Client', bg='#FFCC18')
    label_titel.config(font=('times', 24))
    label_titel.grid(row=0, columnspan=12, sticky='n')

    label_2 = Label(client, text='Naam : ', bg='#FFCC18')
    label_2.config(font=('times', 24))
    label_2.grid(row=1, column=2, sticky='ne')

    label_3 = Label(client, text='Bericht : ', bg='#FFCC18')
    label_3.config(font=('times', 24))
    label_3.grid(row=2, column=2, sticky='ne')

    svar_naam = 'testgui'
    entry_naam = Entry(client, bg='#e6e6e6', borderwidth=4)
    entry_naam.config(font=('times', 20), width=40)
    entry_naam.grid(row=1, column=3, columnspan=4, sticky='nw')
    entry_naam.insert(INSERT, '')

    entry_message = ScrolledText(client, width=40, height=4, bg='#e6e6e6')
    entry_message.config(font=('times', 18))
    entry_message.grid(row=2, column=3, columnspan=6, sticky='ew')
    entry_message.insert(INSERT, '')

    # svar_naam = entry_naam.get(1.0, END)
    svar_bericht = entry_message.get(1.0, END)
    svar_date = definedate()
    svar_station = station
    newlst = [svar_naam, svar_bericht, svar_date, svar_station]
    print(newlst)

    send = lambda: sendtofile(newlst)

    button_cancel = Button(client, text="Cancel", bg='Red', command=client.destroy)
    button_send = Button(client, text='Verstuur', bg="Green", command=send)

    button_cancel.config(font=('times', 32))
    button_cancel.grid(row=10, column=2)
    button_send.config(font=('times', 32))
    button_send.grid(row=10, column=7)
    client.mainloop()