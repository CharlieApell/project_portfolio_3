# import random and a list of word for the program to randomly choose from
import random
import colorama
from colorama import Fore
from words import words_list


colorama.init(autoreset=True)


# function that returns a random word from the word list in uppercase
def get_word():
    word = random.choice(words_list)
    return word.upper()



print(" _   _")
print("| | | |")
print("| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __")
print("|  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\")
print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("                    __/ |")
print("                   |___/")
print("\n")

user_name = input("What's your name? ")


# gameplay will run until the word is right or the user runs out of tries
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f"Let's play Hangman, {user_name}! Guess the city!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(f"{Fore.RED}Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")


# Win or lose message
    if guessed:
        print(f"{Fore.GREEN}Congratulations! You guessed it right! You win!\n")
    else:
        print(f"{Fore.RED}Aaaw, sorry, you ran out of tries!\n")
        print("the word was " + word + ". Better luck next time!\n")


def display_hangman(tries):
    stages = [  # final: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |      |\\
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
