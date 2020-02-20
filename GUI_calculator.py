import tkinter as tk

root = tk.Tk()
root.title("Calculator")

#temporary variable
t = tk.StringVar()
temp1 = ""


# there will be a entry for input
ent = tk.Entry(width = 43, font = "20", textvariable = t)
ent.grid(row = 0, column = 0 , columnspan = 5)


# function for typing entry

def calc(var):
    global t
    global temp1
    temp1 += str(var["text"])
    t.set(temp1)

#function for evaluation
def equal(var):
    global temp1
    total = str(eval(temp1))
    t.set(total)
    temp1 = ""

#function for clear button
def clear(var):
    global temp1
    temp1 = ""
    t.set("")

# there will be buttons for digits and actions

one = tk.Button(width = 10, height = 5,text = "1", command = lambda : calc(one))
one.grid(row = 1, column = 0)

two = tk.Button(width = 10, height = 5, text = "2", command = lambda : calc(two))
two.grid(row = 1, column = 1)

three = tk.Button(width = 10, height = 5, text = "3", command = lambda : calc(three))
three.grid(row = 1, column = 2)

four = tk.Button(width = 10, height = 5, text = "4", command = lambda : calc(four))
four.grid(row = 2, column = 0)

five = tk.Button(width = 10, height = 5, text = "5", command = lambda : calc(five))
five.grid(row = 2, column = 1)

six = tk.Button(width = 10, height = 5, text = "6", command = lambda : calc(six))
six.grid(row = 2, column = 2)

seven = tk.Button(width = 10, height = 5, text = "7", command = lambda : calc(seven))
seven.grid(row = 3, column = 0)

eight = tk.Button(width = 10, height = 5, text = "8", command = lambda : calc(eight))
eight.grid(row = 3, column = 1)

nine = tk.Button(width = 10, height = 5, text = "9", command = lambda : calc(nine))
nine.grid(row = 3, column = 2)

zero = tk.Button(width = 10, height = 5, text = "0", command = lambda : calc(zero))
zero.grid(row = 4, column = 0)

zero2 = tk.Button(width = 22, height = 5, text = "00", command = lambda : calc(zero2))
zero2.grid(row = 4, columnspan = 2, column = 1)

eq = tk.Button(width = 32, height = 5, text = "=", command = lambda : equal(eq))
eq.grid(row = 4, columnspan = 2, column = 3)

clr = tk.Button(width = 32, height = 5, text = "C", command = lambda : clear(clr))
clr.grid(row = 1, columnspan = 2, column = 3)

plus = tk.Button(width = 15, height = 5, text = "+", command = lambda : calc(plus))
plus.grid(row = 2, column = 3)

minus = tk.Button(width = 15, height = 5,text = "-", command = lambda : calc(minus))
minus.grid(row = 3, column = 3)

mult = tk.Button(width = 15, height = 5,text = "*", command = lambda : calc(mult))
mult.grid(row = 2, column = 4)

divide = tk.Button(width = 15, height = 5, text = "/", command = lambda : calc(divide))
divide.grid(row = 3,rowspan = 1, column = 4)


root.mainloop()
