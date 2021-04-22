import random

randomNumber = random.randint(1, 100)
# print(randomNumber)
userGuess = None
guesses = 0

while(userGuess != randomNumber):

    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randomNumber):
        print("You guessed it right!")

    else:
        if (userGuess>randomNumber):
            print("You guessed it wrong! Enter smaller Number")
        
        else:
            print("You guessed it wrong! Enter larger Number")
    

print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the High Score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
