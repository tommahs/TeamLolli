from tkinter import *

# Starting Root-Window
RWindow = Tk()
RWindow.geometry('300x480')

###################

# Idee is het mogelijk om  de format van de message in een functie te zetten
# En dat de functie de format gebruikt om verschillende messages te platens?

###################

# Label naam en Test Bericht
svar_bericht = StringVar(RWindow, value='kut')
svar_naam = StringVar(RWindow, value='Berichten')

# Functie om alles in te laden?
def toont_weet(naam, bericht):
    svar_bericht.set(bericht)
    svar_naam.set(naam)



# Label Naam
label_naam = Message(RWindow, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
label_naam.config(font=('times', 16), width=400)
label_naam.grid(row=1, column=3, columnspan=4, sticky='n', ipadx='100', ipady='10')

# Bericht 1
label_message = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message.config(font=('times', 12), width=400)
label_message.grid(row=2, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 2
label_message2 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message2.config(font=('times', 12), width=400)
label_message2.grid(row=3, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 3
label_message3 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message3.config(font=('times', 12), width=400)
label_message3.grid(row=4, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 4
label_message4 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message4.config(font=('times', 12), width=400)
label_message4.grid(row=5, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 5
label_message5 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message5.config(font=('times', 12), width=400)
label_message5.grid(row=6, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 6
label_message6 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message6.config(font=('times', 12), width=400)
label_message6.grid(row=7, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 7
label_message7 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message7.config(font=('times', 12), width=400)
label_message7.grid(row=8, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 8
label_message8 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message8.config(font=('times', 12), width=400)
label_message8.grid(row=9, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 9
label_message9 = Message(RWindow, textvariable = svar_bericht, bg='#e6e6e6')
label_message9.config(font=('times', 12), width=400)
label_message9.grid(row=10, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

mainloop()