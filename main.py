import random

chances = 5
numb = random.randint(0,9)
guess = int(input("Enter a phrase (Must be from 0-9) : "))

while chances<=5:   
 
    if (guess == numb):
        print("Congrats you got it!")
        chances = 6
    else:
        print("Wrong guess, try again!")
        chances = chances - 1
        
    guess = int(input("Enter a phrase (Must be from 0-9) : "))

