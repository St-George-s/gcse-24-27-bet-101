phrase = str(input("What is the phrase you would like to translate? "))
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
morseCode = [".-", "-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","|"]
myMorseCodeString = ""
i=0
trans={}
for letter in alphabet:
    trans[letter]=morseCode[i]
    i=i+1
for letter in phrase:   
    myMorseCodeString = myMorseCodeString + " " + (trans[letter])
print(myMorseCodeString)

#DAD VERSION
