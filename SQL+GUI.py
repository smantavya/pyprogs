import mysql.connector as con
import tkinter as tk

# SQL connector
conn = con.connect(
    user = "root",
    host = "localhost",
    password = "123",
    database = "myschool",
)
cur = conn.cursor()
cur.execute("select * from student;")
print(cur.fetchall())


#GUI queries
root = tk.Tk()
root.title("MySchool")




root.mainloop()
