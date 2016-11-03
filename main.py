from tkinter import *
from tkinter.scrolledtext import ScrolledText


#Functie beoordeel zorgt voor een output van True of False, aan de hand daarvan if, else statement maken.

def beoordeel(goedgekeurd):
    import mainadmin, mainclient
    print(goedgekeurd)
    if goedgekeurd == 'quit':
        exit()
    elif goedgekeurd == 'Client':
        mainclient.clientmain('Client')
    elif goedgekeurd == 'check':
        mainadmin.tweetAck()



root = Tk()
root.title('NS Feedback Poster')

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
