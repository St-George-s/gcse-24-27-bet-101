cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
populations = [8908, 482, 366, 341, 635] #this pair are a parallel array as they are same length

# for counter in range(len(cityNames)):
#     print(cityNames[counter], "has a population of", populations[counter])
# NOTE: linear search is going one at a time through the data
#linear search example
found = False
userCity = input("what city would you like the population for?   ")
for counter in range(len(cityNames)):
    if userCity == cityNames[counter]:
        print(cityNames[counter], "has a population of", populations[counter])
        found = True
#if instead of commas you use a plus then know you have to clarify string and interger
if not found:
    print("your city was not found")