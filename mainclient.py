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
    print(newlst)

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
# from tkinter.scrolledtext import ScrolledText


def clientmain(msg):
    import general_functions
    station = 'Utrecht'  # input
    station = general_functions.stationabbreviation(station)
    client = Tk()
    client.config(bg='#FFCC18')
    client.wm_title(msg)
    label_titel = Label(client, text='Please enter your feedback about NS below & press Send.')
    label_titel.config(font=('times', 24), bg='#FFCC18')
    label_titel.grid(row=0, columnspan=12, sticky='n')

    label_2 = Label(client, text='Naam : ', bg='#FFCC18')
    label_2.config(font=('times', 24))
    label_2.grid(row=1, column=2, sticky='ne')

    label_3 = Label(client, text='Bericht : ', bg='#FFCC18')
    label_3.config(font=('times', 24))
    label_3.grid(row=2, column=2, sticky='ne')

    entry_naam = Entry(client, bg='#e6e6e6', borderwidth=4)
    entry_naam.config(font=('times', 20), width=40)
    entry_naam.grid(row=1, column=3, columnspan=4, sticky='nw')
    entry_naam.focus_force()
    entry_message = Entry(client, bg='#e6e6e6', borderwidth=4)
    entry_message.config(font=('times', 18))
    entry_message.grid(row=2, column=3, columnspan=6, sticky='ew')

    svar_date = definedate()
    svar_station = station
    def getdata(date, station):
        name = entry_naam.get()
        print('name:', name)
        msg = entry_message.get()
        print('msg:', msg)
        maxlength = (len(msg) + len(name))
        lst = [name, msg, date, station]
        if maxlength <= 125:
            print("error")
            sendtofile(lst)
        entry_message.delete(0, END)
        entry_naam.delete(0, END)
        entry_naam.focus_force()


    send = lambda: getdata(svar_date, svar_station)

    button_cancel = Button(client, text="Cancel", bg='Red', command=client.destroy)
    button_send = Button(client, text='Verstuur', bg="Green", command=send)

    button_cancel.config(font=('times', 32))
    button_cancel.grid(row=10, column=2)
    button_send.config(font=('times', 32))
    button_send.grid(row=10, column=7)
    client.mainloop()