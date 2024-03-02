import random


def load_rating():
    try:
        with open("rating.txt", "r") as file:
            lines = file.readlines()
            return {line.split()[0]: int(line.split()[1]) for line in lines}
    except FileNotFoundError:
        return {}

def update_rating(name, points):
    ratings[name] += points

def save_rating():
    with open("rating.txt", "w") as file:
        for name, points in ratings.items():
            file.write(f"{name} {points}\n")

def determine_winner(user_choice, computer_choice, options):
    half = len(options) // 2
    if user_choice == computer_choice:
        return "Draw"
    elif user_choice in options[options.index(computer_choice)+1:][:half]:
        return "Win"
    else:
        return "Lose"

def play_game():
    print("Okay, let's start")
    while True:
        user_input = input("> ").lower()
        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {ratings[user_name]}")
        elif user_input:
            user_choice = user_input
            computer_choice = random.choice(options)
            print(f"Computer chose {computer_choice}")
            result = determine_winner(user_choice, computer_choice, options)
            if result == "Win":
                print(f"Well done. The computer chose {computer_choice} and failed")
                ratings[user_name] += 100
            elif result == "Lose":
                print(f"Sorry, but the computer chose {computer_choice}")
            else:
                print(f"There is a draw ({user_choice})")

            save_rating()

if __name__ == "__main__":
    print("Enter your name: ", end="")
    user_name = input()
    print(f"Hello, {user_name}")

    ratings = load_rating()

    print("Enter options separated by commas (or press Enter for default options): ", end="")
    user_options = input().lower()
    options = user_options.split(",") if user_options else ["rock", "paper", "scissors"]

    ratings.setdefault(user_name, 0)

    play_game()
