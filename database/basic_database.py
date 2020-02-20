import mysql.connector as conter


conn = conter.connect(
    user = 'root',
    host = 'localhost',
    password = '8524567891235'
)

print(conn)
