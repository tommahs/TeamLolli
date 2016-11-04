######
# Main Client file.
# 1. Ask input from user, add tweetcounter + location
# 2. Write to csv file
# 3. Check if
###

# Twitter max characters = 140

######
# Asking user input
####

# def userinput(station):
#     from general_functions import inputquestion
#     try:
#         fname = inputquestion('First name') #Check length, 10 characters max
#         if len(fname) > 10:
#             print('Name is too long')
#             userinputlst = 1
#             return userinputlst
#         else:
#             text = inputquestion('Tweet') #Check length, 120 char max
#             if len(text) > 120:
#                 print('Text is too long')
#                 userinputlst = 2
#                 return userinputlst
#             date = definedate()
#             userinputlst = [fname, text, date, station]
#             return userinputlst
#     except TypeError:
#         print('Something has gone wrong, please try again')


def definedate():
    from datetime import datetime
    date = datetime.now().strftime("20%y-%m-%d %H:%M")
    return date


def sendtofile(newlst):
    import general_functions
    general_functions.csv_writelist('clients', 'clients', newlst, 1)
    print('Clicked on Send!')
    print(newlst)

######
# Client menu
# Loops
# Asks for user input
# Defines current stations abbriviation
# Combine the userinput into the client list from csv
# Writes clientlist to csv
# Print DONE
####
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def logmain():
    import general_functions
    logfile = general_functions.csv_read('logfile.csv')
    num = 0
    maxlength = 10
    logfilelst = []
    try:
        while num < maxlength:
            logfilelst.append(('{} {}: {} {}'.format(logfile[num][2], logfile[num][0], logfile[num][1], logfile[num][3])))
            num += 1
    except:
        print('lol')
    log = ''
    for each in logfilelst:
        log += '\n{}'.format(each)
    print(log)

    loggui = Tk()
    loggui.title('Logfile Reader')
    loggui.config(bg='Gray')

    label_message = ScrolledText(loggui, width=100, height=20, bg='#e6e6e6')
    label_message.insert(INSERT, log)
    label_message.grid(row=2, column=3, columnspan=5, sticky='ew')
    label_message.config(font=('times', 18))

    # button_cancel = Button(loggui, text="Cancel", bg='Red', command=exit)
    # button_cancel.config(font=('times', 32))
    # button_cancel.grid(row=10, column=2)
    loggui.mainloop()
    #
    #
    # send = lambda: getdata(svar_date, svar_station)
    #
    # button_cancel = Button(client, text="Cancel", bg='Red', command=client.destroy)
    # button_send = Button(client, text='Verstuur', bg="Green", command=send)
    #
    # button_cancel.config(font=('times', 32))
    # button_cancel.grid(row=10, column=2)
    # button_send.config(font=('times', 32))
    # button_send.grid(row=10, column=7)
    # client.mainloop()
