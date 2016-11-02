from tkinter import *

root = Tk()
root.title('NS Bericht')


#Background story
background_image = PhotoImage(file="NS_logo.png")
background_label = Label(root, image=background_image)
background_label.grid(rowspan=30, columnspan=12)


#bericht
label_message = Message(root, textvariable = svar_bericht, bg='#e6e6e6')
label_message.grid(row=2, column=3, columnspan=6,  sticky='ew')
label_message.config(font=('times', 18), width=400)