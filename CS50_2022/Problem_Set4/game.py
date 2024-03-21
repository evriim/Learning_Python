"""Making predictions from a randomly generated range of positive numbers"""
import random
while True:
    #Level determination consisting of positive numbers
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass

number = int(random.uniform(1, level))

while True:
    #Guess the number
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except (ValueError, RecursionError):
        pass
    