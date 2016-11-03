from tkinter import *
from mainscreen import showmainscreen

# Starting Root-Window
RWindow = Tk()
RWindow.geometry('350x480')

###################

# Idee is het mogelijk om  de format van de message in een functie te zetten
# En dat de functie de format gebruikt om verschillende messages te platens?

###################


# Label naam en Test Bericht
svar_bericht = StringVar(RWindow, value='Het Bericht')
svar_labelNaam = StringVar(RWindow, value='Title "Berichten"')
svar_naam = StringVar(RWindow, value='Naam Persoon')



# Functie om alles in te laden?             ## bericht == list of messages
def toont_weet(naam, bericht,lblnaam):
    svar_bericht.set(bericht)
    svar_labelNaam.set(lblnaam)
    svar_naam.set(naam)

def showtweetsonscreen(amountofmessages):
    counter = 0
    newlist = showmainscreen(amountofmessages)
    lst = []
    while True:
        for each in newlist:
            if counter >= 0 and counter < len(newlist):
                name = newlist[0][1]
                message = newlist[counter][0]
                lst.append(message)
                counter += 1
        break

    while True:
        if len(lst) < 9:
            lst.append(' ')
        else:
            break


    # Label Naam
    label_naam = Message(RWindow, textvariable=svar_labelNaam, bg='#e6e6e6', borderwidth=4)
    label_naam.config(font=('times', 16), width=400)
    label_naam.grid(row=1, column=3, columnspan=4, sticky='n', ipadx='100', ipady='10')
    def looping(listofmessages):

        # Bericht 1

        label_message1 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[0]), bg='#e6e6e6')
        label_message1.config(font=('times', 12), width=400)
        label_message1.grid(row=3, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 2

        label_message2 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[1]), bg='#e6e6e6')
        label_message2.config(font=('times', 12), width=400)
        label_message2.grid(row=5, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 3

        label_message3 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[2]), bg='#e6e6e6')
        label_message3.config(font=('times', 12), width=400)
        label_message3.grid(row=7, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 4

        label_message4 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[3]), bg='#e6e6e6')
        label_message4.config(font=('times', 12), width=400)
        label_message4.grid(row=9, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 5
        label_message5 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[4]), bg='#e6e6e6')
        label_message5.config(font=('times', 12), width=400)
        label_message5.grid(row=6, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 6
        label_message6 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[5]), bg='#e6e6e6')
        label_message6.config(font=('times', 12), width=400)
        label_message6.grid(row=7, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 7
        label_message7 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[6]), bg='#e6e6e6')
        label_message7.config(font=('times', 12), width=400)
        label_message7.grid(row=8, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 8
        label_message8 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[7]), bg='#e6e6e6')
        label_message8.config(font=('times', 12), width=400)
        label_message8.grid(row=9, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

        # Bericht 9
        label_message9 = Message(RWindow, textvariable = StringVar(RWindow, value=listofmessages[8]), bg='#e6e6e6')
        label_message9.config(font=('times', 12), width=400)
        label_message9.grid(row=10, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

    looping(lst)
    mainloop()


# def startlooping():
showtweetsonscreen(5)
