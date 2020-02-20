import random

#taking user's input
guess = str(input("Enter your choice:"))

#function for Game
def rps():
    global computer
    # Generating randomly from Rock Paper Scissor
    computer = random.choice(['rock','paper','scissor'])

    #Playing rock paper scissor
    if guess == computer:
        print("Draw!!")
    elif guess == 'rock':
        if computer == 'paper':
            print("Computer wins!!")
        elif computer == 'scissor':
            print('User wins!!')
    elif guess == 'paper':
        if computer == 'rock':
            print('User wins!!')
        elif computer == 'scissor':
            print('Computer wins!!')
    elif guess == 'scissor':
        if computer == 'rock':
            print('Computer wins!!')
        elif computer == 'paper':
            print('User wins!!')

    print("computer is " + computer)
    print("user is " + guess)

rps()
