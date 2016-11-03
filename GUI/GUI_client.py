from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('NS Reizigers mening')


svar_naam = StringVar(root, value='voorbeeld naam')


def toont_weet(naam, bericht):
    svar_bericht.set(bericht)
    svar_naam.set(naam)

#Functie beoordeel zorgt voor een output van True of False, aan de hand daarvan if, else statement maken.


def beoordeel(goedgekeurd):
    print(entry_message.get(1.0,END))


background_image = PhotoImage(file="NS_logo.png")
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
entry_message.grid( row=2, column=3, columnspan=6, sticky='ew')
entry_message.insert(INSERT,'')

svar_bericht = entry_message.get(1.0,END)


reject = lambda:beoordeel(False)
accept = lambda:beoordeel(True)

button_reject = Button(root, text='Cancel', bg="red", command=reject)
button_accept = Button(root, text='Verstuur', bg="Green", command=accept)


button_reject.config(font=('times', 32))
button_reject.grid(row=11, column=1)

button_accept.config(font=('times', 32))
button_accept.grid(row=11, column=10)

root.mainloop()
