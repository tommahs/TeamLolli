import tkinter

# Starting
showWindow = tkinter.Tk()


# Title window
showWindow.title("NS Bericht scherm")

# Icon van window
# showWindow.wm_iconbitmap('')


# Label en Texten "body"
lbl = tkinter.Label(showWindow, text='Bericht scherm')
lbl.pack()

mb = tkinter.Message(showWindow, text='testtest')
mb.pack()



# De grote van de window bepalen
showWindow.geometry('300x500')


# Ending
showWindow.mainloop()