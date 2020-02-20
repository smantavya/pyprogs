import tkinter
#main window
window = tkinter.Tk()
window.title('MY FIRST GUI')
#show text
label = tkinter.Label(window, text = 'hello world!',font=('arial bold',10))
label.grid(column=0,row=0)
#entry
txt = tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)
#button
def clicked():
	label.configure(text='welcome to '+ txt.get() + '!')
	bt.configure(fg="red")
bt = tkinter.Button(window,text = "Enter",fg = "blue",bg="light grey",command=clicked)
bt.grid(column=2,row=0)
window.mainloop()
