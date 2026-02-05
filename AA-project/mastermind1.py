import random
counter = 0

mode = str(input("what mode do you want to play?(hard/easy)   "))
if mode == "hard":
    mastermind = str(random.randint(10000,99999))
    playerGuess = str(input("what is your guess?(5 NUMBERS)   "))
    while len(playerGuess) != 4:
        print("THAT IS NOT RIGHT. 5 NUMBERS!!!!!!!!")
    playerGuess = str(input("what is your guess?(5 NUMBERS)   "))
elif mode == "easy":
    mastermind = str(random.randint(1000,9999))
    print(mastermind)
    playerGuess = str(input("what is your guess?(4 NUMBERS)   "))
    while len(playerGuess) != 4:
        print("THAT IS NOT RIGHT. 4 NUMBERS!!!!!!!!")
        playerGuess = str(input("what is your guess?(4 NUMBERS)   "))

    while playerGuess != mastermind:
        matchedChars = []
        foundAMatch = False
        for index in range(len(mastermind)):
            for indexTwo in range(len(playerGuess)):
                # If the letters match
                if mastermind[index] == playerGuess[indexTwo]:
                    if mastermind[index] not in matchedChars:
                        matchedChars.append(mastermind[index])
                        foundAMatch = True
                        #  Letters match
                        if index == indexTwo:
                            # Positions match
                            print(mastermind[index], " is correct and in the right posistion")
                        elif index != indexTwo:
                            # Positions don't match
                            print(mastermind[index], " is correct and in the wrong posistion")

        if not foundAMatch:
            print("No matches, you are rubbish")
        counter = counter + 1
        print("try again")
        print("you have tried", counter, "time(s), not too good")
        playerGuess = input("would you like to guess again?(numbers again) ")
        while len(playerGuess) != 4:
            print("THAT IS NOT RIGHT. 4 NUMBERS!!!!!!!!")
            playerGuess = str(input("what is your guess?(4 NUMBERS)   "))
    print("congrats!! you pass")
else:
    print("that is not a mode. please select again")
    mode = str(input("what mode do you want to play?(hard/easy)   "))

# Extensions: 
# 1. Let the user pick an easy mode which shows the user which position that they guessed correctly
# 2. Let the user pick a hard mode that gives five digits instead of four
# After the game is finished, ask the user for their name and input their score into a table. Show them the high score at the st0art of the game so that it gives a sense of competition.