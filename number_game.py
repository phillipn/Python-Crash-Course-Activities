# Game where computer picks a number 1-10, and you try and guess it within 5 turns

import random

def play_again_prompt(result):
    play_again = input("You are a {}! Play again? Y/n ".format(result.upper()))
    if play_again != "n":
        number_game()
    else:
        return False

def game_in_progress(guesses, status):
    if (len(guesses) > 4) or (status == "winner"):
        return False
    else:
        return True

def number_game():
    secret_number = random.randint(1, 10)
    guesses = []
    status = ""

    while game_in_progress(guesses, status):
        try:
            guess = int(input("Guess a number between 1 and 10 "))
        except ValueError:
            print("{} isn't a number. Guess again!".format(guess))
        else:
            if guess == secret_number:
                status = "winner"
                continue
            elif guess < secret_number:
                print("Too low")
            elif guess > secret_number:
                print("Too high")

            guesses.append(guess)
    else:
        if status == "winner":
            play_again_prompt("winner")
        else:
            play_again_prompt("loser")

number_game()
