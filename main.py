from random import choice
from tkinter import *
from tkinter import filedialog, messagebox

application = Tk()
application.geometry('650x30')
application.resizable(False, False)
application.title('Gizmo Message Box')
application.config(bg='burlywood')


messages=["You are the best", "The world is better with you", "You are the smartest little Gizmo", "There is no goal to name a prize after you, because no one can achive that much to deserve it",
          "You are so beautiful", "On a hotness scale 1-10 you are 18", "You're food is delicious, just like you", "You're cooking talents like Gordon Ramsey's minus the anger management issues",
          "Everyday is like the best date with you", "I tought there is no perfect person, until I met you", "You can do anything", "You are the beauty industry's Da Vinci"]


def gizmo_message():
    return choice(messages)

# Title tag
top_panel = Frame(application, bd= 1, relief= FLAT)
top_panel.pack(side = TOP)

title_tag = Label(top_panel, text =gizmo_message() + " =)", fg='blue',
                  font = ('Dosis', 10), bg = 'burlywood', width =80)
title_tag.grid(row =30, column =00)


# Prevent window from closing
application.mainloop()





