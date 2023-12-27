class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def display_status(self):
        print(f"The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.disposable_cups} disposable cups")
        print(f"${self.money} of money")

    def buy_coffee(self, choice):
        coffee_types = [
            {"name": "espresso", "water": 250, "milk": 0, "coffee_beans": 16, "cost": 4},
            {"name": "latte", "water": 350, "milk": 75, "coffee_beans": 20, "cost": 7},
            {"name": "cappuccino", "water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
        ]

        coffee_type = coffee_types[choice - 1]

        if self.water < coffee_type["water"]:
            print("Sorry, not enough water!")
        elif self.milk < coffee_type["milk"]:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < coffee_type["coffee_beans"]:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making coffee!")
            self.water -= coffee_type["water"]
            self.milk -= coffee_type["milk"]
            self.coffee_beans -= coffee_type["coffee_beans"]
            self.disposable_cups -= 1
            self.money += coffee_type["cost"]

    def fill_resources(self, water, milk, coffee_beans, disposable_cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.disposable_cups += disposable_cups

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def process_input(self, user_input):
        if user_input == "remaining":
            self.display_status()
        elif user_input == "buy":
            coffee_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
            if coffee_choice in ("1", "2", "3"):
                self.buy_coffee(int(coffee_choice))
        elif user_input == "fill":
            water = int(input("Write how many ml of water you want to add:\n"))
            milk = int(input("Write how many ml of milk you want to add:\n"))
            coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
            disposable_cups = int(input("Write how many disposable cups of coffee you want to add:\n"))
            self.fill_resources(water, milk, coffee_beans, disposable_cups)
        elif user_input == "take":
            self.take_money()
        elif user_input == "exit":
            return False
        return True

    def run(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if not self.process_input(action):
                break


coffee_machine = CoffeeMachine()
coffee_machine.run()
