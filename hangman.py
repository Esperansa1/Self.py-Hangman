
import os
from hangman_photos import HANGMAN_PHOTOS

def print_hangman():
    print(
    """
            Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ ___
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_  |
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/
    """)

def clear_screen():
    os.system('cls')

def check_win(secret_word, old_letters_guessed):
    print(secret_word)
    for letter in secret_word.lower():
        if letter not in old_letters_guessed:
            print(letter, old_letters_guessed)
            return False
        
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ""

    for letter in secret_word:
        if letter.lower() in old_letters_guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "

    return hidden_word


def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed_string =  ' '.join(sorted(old_letters_guessed))
        print(f"X\n{old_letters_guessed_string})")
        return False
    old_letters_guessed.append(letter_guessed.lower())
    return True


def choose_word(file_path, index):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            if 0 <= index < len(words):
                return words[index]
            else:
                print(f"Index out of range: {index}")
    except FileNotFoundError:
        print(f"File path {file_path} was not found")

def main():
    print_hangman()

    path = input("Path to word file: ")

    try:
        word_index = int(input("Enter word index: "))
    except ValueError:
        print("Invalid input for word index (Integer needed)")
        return

    path = path + ".txt" if not path.endswith(".txt") else path
    word = choose_word(path, word_index)
    if word == None:
        return

    clear_screen()

    old_letters_guessed = []
    num_of_tries = 0
    MAX_TRIES = 6

    while num_of_tries < MAX_TRIES:
        print(HANGMAN_PHOTOS[num_of_tries])
        print(show_hidden_word(word, old_letters_guessed))

        letter_guessed = input("Guess a letter: ").lower()

        if letter_guessed in word.lower() and try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if check_win(word, old_letters_guessed):
                print(f"You win!! The word was: {word}")
                return
        else:
            num_of_tries += 1
        clear_screen()
    else:
        print(f"You lost!! The word was: {word}")



if __name__ == '__main__':
    main()