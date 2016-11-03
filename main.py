from tkinter import *
from tkinter.scrolledtext import ScrolledText


#Functie beoordeel zorgt voor een output van True of False, aan de hand daarvan if, else statement maken.

def beoordeel(goedgekeurd):
    import mainadmin
    print(goedgekeurd)
    if goedgekeurd == 'quit':
        exit()
    elif goedgekeurd == 'Client':
        # mainclient.clientmenu()
        clientmain('Client')
    elif goedgekeurd == 'check':
        mainadmin.tweetAck()

def clientmain(msg):
    client = Tk()
    client.wm_title(msg)

    send = lambda: beoordeel(True, newlst)
    button_cancel = Button(client, text="Cancel", bg='Red', command=client.destroy)
    button_send = Button(client, text='Verstuur', bg="Green")  # , command=send)

    button_cancel.config(font=('times', 32))
    button_cancel.grid(row=10, column=2)
    button_send.config(font=('times', 32))
    button_send.grid(row=10, column=7)
    svar_naam = StringVar(client, value='voorbeeld naam')

    # background_image = PhotoImage(file="GUI/NS_logo2.png")
    # background_label = Label(client, image=background_image)
    # background_label.grid(rowspan=30, columnspan=12)
    # client.resizable(False, False)

    label_titel = Label(client, text='NS bericht approval', bg='#FFCC18')
    label_titel.config(font=('times', 24))
    label_titel.grid(row=0, columnspan=12, sticky='n')

    label_2 = Label(client, text='Naam : ', bg='#FFCC18')
    label_2.config(font=('times', 24))
    label_2.grid(row=1, column=2, sticky='ne')

    label_3 = Label(client, text='Bericht : ', bg='#FFCC18')
    label_3.config(font=('times', 24))
    label_3.grid(row=2, column=2, sticky='ne')

    entry_naam = Entry(client, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
    entry_naam.config(font=('times', 20), width=40)
    entry_naam.grid(row=1, column=3, columnspan=4, sticky='nw')

    entry_message = ScrolledText(client, width=40, height=4, bg='#e6e6e6')
    entry_message.config(font=('times', 18))
    entry_message.grid(row=2, column=3, columnspan=6, sticky='ew')
    entry_message.insert(INSERT, '')

    svar_bericht = entry_message.get(1.0, END)

    svar_date = definedate()
    svar_station = station
    newlst = [svar_naam, svar_bericht, svar_date, svar_station]
    print(newlst)


    client.mainloop()

root = Tk()
root.title('NS Approval App')

background_image = PhotoImage(file="GUI/NS_logo.png")
background_label = Label(root, image=background_image)
background_label.grid(rowspan=30, columnspan=12)
root.resizable(False, False)

label_titel = Label(root, text='Main Menu', bg='#FFCC18')
label_titel.config(font=('times', 24))
label_titel.grid(row=0, columnspan=12, sticky='n')

client = lambda:beoordeel('Client')
check = lambda:beoordeel('Check Tweet')
quit = lambda:beoordeel('quit')

button_client = Button(root, text='client', bg="red", font=('times', 32), command=client)
button_check = Button(root, text='checktweets', bg="Green",font=('times', 32), command=check)
button_quit = Button(root, text='Quit program', bg='Green', font=('times', 32), command=quit)

button_client.grid(row=1, column=2)
button_check.grid(row= 2, column=2)
button_quit.grid(row=3, column=2)
root.mainloop()
