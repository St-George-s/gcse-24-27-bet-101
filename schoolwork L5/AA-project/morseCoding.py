phrase = str(input("What is the phrase you would like to translate? "))
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morseCode = [".-", "-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","|"]
myMorseCodeString = ""
for letter in phrase:
    for index in range(len(alphabet)):
        if letter == alphabet[index]:
            myMorseCodeString = myMorseCodeString + " " + (morseCode[index])
print(myMorseCodeString)
