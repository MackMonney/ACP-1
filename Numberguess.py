import random
#Generate a random number between 1 and 100
number = random.randint(1, 100)

print("Guess the number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low, Try again.")
    elif guess > number:
        print("Too high, Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attemps")
        break 