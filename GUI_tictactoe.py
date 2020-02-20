import tkinter as tk

root = tk.Tk()
root.title("TIC TAC TOE")

b = True

def btnval(val):
        from tkinter import messagebox
        global b
        if val["text"] == "" and b == True :
            val["text"] = 'x'
            b = False
        elif val["text"] == "" and b == False:
            val["text"] = 'o'
            b = True
        if but1["text"] == but2["text"] == but3["text"] or but4["text"] == but5["text"] == but6["text"] or but7["text"] == but8["text"] == but9["text"] or but1["text"] == but4["text"] ==but7["text"] or but2["text"] == but5["text"] == but8["text"] or but3["text"] == but6["text"] == but9["text"] or but1["text"] == but5["text"] == but9["text"] or but3["text"] == but5["text"] == but7["text"]:
            messagebox.showinfo("title","You Won!!" )


but1 = tk.Button(text = "",width = 30, height = 10, command = lambda : btnval(but1))
but1.grid(row = 0, column = 0)

but2 = tk.Button(width = 30, height = 10, command = lambda : btnval(but2))
but2.grid(row = 1, column = 0)

but3 = tk.Button(width = 30, height = 10, command = lambda : btnval(but3))
but3.grid(row = 2, column = 0)

but4 = tk.Button(width = 30, height = 10, command = lambda : btnval(but4))
but4.grid(row = 0, column = 1)

but5 = tk.Button(width = 30, height = 10, command = lambda : btnval(but5))
but5.grid(row = 0, column = 2)

but6 = tk.Button(width = 30, height = 10, command = lambda : btnval(but6))
but6.grid(row = 1, column = 1)

but7 = tk.Button(width = 30, height = 10, command = lambda : btnval(but7))
but7.grid(row = 1, column = 2)

but8 = tk.Button(width = 30, height = 10, command = lambda : btnval(but8))
but8.grid(row = 2, column = 1)

but9 = tk.Button(width = 30, height = 10, command = lambda : btnval(but9))
but9.grid(row = 2, column = 2)

root.mainloop()

# if but1["text"] == but2["text"] == but3["text"]:


# a = lambda argument : expression

# a =lambda e : e*3
# print(a([1,2,3]))
