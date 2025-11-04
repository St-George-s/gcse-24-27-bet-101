
#Q1
# string = input(str("enter a string: "))
# print(string[0])
# print(string[-1])

#Q2
# myString = "hello"
# reversedString = ""
# for character in myString:
#     reversedString = character + reversedString

# print(reversedString)

#Write a Python program to check if a string is a palindrome (reads the same forward and backward). 
#Q3
# myString = "hello"
# reversedString = ""
# for character in myString:
#     reversedString = character + reversedString

# print(reversedString == myString)






#Q6
# import random
# myRandom = random.randint(1, 6)

# print(myRandom)

import random
diceUno = random.randint(1, 6)
diceDos = random.randint(1, 6)
print(str(diceUno), "+", str(diceDos), "=")
print(str(diceUno + diceDos))  