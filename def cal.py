def agina():
    p = input("y for conti n fpor exit")

    if p =='y':
        cal()
    elif p == 'n':
        quit()
    else:
        agina()

def cal():
    try:
        a = int(input('first number = '))
        b = int(input('second number = '))
    except:
        print("plz enter number :-   ")
        cal()

    else:
        opt = input('''
                Enter your operation
                + for addition
                - for subtraction
                x for multiplication
                / for division
                % for percentage
                     ''')

        if opt == '+':
            print(a+b)
        if opt == '-':
            print(a-b)
        if opt == 'x':
            print(a*b)

        if opt == '/':
            print(a/b)
        if opt == '%':
            print(a%b)
    agina()
cal()
