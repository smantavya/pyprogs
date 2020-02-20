import mysql.connector

conn = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = '123',
    database = "sakila",
)

cur = conn.cursor()

# cur.execute("show databases;")
cur.execute("show tables;")
# print(cur)
# for q in cur:
#     print(q)


print(cur.fetchall())
# conn.commit()
