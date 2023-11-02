print("Hello! My name is DICT_Bot.")
print("I was created in 2020.")
name = input("Please, remind me your name. > Anastasia\n")
print(f"What a great name you have, Anastasia {name}!")
print("Let me guess your age.")
remainder3 = int(input("Enter remainders of dividing your age by 3: "))
remainder5 = int(input("Enter remainders of dividing your age by 5: "))
remainder7 = int(input("Enter remainders of dividing your age by 7: "))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
num = int(input("Enter a positive number: "))
for i in range(num + 1):
    print(f"{i} !")
print("Completed, have a nice day!")

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = "2"
while True:
    answer = input("Enter the number of your answer (1/2/3/4): ")
    if answer == correct_answer:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")

