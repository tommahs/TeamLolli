from tkinter import *


def beoordeel(goedgekeurd):
    """Beoordeeld wat er gedaan moet worden"""
    import mainadmin, mainclient, logfilegui
    if goedgekeurd == 'quit':
        exit()
    elif goedgekeurd == 'Client':
        mainclient.clientmain('Client')
    elif goedgekeurd == 'Check Tweet':
        mainadmin.tweetAck('NS Approval App')
    elif goedgekeurd == 'log':
        logfilegui.logmain()


def main():
    '''Main menu'''
    root = Tk()
    root.title('NS Feedback Poster')

    background_image = PhotoImage(file="GUI/NS_logo.png")
    background_label = Label(root, image=background_image)
    background_label.grid(rowspan=30, columnspan=12)
    root.resizable(False, False)

    label_titel = Label(root, text='Main Menu', bg='#FFCC18')
    label_titel.config(font=('Helvetica', 24))
    label_titel.grid(row=0, columnspan=12, sticky='n')

    client = lambda:beoordeel('Client')
    check = lambda:beoordeel('Check Tweet')
    quit = lambda:beoordeel('quit')
    log = lambda:beoordeel('log')

    button_client = Button(root, text='Make tweets', bg="green", font=('Helvetica', 30), command=client)
    button_check = Button(root, text='Acknowledge tweets', bg="Green",font=('Helvetica', 30), command=check)
    button_log = Button(root, text='View logfile', bg='Gray', font=('Helvetica', 30), command=log)
    button_quit = Button(root, text='Quit program', bg='red', font=('Helvetica', 30), command=quit)

    button_client.grid(row=1, columnspan=12, sticky='n')
    button_check.grid(row= 2, columnspan=12, sticky='n')
    button_log.grid(row=28, columnspan=12)
    button_quit.grid(row=29, columnspan=12)

    root.mainloop()
main()
