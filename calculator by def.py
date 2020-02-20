a = int(input('first number = '))
b = int(input('second number = '))

def add():
    print(a + b)
def subtract():
    print(a - b)
def multiply():
    print(a * b)
def divide():
    print(a/b)
def percentage():
    print(a/b*100)

opt = input('''
        Enter your operation
        + for addition
        - for subtraction
        x for multiplication
        / for division
        % for percentage
             ''')

if opt == '+':
    add()
if opt == '-':
    subtract()
if opt == 'x':
    multiply()
if opt == '/':
    divide()
if opt == '%':
    percentage()
