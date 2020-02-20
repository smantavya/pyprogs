import tkinter as tk

root = tk.Tk()
root.title("Billing Counter")

#variables
mrp = tk.IntVar()
t1 = tk.StringVar()
t2 = tk.StringVar()
t3 = tk.StringVar()

#FUNCTIONS
def clr():
    global t1
    global t2
    global t3
    t1 == t2 == t3 == ''

def ttl():
    global mrp
    global t1
    global t2
    global t3



title = tk.Label(width = 30, text = "Sample Restaurant Billing :- ", font = "bold 17")
title.grid(row = 0, columnspan = 4, column = 0)

item1 = tk.Label(width = 12, text = "Item1 @ 20", font = "bold")
item1.grid(row = 1, column = 0)

ent1 = tk.Entry(width = 12, textvariable = t1)
ent1.grid(row = 1, column = 1)

item2 = tk.Label(width = 12, text = "Item2 @ 40", font = "bold")
item2.grid(row = 2, column = 0)

ent2 = tk.Entry(width = 12, textvariable = t2)
ent2.grid(row = 2, column = 1)

item3 = tk.Label(width = 12, text = "Item3 @ 80", font = "bold")
item3.grid(row = 3, column = 0)

ent3 = tk.Entry(width = 12, textvariable = t3)
ent3.grid(row = 3, column = 1)

clear = tk.Button(width = 12, text = "CLEAR", command = clr)
clear.grid(row = 4, column = 0)

tbutton = tk.Button(width = 12, text = "TOTAL")
tbutton.grid(row = 4, column = 1)

total = tk.Label(width = 12, text = "MRP = ")
total.grid(row = 5, column = 0)

total1 = tk.Label(width = 12, textvariable = mrp)
total1.grid(row = 5, column = 1)
root.mainloop()
