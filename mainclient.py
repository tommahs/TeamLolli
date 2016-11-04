def definedate():
    '''get current date/time'''
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def sendtofile(newlst):
    '''Write a list to a file'''
    import general_functions
    general_functions.csv_writelist('clients', 'clients', newlst, 1)


from tkinter import *

def clientmain(msg):
    '''Main window for the client.
    - Ask for userinput
    - Defines current station's abbreviation
    - Combines userinput with the clientslist
    - Write to clients.csv
    - Clears both inputboxes'''
    import general_functions
    station = 'Utrecht'  # input
    station = general_functions.stationabbreviation(station)
    client = Tk()
    client.config(bg='#FFCC18')
    client.wm_title(msg)
    label_titel = Label(client, text='Please enter your feedback about NS below & press Send.')
    label_titel.config(font=('Helvetica', 24), bg='#FFCC18')
    label_titel.grid(row=0, columnspan=12, sticky='n')

    label_2 = Label(client, text='Name : ', bg='#FFCC18')
    label_2.config(font=('Helvetica', 24))
    label_2.grid(row=1, column=2, sticky='ne')

    label_3 = Label(client, text='Message : ', bg='#FFCC18')
    label_3.config(font=('Helvetica', 24))
    label_3.grid(row=2, column=2, sticky='ne')

    entry_naam = Entry(client, bg='#e6e6e6', borderwidth=4)
    entry_naam.config(font=('Helvetica', 20), width=40)
    entry_naam.grid(row=1, column=3, columnspan=4, sticky='nw')
    entry_naam.focus_force()
    entry_message = Entry(client, bg='#e6e6e6', borderwidth=4)
    entry_message.config(font=('Helvetica', 18))
    entry_message.grid(row=2, column=3, columnspan=6, sticky='ew')

    svar_date = definedate()
    svar_station = station
    def getdata(date, station):
        '''get data from entry & check if the data is valid'''
        name = entry_naam.get()
        msg = entry_message.get()
        maxlength = (len(msg) + len(name))
        lst = [name, msg, date, station]
        if maxlength <= 125:
            sendtofile(lst)
        entry_message.delete(0, END)
        entry_naam.delete(0, END)
        entry_naam.focus_force()


    send = lambda: getdata(svar_date, svar_station)

    button_cancel = Button(client, text="Cancel", bg='Red', command=client.destroy)
    button_send = Button(client, text='Send', bg="Green", command=send)

    button_cancel.config(font=('Helvetica', 32))
    button_cancel.grid(row=10, column=2)
    button_send.config(font=('Helvetica', 32))
    button_send.grid(row=10, column=7)
    client.mainloop()
