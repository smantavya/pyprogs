import mysql.connector

conn = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = '123',
    database = 'mybank',
)

def bank():
    act = int(input('''Welcome to MyBank
            press 1 to create a new account
            press 2 to deposit amount
            press 3 to withdraw amount
            press 4 for account details
            press 5 to transfer funds
            press 6 to delete account
      =  '''))
    if act == 1:
        create_account()
    elif act == 2:
        deposit_amount()
    elif act == 3:
        withdraw_amount()
    elif act == 4:
        account_details()
    elif act == 5:
        transfer_funds()
    elif act == 6:
        delete_account()

cur = conn.cursor()



def create_account():
    global n
    global ln
    global fn
    global c
    n = str(input("enter customer's first name = "))
    ln = str(input("enter customer's last name = "))
    fn = str(input("enter customer's father's name = "))
    c = int(input("enter customer's contact number = "))
    bal = 0
    crac = "insert into accounts(firstname,lastname,f_name,contactinfo,balance) values(%s,%s,%s,%s,%s);"
    cracv = (n, ln, fn, c,bal)
    cur.execute(crac,cracv)
    conn.commit()


def deposit_amount():
    global n
    n = str(input("enter customer's first name = "))
    ac = int(input("enter customer's account number = "))
    dep = int(input('enter amount to be deposited = '))
    chk = "select * from accounts where firstname = %s"
    chkv = (n, )
    cur.execute(chk,chkv)
    a = cur.fetchall()
    if n == str(a[0][1]) and str(ac) == str(a[0][0]):
        dpam = "update accounts set balance = balance + %s where firstname = %s and account_no = %s;"
        dpamv = (dep, n, ac)
        cur.execute(dpam,dpamv)
        conn.commit()
        print('Amount deposited!')
    else:
        print("this customer's account doesn't exist")

def withdraw_amount():
    global n
    n = str(input("enter customer's first name = "))
    ac = int(input("enter customer's account number = "))
    wit = int(input('enter amount to be withdrawn = '))
    chk = "select * from accounts where firstname = %s"
    chkv = (n,)
    cur.execute(chk, chkv)
    a = cur.fetchall()
    if n == str(a[0][1]) and str(ac) == str(a[0][0]):
        wdam = "update accounts set balance = balance - %s where firstname = %s and account_no = %s;"
        wdamv = (wit, n, ac)
        cur.execute(wdam,wdamv)
        conn.commit()
        print('amount withdrawn!')
    else:
        print("This Customer's account doesn't exist!")

def account_details():
    n = str(input("enter customer's first name = "))
    det = "select * from accounts where firstname = %s;"
    detv = (n,)
    cur.execute(det,detv)
    print(cur.fetchall())

def transfer_funds():
    n = str(input("enter payer's first name = "))
    ac = int(input("enter payer's account number = "))
    wit = int(input('enter amount to be transferred = '))
    n1 = str(input("enter payee's first name = "))
    ac1 = int(input("enter payee's account number = "))

    chk = "select * from accounts where firstname = %s"
    chkv = (n,)
    chkv1 =(n1,)
    cur.execute(chk, chkv)
    a = cur.fetchall()
    cur.execute(chk, chkv1)
    b = cur.fetchall()

    if n == str(a[0][1]) and str(ac) == str(a[0][0]):
            if n1 == str(b[0][1]) and str(ac1) == str(b[0][0]):
                wdam = "update accounts set balance = balance - %s where firstname = %s and account_no = %s;"
                wdamv = (wit, n, ac)
                dpam = "update accounts set balance = balance + %s where firstname = %s and account_no = %s;"
                dpamv = (wit, n1, ac1)
                cur.execute(wdam, wdamv)
                cur.execute(dpam,dpamv)
                conn.commit()
                print("Amount transferred successfully")

            else:
                print("payee's account doesn't exist!")
    else:
        print("payer's account doesn't exist!")


def delete_account():
    n = str(input("enter customer's first name = "))
    ac = int(input("enter customer's account number = "))

    chk = "select * from accounts where firstname = %s"
    chkv = (n,)
    cur.execute(chk, chkv)
    a = cur.fetchall()
    if n == str(a[0][1]) and str(ac) == str(a[0][0]):
        dtac = "delete from accounts where firstname = %s and account_no = %s;"
        dtacv = (n,ac)
        cur.execute(dtac,dtacv)
        conn.commit()
        print("Account deleted successfully!")
    else:
        print("Account doesnt't exist!")
bank()
