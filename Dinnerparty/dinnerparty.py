import random


def get_friends_count():
    count = int(input("Enter the number of friends joining (including you):\n> "))
    if count <= 0:
        print("No one is joining for the party")
        return 0
    return count


def get_friends_names(count):
    print("Enter the name of every friend (including you), each on a new line:")
    return [input("> ") for _ in range(count)]


def calculate_bill_per_person(total_amount, count, lucky_one=None):
    if lucky_one is not None:
        return round(total_amount / (count - 1), 2)
    return round(total_amount / count, 2)


def main():
    friends_count = get_friends_count()
    if friends_count == 0:
        return

    friends_names = get_friends_names(friends_count)
    total_amount = float(input("Enter the total amount:\n> "))

    lucky_one = None
    if input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n> ").lower() == 'yes':
        lucky_one = random.choice(friends_names)
        print(f"{lucky_one} is the lucky one!")

    bill_per_person = calculate_bill_per_person(total_amount, friends_count, lucky_one)
    friends_bills = {name: 0 if name == lucky_one else bill_per_person for name in friends_names}

    print(friends_bills)


main()

