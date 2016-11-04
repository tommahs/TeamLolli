from tkinter import *
from tkinter.scrolledtext import ScrolledText


def loglist():
    '''This function reads the logfile, appends each tweet to a list & creates a line for each tweet.'''
    import general_functions
    logfile = general_functions.csv_read('logfile.csv')
    counter = 0
    maxlength = 10
    logfilelst = []
    try:
        while counter < maxlength:
            logfilelst.append(
                ('{} {}: {} {}'.format(logfile[counter][2], logfile[counter][0], logfile[counter][1], logfile[counter][3])))
            counter += 1
    except:
        if ValueError:
            pass
    log = ''
    for each in logfilelst:
        log += '\n{}'.format(each)
    return log


def logmain():
    '''Main window. The logs will be displayed here.'''
    loggui = Tk()
    loggui.title('Logfile Reader')
    loggui.config(bg='Gray')

    label_message = ScrolledText(loggui, width=100, height=20, bg='#e6e6e6')
    label_message.insert(INSERT, loglist())
    label_message.grid(row=2, column=3, columnspan=5, sticky='ew')
    label_message.config(state="disabled", font=('times', 18))

    loggui.mainloop()
