x = int(input("Enter 1th number "))
y = int(input("Enter 2th number "))

opt = input('''
        Enter your operation
        + for addition
        - for subtraction
        x for multiplication
        / for division
        % for percentage
             ''')


if opt == '+':
    print(x+y)
if opt == '-':
    print(x-y)
if opt == 'x':
    print(x*y)
if opt == '/':
    print(x/y)
if opt == '%':
    print(x/y*100)


