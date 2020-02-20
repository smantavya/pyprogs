a = float(input('enter your temperature = '))

b = input('''if temperature is in celcius 
                       enter 'c'
             if temperature is in fahrenheit
                       enter 'f'  
your answer = ''')

if b is 'c':
    print('temperature in fahrenheit = ',((a*9/5)+32))
else:
    print('temperature in celsius = ',((a-32)*5/9))

