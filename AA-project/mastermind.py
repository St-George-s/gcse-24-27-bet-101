import random

mastermind = str(random.randint(1000,9999))
counter = 0
print(mastermind)

playerGuess = str(input("what is your guess?(4 NUMBERS)   "))
while len(playerGuess) != 4:
    print("THAT IS NOT RIGHT. 4 NUMBERS!!!!!!!!")
    playerGuess = str(input("what is your guess?(4 NUMBERS)   "))
while playerGuess != mastermind:
    for letter in playerGuess:
        print(letter)
        if letter in mastermind:
            print("this is correct")
        elif playerGuess == mastermind:
            print("you are fully correct!")
        else:
            print("this is wrong")
    counter = counter + 1
    print("try again")
    print("you have tried", counter, "time(s), not too good")
    playerGuess = input("would you like to guess again?(numbers again) ")
    while len(playerGuess) != 4:
        print("THAT IS NOT RIGHT. 4 NUMBERS!!!!!!!!")
        playerGuess = str(input("what is your guess?(4 NUMBERS)   "))
print("congrats!! you pass")
 
     