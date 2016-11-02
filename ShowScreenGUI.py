from tkinter import *

# Starting

master = Tk()
master.geometry('300x500')


svar_bericht = StringVar(master, value='kut')
svar_naam = StringVar(master, value='Berichten')


def toont_weet(naam, bericht):
    svar_bericht.set(bericht)
    svar_naam.set(naam)




label_naam = Message(master, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
label_naam.config(font=('times', 16), width=400)
label_naam.grid(row=1, column=3, columnspan=4, sticky='nw')

label_message = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message.grid(row=2, column=3, columnspan=6,  sticky='ew')
label_message.config(font=('times', 12), width=400)

mainloop()