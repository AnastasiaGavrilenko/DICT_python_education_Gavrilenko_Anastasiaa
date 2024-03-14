import random

def get_user_input():
    while True:
        user_input = input("> ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Incorrect format.")

def generate_task(level_range):
    num1 = random.randint(level_range[0], level_range[1])
    num2 = random.randint(level_range[0], level_range[1])
    operator = random.choice(['+', '-', '*'])
    task = f"{num1} {operator} {num2}"
    answer = eval(task)
    return task, answer

def save_result(name, mark, level_description):
    with open("results.txt", "a") as file:
        file.write(f"{name}: {mark}/5 in level {level_description}.\n")

def arithmetic_test():
    levels = [
        {"description": "simple operations with numbers 2-9", "range": (2, 9)},
        {"description": "integral squares of 11-29", "range": (11, 29)}
    ]

    for level in range(1, len(levels) + 1):
        print(f"Which level do you want? Enter {level} for {levels[level-1]['description']}")

        chosen_level = get_user_input()

        if chosen_level != level:
            print("Incorrect format. Please enter the correct level.")
            return

        level_description = levels[level-1]["description"]
        level_range = levels[level-1]["range"]

        correct_answers = 0

        for _ in range(5):
            task, answer = generate_task(level_range)
            print(task)

            user_answer = get_user_input()

            if answer is not None:
                result = user_answer == answer
                if result:
                    print("Right!")
                    correct_answers += 1
                else:
                    print("Wrong format! Try again.")
            else:
                print("Invalid level. Exiting the program.")
                return

        print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")

        save_result_flag = input("> ").lower()
        if save_result_flag in ['yes', 'y']:
            print("What is your name?")
            name = input("> ")
            save_result(name, correct_answers, level_description)
            print(f'The results are saved in "results.txt".')

if __name__ == "__main__":
    arithmetic_test()
