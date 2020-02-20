import tkinter.ttk

window = tkinter.Tk()
window.title('ComboBox')
combo = tkinter.ttk.Combobox(window)
combo['values'] = (1,2,3,4,5,'text')
combo.current(3)
combo.grid()

window.mainloop()