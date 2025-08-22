#!/usr/bin/env python3

from game import play_game

def main():
    """The main entry point for the application."""
    while True:
        play_game()
        while True:
            play_again = input("Play again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
