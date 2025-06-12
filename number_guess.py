import random

print("I am thinking of a number between 1 and 100. What number is it?")

# Takes a random number in the range 1 and 100 and stores it in a variable
random_number = random.randint(1, 100)

# Calling variables for the number guess and the number of attempts to guess correctly
guess = 0
attempts = 0

# Main game loop
while guess != random_number:
    guess = input("Guess the number: ")
    try:
        guess_int = int(guess)
        if guess_int > 0:
            if guess_int > random_number:
                print("Too high! Try again.")
                attempts += 1
            elif guess_int < random_number:
                print("Too low! Try again.")
                attempts += 1
            else:
                attempts += 1
                print("You guessed correctly after " + str(attempts) + " attempts! Congrats!")
                break
        else:
            print("Invalid input! Please enter positive integers only")
    except ValueError:
        print("Invalid input! Please enter positive integers only")