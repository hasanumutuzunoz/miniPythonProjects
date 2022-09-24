from random import *
number = randint(1,5)
chance = 3

print("Welcome to my game \nYou need to guess my number between 1 to 5 \nBut beware! You only have 3 chance! \n")
while chance > 0:
    chance -= 1
    playerGuess = int(input("Enter a number between 1 to 5\n"))

    if (chance == 2 and (playerGuess > 5 or playerGuess < 1)):
        chance += 1
        print("You need to enter a number between 1 to 5, I won't decrease your attempt for now\n"
              "You still have %i chance to win the game\n" %(chance))
        continue

    if playerGuess == number:
        print("YOU GUESSED RIGHT!!! YOU WIN THE GAME!")
        chance += 10
        break
    else:
        print("Wrong number. You have %i chance left" %(chance))

if chance == 0:
    print("You lost the game!")