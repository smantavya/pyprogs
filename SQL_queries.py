import mysql.connector

conn = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = '123',
    database = 'myschool',
)

cur = conn.cursor()

# cur.execute("select * from student where name = 'rakesh';")
# cur.execute("select * from student where s_no = 6;")
# cur.execute("update student set name = 'hey', f_name = 'hello' where s_no = 3;")
sel = "insert into student(name,f_name,sub1,sub2,sub3) values(%s,%s,%s,%s,%s);"
t = ("a","b",1,2,3)
cur.execute(sel,t)
# cur.execute("select * from student;")

# print(cur.fetchall())

conn.commit()
