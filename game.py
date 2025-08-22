import random

def play_game():
    """The main game logic for the number guessing game."""
    number_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess_str = input("Your guess: ")
            guess = int(guess_str)

            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number, which was {number_to_guess}.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
