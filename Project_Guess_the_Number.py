#Guess the number

#importing random module
import random

answer = random.randint(0,20)

#asking user to guess
def guess_number():
    global number
    global answer
    number = int(input("enter your guess = "))
    # checking if number is right
    if number < answer:
        print("You guessed a smaller number, Try Again!!")
        guess_number()
    elif number > answer:
        print("You guessed a higher number, Try Again!!")
        guess_number()
    elif number == answer:
        print("You guessed it right. Voila!!")


guess_number()


