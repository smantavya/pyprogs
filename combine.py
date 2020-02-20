def program():
    a = int(input('''
            enter 1 for armstrong number
                  2 for prime number
                  3 for consonants and vowels game
                  4 for calculator
                  '''))
    if a == 1:
        armstrong()
    elif a == 2:
        prime()
    elif a == 3:
        game()
    elif a == 4:
        cal()
    else:
        again()

def again():
    p = input("y for continue n for exit")

    if p =='y':
        program()
    elif p == 'n':
        quit()
    else:
        again()



def armstrong():
    a = input('a for single digit and b for range')
    if a == 'a':
        armstrong_single()
    if a == 'b':
        armstrong_range()

def armstrong_single():
    n = int(input("your number here "))

    ln = len(str(n))
    s = 0
    temp = n

    while temp > 0:
        d = temp % 10
        s = s + (d ** ln)
        temp = temp//10

    if s == n:
        print("this is an armstrong number")
    else:
        print("this is not an armstrong number")
    again()

def armstrong_range():
    a = int(input('start = '))
    b = int(input('end = '))

    for n in range(a,b+1):
        ln = len(str(n))
        s = 0
        temp = n

        while temp > 0:
            d = temp % 10
            s = s + (d ** ln)
            temp = temp//10

        if s == n:
            print(n)
    again()

def prime():
    a = input('a for single digit and b for range')
    if a == 'a':
        prime_single()
    if a == 'b':
        prime_range()
    again()

def prime_single():
    n = int(input('your number here = '))
    a = 2
    while a < n:
        if n % a == 0:
            print(n,'is not a prime number')
            a = a+1
            break
        else:
            a = a + 1

    if a == n:
        print(n,'is a prime number')
    again()

def prime_range():
    n = int(input('your number here = '))
    for a in (2,n):
        if n % a == 0:
             print(n,'is not a prime number')
             break
        else:
            continue

    else:
        print(n,'is a prime number')
    again()

def game():
    a = input('enter your word = ')
    a = a.upper()

    c = 0
    # c will gain point for every consonants
    v = 0
    # v will gain point for every vowels

    n = 0
    # n is index number in 'a'

    l = len(a)

    while n < l:
        if a[n] in ('AEIOU'):
            v = v + (l-n)
            n = n + 1
        else:
            c = c + (l-n)
            n = n + 1

    print('points for c =',c)
    print('points for v =',v)

    if c > v:
        print('KO! c wins!')
    else:
        print('KO! v wins!')
    again()

def cal():
    a = int(input('first number = '))
    b = int(input('second number = '))

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
    again()
program()
