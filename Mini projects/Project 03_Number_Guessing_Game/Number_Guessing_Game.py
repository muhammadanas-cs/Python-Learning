import random

print("\nWelcome to Number Guessing Game!")
print("\nI have selected a number between 1 and 100")
print("\nTry to guess it!")

number = random.randint(1,100)
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess < number:
        print("Too low! Try Again.")
    elif guess > number:
         print("Too high! Try Again.")
    else:
        print(f"Correct! You guessed it in {tries} attempts")
        break