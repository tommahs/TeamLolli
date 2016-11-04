from tkinter import *
from mainscreen import showmainscreen
import tkinter
import sched, time




# Starting Root-Window
RWindow = Tk()
RWindow.geometry('600x1065')

###################

# Idee is het mogelijk om  de format van de message in een functie te zetten
# En dat de functie de format gebruikt om verschillende messages te platens?

###################


# Label naam en Test Bericht
svar_bericht = StringVar(RWindow, value='Het Bericht')
svar_labelNaam = StringVar(RWindow, value='NS TWITTER')
svar_naam = StringVar(RWindow, value='Naam Persoon')



# Functie om alles in te laden?             ## bericht == list of messages
def toont_weet(naam, bericht,lblnaam):
    svar_bericht.set(bericht)
    svar_labelNaam.set(lblnaam)
    svar_naam.set(naam)

def createlist():
    counter = 0
    lst = []
    newlist = showmainscreen(9)
    while True:
        for each in newlist:
            if counter >= 0 and counter < len(newlist):

                message = newlist[counter][0]
                lst.append(message)
                counter += 1
        break

    while True:
        if len(lst) < 10:
            lst.append(' ')
        else:
            break
    return lst


    # Label Naam

background_image = PhotoImage(file="bg_image.png")
background_label = Label(RWindow, image=background_image)
background_label.grid(rowspan=30, columnspan=12)


label_naam = Message(RWindow, textvariable=svar_labelNaam, bg='white', borderwidth=5)
label_naam.config(font=('times', 16), width=100)
label_naam.grid(row=2, column=4, columnspan=10, sticky='n', ipadx='250', ipady='10',)

listofmessages = createlist()

        # Bericht 1

label_message1 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[0]), bg='#62C8FF')
label_message1.config(font=('times', 12), width=400,anchor='w')
label_message1.grid(row=3, column=1, columnspan=20,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 2
label_message2 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[1]), bg='#D3D127')
label_message2.config(font=('times', 12), width=400,anchor='w')
label_message2.grid(row=4, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 3
label_message3 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[2]), bg='#62C8FF')
label_message3.config(font=('times', 12), width=400,anchor='w')
label_message3.grid(row=5, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 4
label_message4 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[3]), bg='#D3D127')
label_message4.config(font=('times', 12), width=400,anchor='w')
label_message4.grid(row=6, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # # Bericht 5
label_message5 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[4]), bg='#62C8FF')
label_message5.config(font=('times', 12), width=400,anchor='w')
label_message5.grid(row=7, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 6
label_message6 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[5]), bg='#D3D127')
label_message6.config(font=('times', 12), width=400,anchor='w')
label_message6.grid(row=8, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 7
label_message7 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[6]), bg='#62C8FF')
label_message7.config(font=('times', 12), width=400,anchor='w')
label_message7.grid(row=9, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 8
label_message8 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[7]), bg='#D3D127')
label_message8.config(font=('times', 12), width=400,anchor='w')
label_message8.grid(row=10, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 9
label_message9 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[8]), bg='#62C8FF')
label_message9.config(font=('times', 12), width=400,anchor='w')
label_message9.grid(row=11, column=3, columnspan=10,  sticky='ew', ipadx='100', ipady='10')


def loop():
    listofmessages1 = createlist()
    label_message1.config(textvariable=StringVar(RWindow, value=listofmessages1[0]))
    label_message2.config(textvariable=StringVar(RWindow, value=listofmessages1[1]))
    label_message3.config(textvariable=StringVar(RWindow, value=listofmessages1[2]))
    label_message4.config(textvariable=StringVar(RWindow, value=listofmessages1[3]))
    label_message5.config(textvariable=StringVar(RWindow, value=listofmessages1[4]))
    label_message6.config(textvariable=StringVar(RWindow, value=listofmessages1[5]))
    label_message7.config(textvariable=StringVar(RWindow, value=listofmessages1[6]))
    label_message8.config(textvariable=StringVar(RWindow, value=listofmessages1[7]))
    label_message9.config(textvariable=StringVar(RWindow, value=listofmessages1[8]))
    RWindow.after(5000,loop)


RWindow.after(8000, loop)
RWindow.mainloop()
