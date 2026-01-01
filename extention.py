#HANGMAN!
#Create a version of the Hangman game using Lists. The program should ask for the word to guess and the number of chances to be given. 
#For every guess you should update the user with which letters they have guessed incorrectly, as well as replacing the letters in the guess word with the ones they have guessed correctly.  
#You should also show the user how many chances they have left. 
# Optional Extensions:  
#     1.     Make sure that you do not let the user lose a life if they guess a letter that they have already guessed.

yourWord = str(input("What is your word?   "))
yourChances = int(input("How many chances do you want?  "))
yourGuess = str(input("What is your guess?  "))

for counter in range(yourChances):
    user_input = input(yourGuess).strip()  # Remove spaces
    if len(user_input) == 1 and user_input.isalpha():
        print(f"You entered: {user_input}")
    else:
        print("Invalid input. Please enter exactly one letter (A-Z).")



# myString = "hiya!"
# print(myString[0])
# print(myString[0:m])
# print(myString[-1])
# print(myString[-3:])


#substrings