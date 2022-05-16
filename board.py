from tkinter import *
from tkinter import messagebox
# import nltk
# from nltk.corpus import words
from time import gmtime, strftime
import time
from collections import Counter


import tkinter as tki

ws = tki.Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')

# word_bank_img = tki.PhotoImage(file="photos\word_bank.png")
#
# label = tki.Label(ws, text='Some Plain Text', image=word_bank_img, compound='center')
# label.pack()

message = "line1"

text_box = tki.Text(
    ws,
    height=12,
    width=40, bg='#394d59'
)
text_box.pack(expand=True)
text_box.insert(tki.INSERT, message +"\n")
text_box.config(state='normal')
text_box.insert(tki.INSERT, "line2")
text_box.config(state='disabled')





ws.mainloop()




# import tkinter as tki
# # from PIL import Image, ImageTk
#
# root = tki.Tk()
#
# # image = Image.open('hi.gif')
# word_bank_img = tki.PhotoImage(file="photos\word_bank.png")
#
# label = tki.Label(root, text='Some Plain Text', image=word_bank_img, compound='center')
# label.pack()
#
# root.mainloop()
#
#










# def game_timer(countdown):
#     min, sec = divmod(countdown, 60)
#     # show the timer with up to 2 decimal places in minutes and second:
#     timer_lbl['text'] = "{:02d}:{:02d}".format(int(min), int(sec))
#     if countdown != 0:
#         root.after(1000, game_timer, countdown - 1)
#
#
# if __name__ == '__main__':
#     # creating the main window
#     root = Tk()
#     # setting the window
#     root.title("Boggle")
#     root.configure(bg='#394d59')
#     root.geometry("1200x600")
#     # setting the logo
#     logo_img = PhotoImage(file="photos\logo.png")
#     logo_lbl = Label(root, image=logo_img)
#     logo_lbl.configure(borderwidth=0, highlightthickness=0)
#     logo_lbl.place(x=450, y=0)
#     # setting the users choices label
#     user_choice_lbl = Label(root, text="")
#     user_choice_lbl.place(x=435, y=190, relwidth=0.23, relheight=0.005, height=40)
#     # setting the submit button
#     submit_btn = Button(root, text="Submit", bg="White", fg="Black", width=5,
#                       height=2, font=('Helvetica', '10'))
#     submit_btn.place(x=735, y=190)
#     # setting the score label
#     score_lbl = Label(root, text="0", bg="#394d59", fg="Yellow", font=('Helvetica', '17'))
#     score_lbl.place(x=750, y=130)
#     s_lbl = Label(root, text="score", bg="#394d59", fg="Yellow", font=('Helvetica', '11'))
#     s_lbl.place(x=740, y=160)
#     # creating the words bank
#     word_bank_img = PhotoImage(file="photos\word_bank.png")
#     word_bank_lbl = Label(root, image=word_bank_img)
#     word_bank_lbl.configure(borderwidth=0, highlightthickness=0)
#     word_bank_lbl.place(x=800, y=200)
#
#     # creating the buttons
#     # the below list of lists will hold all buttons
#     buttons_grid = []
#     for row in range(4):
#         row_of_buttons = []
#         for col in range(4):
#             btn = Button(root, text="A", bg="white", fg="Black", width=5,
#                          height=2, font=('Helvetica', '20'))
#             btn.place(x=430 + (90 * col), y=240 + (90 * row))
#             row_of_buttons.append(btn)
#         buttons_grid.append(row_of_buttons)
#
#     timer_lbl = Label(root)
#     timer_lbl.place(x=20, y=50)
#     TIME = 180
#     game_timer(TIME)
#     # root.after(60000, )
#
#     # create the scroll bar word bank
#     # creating a scrollbar
#     scrollbar = Scrollbar(root)
#     # v.configure(troughcolor="#394d59")
#     scrollbar.place(x=1110, y=260, relheight=0.325)
#     # create a Text widget with 35 chars
#     # width and 12 lines height
#     # here yscrollcomannd is used to attach Text
#     # widget to the vertical scrollbar
#     text_box = Text(root, width=35, height=12, wrap=NONE,
#                     yscrollcommand=scrollbar.set)
#
#     # insert some text into the text widget
#     for i in range(20):
#         text_box.insert(END, "text\n")
#     # attach Text widget to root window at top
#     text_box.place(x=830, y=260)
#     # here command represents the method to
#     # be executed yview is executed on
#     # object 't' Here t may represent any
#     # widget
#     scrollbar.config(command=text_box.yview)
#
#     root.mainloop()
#
