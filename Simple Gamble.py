import random

NumberToGuess = (random.randrange(1, 10))

 

print("Welcome to guess the Number")

print("range from 1 to 10")
print("whats your number?")
GuessedNumber = input()

if NumberToGuess == NumberToGuess:
    print("You Won!")    
else:
    print("you Lose!")