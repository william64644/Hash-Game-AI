#================== Setups ==================#

import tkinter as tk
from threading import *

app = tk.Tk()
app.title("Hash Game")
app.config(bg="#1b5969")
app.geometry("350x216")

btx_size = 55
bty_size = 55

grid_spacing = 6

xicon = tk.PhotoImage(file=r'.\icons\x.png')
oicon = tk.PhotoImage(file=r'.\icons\o.png')
blank_image = tk.PhotoImage(file=r'.\icons\blank.png')

#=================#

class button:

    def left_click(self, event):
        self.bt.config(image=oicon)
    
    def right_click(self, event):
        self.bt.config(image=xicon)

    def midle_click(self, event):
        self.bt.config(image=blank_image)
        print(event, type(event))

    def click(self, event):
        self.bt.config(image=blank_image)



    def __init__(self, gridx, gridy):

        self.gridx = gridx
        self.gridy = gridy
        self.bt = tk.Button(padx=btx_size, pady=bty_size, image=blank_image)
        self.bt.grid(row=gridy, column=gridx, pady=grid_spacing, padx=grid_spacing)
        self.bt.bind('<Button-1>', self.left_click)
        self.bt.bind('<Button-2>', self.midle_click)
        self.bt.bind('<Button-3>', self.right_click)


bt00 = button(0, 0)
bt01 = button(0, 1)
bt02 = button(0, 2)

bt10 = button(1, 0)
bt11 = button(1, 1)
bt12 = button(1, 2)

bt20 = button(2, 0)
bt21 = button(2, 1)
bt22 = button(2, 2)

app.mainloop()