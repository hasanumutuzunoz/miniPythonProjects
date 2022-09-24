from random import *

print("Welcome to my dice roll program")

while True:
    userRequest = str(input("To roll the dice, type \"roll\"\n"))
    if userRequest == "roll":
            print(randint(1,6))
    else:
        print("program ended without roll")
        break
