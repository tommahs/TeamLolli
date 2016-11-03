from tkinter import *
from tkinter.scrolledtext import ScrolledText

def updatelist():
    from general_functions import csv_read, csv_writelist
    csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 2)
    pending = csv_read('ReadyForAck.csv')
    return pending


def beoordeel(goedgekeurd, eachtweet, tweetnum):
    import general_functions
    if goedgekeurd is True:
        general_functions.accepted(eachtweet)
        print(eachtweet)
    elif goedgekeurd is False:
        general_functions.rejected(eachtweet)
    elif goedgekeurd == 'exit':
        tweetAck.quit()


def tweet(lst, tweetnum):
    eachtweet = lst[tweetnum]
    return eachtweet


def svarname(tweet):
    svarname = tweet[0]
    return svarname


def svarmsg(tweet):
    svarmsg = tweet[1]
    return svarmsg


def popupmsg():
    popup = Tk()
    popup.wm_title('Continue?')
    label = Label(popup, text='Do you wish to continue?')
    # B1 = Button(popup, text="Okay", command=popup.destroy)
    yes = True
    no = False
    Button2 = Button(popup, text="Yes", command=yes)
    Button3 = Button(popup,text="No", command=no)
    # B1.pack()
    Button2.pack()
    Button3.pack()
    popup.mainloop()
    return



def tweetAck(msg):
    tweetnum = 0
    loop = 0
    while loop == 0:
        Tweets = updatelist()
        tweetslength = len(Tweets) - 1
        if tweetnum >= tweetslength:
            loop = 1
        ### NEXT FUNCTIE
        try:
            svar_naam = Tweets[tweetnum][0]
            # print(svar_naam)
            svar_bericht = Tweets[tweetnum][1]
            # print('msg:', svar_bericht)
            check = Tk()
            check.wm_title(msg)
            ######
            # Background
            ####
            # print('Backgrounding!')
            # background_image = PhotoImage(file="GUI/NS_logo.png")
            # background_label = Label(check, image=background_image)
            # background_label.grid(rowspan=30, columnspan=12)
            # check.resizable(False, False)

            ######
            # Titellabel
            ####
            # print('Title Lable')
            label_titel = Label(check, text='NS bericht approval', bg='#FFCC18')
            label_titel.config(font=('times', 24))
            label_titel.grid(row=0, columnspan=12, sticky='n')

            ######
            # Name
            ####
            label_2 = Label(check, text='Naam : ', bg='#FFCC18')
            label_2.config(font=('times', 24))
            label_2.grid(row=1, column=2, sticky='ne')
            # print('Name label')
            label_3 = Label(check, text='Bericht : ', bg='#FFCC18')
            label_3.config(font=('times', 24))
            label_3.grid(row=2, column=2, sticky='ne')
            # print('Message label')
            ####
            label_naam = Message(check, textvariable='svar_naam', bg='#e6e6e6', borderwidth=4)
            label_naam = Label(check, text=svar_naam, bg='#e6e6e6', borderwidth=4)
            label_naam.config(font=('times', 20), width=20)
            label_naam.grid(row=1, column=3, columnspan=4, sticky='nw')
            # print("containing name")
            label_message = ScrolledText(check, width=40, height=4, bg='#e6e6e6')
            label_message.insert(INSERT, svar_bericht)
            # label_message = Label(check, text=svar_bericht, width=40, height=4, bg='#e6e6e6')
            label_message.grid(row=2, column=3, columnspan=5,  sticky='ew')
            label_message.config(font=('times', 18))
            # print("containing message")
            accept = lambda: beoordeel(True, Tweets[tweetnum], tweetnum)
            reject = lambda: beoordeel(False, Tweets[tweetnum], tweetnum)

            button_reject = Button(check, text='Reject', bg="Red", command=reject)
            # print('Rejectbutton')
            button_accept = Button(check, text='accept', bg="Green", command=accept)
            # print('Accept button')
            button_quit = Button(check, text="Cancel", bg='Red', command=check.quit)
            # print('Quit button')
            button_reject.config(font=('times', 32))
            button_reject.grid(row=11, column=1)
            # print('Rejectgrid')
            button_accept.config(font=('times', 32))
            button_accept.grid(row=11, column=10)
            # print('Accept grid')
            button_quit.config(font=('times', 32))
            button_quit.grid(row=11, column=5)
            print('Quit grid')
            tweetnum += 1
            check.mainloop()

        except:
            if IndexError:
                loop = 1
            else:
                print('test')
        try:
            print(tweetnum)
            next = popupmsg()
            if next is True:
                break
            else:
                continue
        except:
            print("except")

        finally:
            if next is True:
                pass
            else:
                loop = 1
# tweetAck('Client')