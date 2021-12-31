#================== Setups ==================#

import tkinter as tk

app = tk.Tk()
app.config(bg="#1b5969")

btx_size = 55
bty_size = 55

grid_spacing = 6

xicon = tk.PhotoImage(file=r'C:\Users\Night\Documents\Python\icons\x.png')
oicon = tk.PhotoImage(file=r'C:\Users\Night\Documents\Python\icons\o.png')
blank_image = tk.PhotoImage(file=r'C:\Users\Night\Documents\Python\icons\b.png')

#===========test=======#

class button:

    def left_click(self, event):
        self.bt.config(image=oicon)
    
    def right_click(self, event):
        self.bt.config(image=xicon)

    def midle_click(self, event):
        self.bt.config(image=blank_image)

    def click(self, event):
        self.bt.config(image=blank_image)

    def __init__(self, icon, gridx, gridy):

        self.icon = icon
        self.gridx = gridx
        self.gridy = gridy
        self.bt = tk.Button(padx=btx_size, pady=bty_size, image=blank_image)
        self.bt.grid(row=gridy, column=gridx, pady=grid_spacing, padx=grid_spacing)
        self.bt.bind('<Button-1>', self.left_click)
        self.bt.bind('<Button-2>', self.midle_click)
        self.bt.bind('<Button-3>', self.right_click)


bt00 = button(None, 0, 0)
bt01 = button(None, 0, 1)
bt02 = button(None, 0, 2)

bt10 = button(None, 1, 0)
bt11 = button(None, 1, 1)
bt12 = button(None, 1, 2)

bt20 = button(None, 2, 0)
bt21 = button(None, 2, 1)
bt22 = button(None, 2, 2)

app.mainloop()