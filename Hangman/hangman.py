# hangman.py
import random
def choose_word():
    word_list = ['python', 'java', 'javascript', 'php']
    return random.choice(word_list)
def display_word(word, revealed_letters):
    displayed_word = ""
    for letter in word:
        if letter in revealed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word
def main():
    while True:
        print("HANGMAN")
        user_choice = input('Type "play" to play the game, "exit" to quit: > ')
        if user_choice == "exit":
            break
        if user_choice != "play":
            print("Please enter a valid choice.")
            continue
        word = choose_word()
        revealed_letters = []
        attempts = 8
        print(display_word(word, revealed_letters))
        while attempts > 0:
            guess = input("Input a letter: > ")
            if len(guess) != 1:
                print("You should input a single letter")
                continue
            if not guess.isalpha() or not guess.islower():
                print("Please enter a lowercase English letter")
                continue
            if guess in revealed_letters:
                print("You've already guessed this letter")
                continue
            if guess in word:
                revealed_letters.append(guess)
                displayed = display_word(word, revealed_letters)
                print(displayed)
                if displayed == word:
                    print(f"Congratulations! You've guessed the word {word}!")
                    break
            else:
                print("That letter doesn't appear in the word")
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
if __name__ == "__main__":
    main()
