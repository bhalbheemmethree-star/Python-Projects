
import random

secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("     NUMBER GUESSING GAME       ")
print("================================")
print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")


while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number :
        print("Too High! Try again.")
    elif guess < secret_number:
        print("Too Low! Try again.")
    else:
        print(f"correct! The number was {secret_number}.")
        print(F"Attempts: {attempts}")
        break

    