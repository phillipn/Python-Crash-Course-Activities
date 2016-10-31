import random
import os
import io

def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

def generate_board(word, correct_guesses, incorrect_guesses):
    clear()
    print("You have {}/7 incorrect guesses!".format(len(incorrect_guesses)))
    for letter in incorrect_guesses:
        print(letter, end=' ')
    print('\n\n')
    board = ''
    for letter in word:
        if letter in correct_guesses:
            board += (letter + ' ')
        else:
            board += '_ '
    print(board)
    return ('').join(board.split())

def game_in_progress(word, board, incorrect_guesses):
    if (word == board) or (incorrect_guesses > 6):
        return False
    else:
        return True

def game_over_prompt(status, word):
    print("The secret word was {}".format(word))
    choice = input("You {}!!! Play again? Y/n ".format(status))
    if choice != 'n':
        hangman()

def user_guess_valid(letter, correct_guesses, incorrect_guesses):
    if not letter:
        print("Please input a letter...")
        return False
    elif not letter.isalpha():
        print("Need a letter, not a number...")
        return False
    elif len(letter) > 1:
        print("Need just one letter...")
        return False
    elif (letter in correct_guesses) or (letter in incorrect_guesses):
        print('You have already guessed this letter')
        return False
    else:
        return True

def hangman():
    clear()
    status = "lose"
    lines = []
    incorrect_guesses = []
    correct_guesses = []

    with open('./dictionary.txt') as f:
        lines = f.read().lower().splitlines()

    random_word = random.choice(lines)
    user_board = generate_board(random_word, correct_guesses, incorrect_guesses)

    while game_in_progress(random_word, user_board, len(incorrect_guesses)):
        user_guess = input('Guess a letter ').lower()

        if not user_guess_valid(user_guess, correct_guesses, incorrect_guesses):
            continue

        if user_guess in random_word:
            correct_guesses.append(user_guess)
        else:
            incorrect_guesses.append(user_guess)

        user_board = generate_board(random_word, correct_guesses, incorrect_guesses)

        if user_board == random_word:
            status = "win"
    else:
        game_over_prompt(status, random_word)

hangman()
