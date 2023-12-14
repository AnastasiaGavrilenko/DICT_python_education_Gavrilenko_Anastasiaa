def validate_player_name(input_value):
    if input_value not in ["John", "Jack"]:
        return "Choose between 'John' and 'Jack'"
    return None
import random
def validate_pencils(input_value):
    if not input_value.isnumeric():
        return "The number of pencils should be numeric"
    pencils_count = int(input_value)
    if pencils_count <= 0:
        return "The number of pencils should be positive"
    return None
while True:
    pencils_input = input("How many pencils would you like to use:\n> ")
    validation_result = validate_pencils(pencils_input)
    if validation_result is None:
        break
    else:
        print(validation_result)
while True:
    player_input = input("Who will be the first (John, Jack):\n> ")
    validation_result = validate_player_name(player_input)
    if validation_result is None:
        break
    else:
        print(validation_result)
pencils_count = int(pencils_input)
current_player = player_input
while pencils_count > 0:
    if current_player == "Jack":
        if pencils_count % 4 == 0:
            taken_pencils = random.randint(1, 3)
        else:
            taken_pencils = pencils_count % 4
        print(f"{current_player}'s turn: {taken_pencils}")
    else:
        while True:
            taken_pencils_input = input(f"{current_player}'s turn:\n> ")
            validation_result = validate_pencils(taken_pencils_input)
            if validation_result is None:
                taken_pencils = int(taken_pencils_input)
                if taken_pencils > 3 or taken_pencils < 1 or taken_pencils > pencils_count:
                    print("Possible values: '1', '2' or '3'")
                    continue
                break
            else:
                print(validation_result)
    pencils_count -= taken_pencils
    print("|" * pencils_count)
    current_player = "John" if current_player == "Jack" else "Jack"
winner = "John" if current_player == "Jack" else "Jack"
print(f"{winner} won!")
