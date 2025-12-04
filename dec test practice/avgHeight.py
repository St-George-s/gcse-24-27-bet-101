# counter = 0
# totalHeight = 0

# for i in range(4): 
#     height = int(input("height? "))
#     totalHeight = totalHeight + height
#     counter = counter + 1

# print("average is:", totalHeight / counter)

countA = 0


while countA < 3: 
    word = input("input a word:   ") 
    countA = 0  
    for letter in word: 
        if letter == "a" or letter == "A":
            countA = countA + 1 