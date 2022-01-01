#================== Setups ==================#

import tkinter as tk
from threading import *

app = tk.Tk()
app.title("Hash Game")
app.config(bg="#1b5969")
app.geometry("350x218")

btx_size = 55
bty_size = 55

grid_spacing = 6

xicon = tk.PhotoImage(file=r'.\icons\x.png')
oicon = tk.PhotoImage(file=r'.\icons\o.png')
blank_image = tk.PhotoImage(file=r'.\icons\blank.png')
wipe_icon = tk.PhotoImage(file=r'.\icons\wipe-icon.png')

#=======================================#

class button:

    def left_click(self, *args):
        self.bt.config(image=oicon)
    
    def right_click(self, *args):
        self.bt.config(image=xicon)

    def midle_click(self, *args):
        self.bt.config(image=blank_image)

    def wipe(*args):
        for bt in game_buttons:
            bt.midle_click(Event)

    def __init__(self, gridx, gridy, purpose, button_image = blank_image):

        self.gridx = gridx
        self.gridy = gridy
        self.bt = tk.Button(padx=btx_size, pady=bty_size, image=button_image)
        self.bt.grid(row=gridy, column=gridx, pady=grid_spacing, padx=grid_spacing)

        if purpose == "game":
            self.bt.bind('<Button-1>', self.left_click)
            self.bt.bind('<Button-2>', self.midle_click)
            self.bt.bind('<Button-3>', self.right_click)

        elif purpose == "wipe":
            self.bt.bind('<Button-1>', self.wipe)

#=======================================#

bt00 = button(0, 0, "game")
bt01 = button(0, 1, "game")
bt02 = button(0, 2, "game")
bt10 = button(1, 0, "game")
bt11 = button(1, 1, "game")
bt12 = button(1, 2, "game")
bt20 = button(2, 0, "game")
bt21 = button(2, 1, "game")
bt22 = button(2, 2, "game")

game_buttons = [bt00, bt01, bt02, bt10, bt11, bt12, bt20, bt21, bt22]

btwipe = button(3, 0, "wipe", button_image=wipe_icon)

app.mainloop()