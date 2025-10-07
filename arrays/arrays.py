#to create an array you use []
heights = [10, 20, 32, 10]
names = ["maggie", "elizabeth", "alina"]
#arrays start at index 0 reference the index by []
print(names[1])
print(heights[2])
#loop over names array and print
for counter in range(len(names)): #len gets the length or the variable you attach it to-
    print(names[counter]) #counter is 0 then 1 then 2
    print(heights[counter])

#append is the same as add but heres how you add to the end of the array
heights.append(55)
names.append("muskaan")

print(heights)
print(names)