# Game where you pick a number 1-10, and the computer tries to guess it within 5 turns
import random

def request_number():
    try:
        your_number = (int(input("Pick a number 1-10: ")))
        if (your_number >10) or (your_number<1):
            raise ValueError
    except ValueError:
        print("Pick a number between 1 and 10, FOOL! ")
        request_number()
    else:
        return your_number

def game_in_progress(guesses, status):
    if (len(guesses) > 4) or (status):
        return False
    else:
        return True

def game_over_prompt(status):
    if status != "lose":
        print("WINNER!!! Computer did not guess your number!")
    else:
        print("LOSER!!! Computer guessed your number!")

    play_again = input("Play again? Y/n ")
    if play_again != 'n':
        number_game()

def number_game():
    guesses = []
    status = ""
    number = request_number()

    while game_in_progress(guesses, status):
        random_guess = random.randint(1,10)
        print("Computer guesses " + str(random_guess))
        if random_guess == number:
            status = "lose"
            continue
        else:
            guesses.append(random_guess)
    else:
        game_over_prompt(status)


number_game()
