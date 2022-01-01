import tkinter as tk

#================== Setups ==================#

app = tk.Tk()
app.config(bg="#1b5969")

btx = 27
bty = 19

grid_spacing = 6

xicon = tk.PhotoImage(file=r'C:\Users\Night\Documents\Python\icons\x.png')
oicon = tk.PhotoImage(file=r'C:\Users\Night\Documents\Python\icons\o.png')



#================== Row 1 Assignment ==================#

bt00 = tk.Button(padx=btx, pady=bty)
bt00.grid(row=0, column=0, pady=grid_spacing, padx=grid_spacing)

bt01 = tk.Button(padx=btx, pady=bty)
bt01.grid(row=0, column=1, pady=grid_spacing, padx=grid_spacing)

bt02 = tk.Button(padx=btx, pady=bty)
bt02.grid(row=0, column=2, pady=grid_spacing, padx=grid_spacing)

#================== Row 2 Assignment ==================#

bt10 = tk.Button(padx=btx, pady=bty)
bt10.grid(row=1, column=0, pady=grid_spacing, padx=grid_spacing)

bt11 = tk.Button(padx=btx, pady=bty)
bt11.grid(row=1, column=1, pady=grid_spacing, padx=grid_spacing)

bt12 = tk.Button(padx=btx, pady=bty)
bt12.grid(row=1, column=2, pady=grid_spacing, padx=grid_spacing)

#================== Row 3 Assignment ==================#

bt20 = tk.Button(padx=btx, pady=bty)
bt20.grid(row=2, column=0, pady=grid_spacing, padx=grid_spacing)

bt21 = tk.Button(padx=btx, pady=bty)
bt21.grid(row=2, column=1, pady=grid_spacing, padx=grid_spacing)

bt22 = tk.Button(padx=btx, pady=bty)
bt22.grid(row=2, column=2, pady=grid_spacing, padx=grid_spacing)

#================== Buttons Index Assignment ==================#

grid = [[bt00, bt01, bt02], [bt10, bt11, bt12], [bt20, bt21, bt22]]

# grid[line][column].config(image=icon)

#==================#

app.mainloop()