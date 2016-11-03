from tkinter import *


def updatelist():
    from general_functions import csv_read, csv_writelist
    csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 2)
    pending = csv_read('ReadyForAck.csv')
    return pending


def beoordeel(goedgekeurd, eachtweet, tweetnum):
    import general_functions
    if goedgekeurd is True:
        general_functions.accepted(eachtweet)
        root.destroy()
    elif goedgekeurd is False:
        general_functions.rejected(eachtweet)
        root.destroy()
def tweet(lst, tweetnum):
    eachtweet = lst[tweetnum]
    return eachtweet

def svarname(tweet):
    svarname = tweet[0]
    return svarname

def svarmsg(tweet):
    svarmsg = tweet[1]
    return svarmsg

tweetnum = 0

loop = 0
while loop == 0:
    Tweets = updatelist()
    tweetslength = len(Tweets) - 1
    for eachtweet in Tweets:# eachtweet 0 = naam, 1 is bericht, 2 is datum, 3 is stationafkorting
        try:
            root = Tk()
            root.title('NS Approval App')


            ######
            # Background
            ####
            background_image = PhotoImage(file="GUI/NS_logo.png")
            background_label = Label(root, image=background_image)
            background_label.grid(rowspan=30, columnspan=12)
            root.resizable(False, False)

            ######
            # Titellabel
            ####

            label_titel = Label(root, text='NS bericht approval', bg='#FFCC18')
            label_titel.config(font=('times', 24))
            label_titel.grid(row=0, columnspan=12, sticky='n')

            ######
            # Name
            ####
            label_2 = Label(root, text='Naam : ', bg='#FFCC18')
            label_2.config(font=('times', 24))
            label_2.grid(row=1, column=2, sticky='ne')
            ######
            # Message:
            ####
            label_3 = Label(root, text='Bericht : ', bg='#FFCC18')
            label_3.config(font=('times', 24))
            label_3.grid(row=2, column=2, sticky='ne')



            ####
            svar_naam = StringVar(root, value=eachtweet[0])
            svar_bericht = StringVar(root, value=eachtweet[1])

            label_naam = Message(root, textvariable=svar_naam, bg='#e6e6e6', borderwidth=4)
            label_naam.config(font=('times', 20), width=400)
            label_naam.grid(row=1, column=3, columnspan=4, sticky='nw')

            label_message = Message(root, textvariable=svar_bericht, bg='#e6e6e6')
            label_message.grid(row=2, column=3, columnspan=5,  sticky='ew')
            label_message.config(font=('times', 18), width=400)

            accept = lambda: beoordeel(True, eachtweet, tweetnum)
            reject = lambda: beoordeel(False, eachtweet, tweetnum)
            Exit = loop = 1
            button_reject = Button(root, text='Reject', bg="red", command=reject)
            button_accept = Button(root, text='accept', bg="Green", command=accept)
            button_quit = Button(root, text='quit', bg='Gray', command=Exit)

            button_reject.config(font=('times', 32))
            button_reject.grid(row=11, column=1)


            button_accept.config(font=('times', 32))
            button_accept.grid(row=11, column=10)

            button_quit.config(font=('times', 32))
            button_quit.grid(row=11, column=5)
            tweetnum += 1
            root.mainloop()
        except:
            if IndexError:
                # popup -> wil je doorgaan?
                # Ja = voer bestand opnieuw uit
                # Nee = loop = 1