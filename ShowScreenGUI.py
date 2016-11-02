from tkinter import *

# Starting

master = Tk()
master.geometry('300x480')


svar_bericht = StringVar(master, value='kut')
svar_naam = StringVar(master, value='Berichten')


def toont_weet(naam, bericht):
    svar_bericht.set(bericht)
    svar_naam.set(naam)



# Label Naam
label_naam = Message(master, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
label_naam.config(font=('times', 16), width=400)
label_naam.grid(row=1, column=3, columnspan=4, sticky='n', ipadx='100', ipady='10')

# Bericht 1
label_message = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message.config(font=('times', 12), width=400)
label_message.grid(row=2, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 2
label_message2 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message2.config(font=('times', 12), width=400)
label_message2.grid(row=3, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 3
label_message3 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message3.config(font=('times', 12), width=400)
label_message3.grid(row=4, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 4
label_message4 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message4.config(font=('times', 12), width=400)
label_message4.grid(row=5, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 5
label_message5 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message5.config(font=('times', 12), width=400)
label_message5.grid(row=6, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 6
label_message6 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message6.config(font=('times', 12), width=400)
label_message6.grid(row=7, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 7
label_message7 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message7.config(font=('times', 12), width=400)
label_message7.grid(row=8, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 8
label_message8 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message8.config(font=('times', 12), width=400)
label_message8.grid(row=9, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

# Bericht 9
label_message9 = Message(master, textvariable = svar_bericht, bg='#e6e6e6')
label_message9.config(font=('times', 12), width=400)
label_message9.grid(row=10, column=3, columnspan=6,  sticky='ew', ipadx='100', ipady='10')

mainloop()