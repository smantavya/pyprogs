import tkinter as tk

# Tk() is used for creating main window
root = tk.Tk()
root.title("My First GUI")

p = tk.StringVar()

# label is used for texts and pictures
lb = tk.Label(width = 20 , height = 2 ,text = "This is python", bg="red", fg="yellow", font = "bold 20 ")
lb.grid(row = 0, column = 0)
lb1 = tk.Label(text = "this is python1")
lb1.grid(row = 1, column = 0)

# entry is used to create user input dialogue
def hello():
    t = "hello"
    p.set(t)
    # print(p.get())
ent = tk.Entry(textvariable = p)
ent.grid(row = 2, column = 0)

# Button() is used for creating clickable button
bt = tk.Button(text = "click for hello", activeforeground = "yellow", activebackground = "red", command = hello)
bt.grid(row = 3, column = 0)

# mainloop() is used to make window run untill stopped
root.mainloop()
