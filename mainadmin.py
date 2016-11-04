from tkinter import *
from tkinter.scrolledtext import ScrolledText

def updatelist():
    '''Creates a new list containing tweets that are ready to be checked'''
    from general_functions import csv_read, csv_writelist
    csv_writelist('ReadyForAck', 'ReadyForAck', 'clients', 2)
    pending = csv_read('ReadyForAck.csv')
    return pending

def tweetAck(msg):
    '''The main application to check messages to be posted on twitter'''
    tweetnum = 0
    loop = 0
    Tweets = updatelist()
    while loop == 0:
        tweetslength = len(Tweets) - 1
        if tweetnum >= tweetslength:
            loop = 1
        try:
            svar_naam = Tweets[tweetnum][0]
            svar_bericht = Tweets[tweetnum][1]
            check = Tk()
            check.config(bg='#FFCC18')
            check.wm_title(msg)

            label_titel = Label(check, text='NS bericht approval', bg='#FFCC18')
            label_titel.config(font=('times', 24))
            label_titel.grid(row=0, columnspan=12, sticky='n')

            label_2 = Label(check, text='Naam : ', bg='#FFCC18')
            label_2.config(font=('times', 24))
            label_2.grid(row=1, column=2, sticky='ne')

            label_3 = Label(check, text='Bericht : ', bg='#FFCC18')
            label_3.config(font=('times', 24))
            label_3.grid(row=2, column=2, sticky='ne')

            label_naam = Label(check, text=svar_naam, bg='#e6e6e6', borderwidth=4)
            label_naam.config(anchor=W, font=('times', 20), width=20)
            label_naam.grid(row=1, column=3, columnspan=4, sticky='nw')

            label_message = ScrolledText(check, width=40, height=4, bg='#e6e6e6')
            label_message.insert(INSERT, svar_bericht)

            label_message.grid(row=2, column=3, columnspan=5,  sticky='ew')
            label_message.config(state="disabled", font=('times', 18))

            def beoordeel(allowed, eachtweet, tweetnum):
                ''' Either send to accepted(eachtweet) or rejected(eachtweet) based on the input from different buttons'''
                import general_functions
                if allowed is True:
                    general_functions.accepted(eachtweet)
                    check.quit()
                elif allowed is False:
                    general_functions.rejected(eachtweet)
                    check.quit()
            accept = lambda: beoordeel(True, Tweets[tweetnum], tweetnum)
            reject = lambda: beoordeel(False, Tweets[tweetnum], tweetnum)


            button_reject = Button(check, text='Reject', bg="Red", command=reject)

            button_accept = Button(check, text='accept', bg="Green", command=accept)

            button_cancel = Button(check, text="Quit", bg='Red', command=exit)
            button_quit = Button(check, text='Quit program', bg='Green', font=('times', 32), command=exit)

            button_reject.config(font=('times', 32))
            button_reject.grid(row=11, column=1)

            button_accept.config(font=('times', 32))
            button_accept.grid(row=11, column=10)

            button_cancel.config(font=('times', 32))
            button_cancel.grid(row=11, column=4)
            button_quit.config(font=('times', 32))
            button_quit.grid(row=11, column=5)
            check.mainloop()
            tweetnum += 1
        except:
            if IndexError:
                loop = 1
        finally:
            check.destroy()