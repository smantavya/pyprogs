import mysql.connector
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "123",
    database = "myschool1",
)

def school():
    act = int(input('''Welcome to MySchool
                press 1 to Add a new student
                press 2 to Deposit Fees
                press 3 to know due Fees
                press 4 to Remove Student
                press 5 to know students data
                press 6 to exit
            '''))
    if act == 1:
        add_student()
    elif act == 2:
        deposit_fees()
    elif act == 3:
        feesdue()
    elif act == 4:
        remove_student()
    elif act == 5:
        school_data()
    # elif act == 6:
    #     delete_account()
    elif act == 6:
        exit()


cur = conn.cursor()


def add_student():
    global n
    global ln
    n = str(input("enter student's firstname = "))
    ln = str(input("enter student's lastname name = "))
    adst = "insert into students(firstname,lastname) values(%s,%s);"
    adstv = (n,ln)
    cur.execute(adst,adstv)
    conn.commit()

def deposit_fees():
    global n
    global f
    try:
        n = str(input("enter student's firstname = "))
        r = int(input("enter your student's roll number = "))
        f = int(input("enter amount of fees to be deposited = "))
        chkst = "select * from students where firstname = %s"
        chkstv = (n, )
        cur.execute(chkst,chkstv)
        a = cur.fetchall()
        if str(a[0][1]) == n and str(a[0][0]) == str(r):
            defe = "update students set feesdue = feesdue - %s where firstname = %s and s_no = %s"
            defev = (f,n,r)
            cur.execute(defe,defev)
            print("fees successfully deposited!! ")
            conn.commit()
            school()
        else:
            print(n, " doesn't exists!!")
            school()
    except:
        print("ENTER VALID VALUE!!")
        school()

def feesdue():
    global n
    global ln
    n = str(input("enter student's firstname = "))
    ln = str(input("enter student's lastname name = "))
    check = "select * from students where firstname = %s and lastname = %s;"
    checkv = (n,ln)
    cur.execute(check,checkv)
    a = cur.fetchall()
    print(n +  "'s due fees is ", a[0][3])
    school()

def remove_student():
    global n
    global ln
    global r
    n = str(input("enter student's firstname = "))
    ln = str(input("enter student's lastname name = "))
    r = int(input("enter your student's roll number = "))
    
def school_data():
    global ln
    global j
    j1 = 2019
    j2 = 2020
    query = "select count(*) from students where joined = %s;"
    var1 = (j1,)
    var2 = (j2,)
    cur.execute(query,var1)
    a = cur.fetchall()
    a1 = a[0][0]
    cur.execute(query,var2)
    b = cur.fetchall()
    b1 = b[0][0]
    xaxis = [2017,2018,2019,2020,2021,2020]
    yaxis = [0,0,a1,b1,0,0]
    plt.bar(xaxis,yaxis)
    plt.show()


school()
