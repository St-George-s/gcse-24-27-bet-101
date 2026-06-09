# procedures don't return anything
# functions return something 
# return means you get back a variable it DOES NOT mean it gets printed

# E.G.
# procedure
def printName(name):
    print(name)

# function with one parameter name
def printNameFunc(name):
    return name

# call the procedure
printName("liyana")

# call the function and print returned value
print(printNameFunc("vigdis"))

# call the function and store returned value in variable
returnedName = printNameFunc("alina")
print(returnedName)

# Q1
import math
pi = (math.pi)


def sphereVolume(radius):
    volume = 4//3 * pi * radius ** 3
    return volume

print(sphereVolume(5))
 
# Q2

numbers = [3, 8, 2, 10, 7]

def linear_search(data_list, target):
    found = False
    index = 0
    while not found and index < len(data_list:)
        print(data_list)
        if target == data_list[index]:
            print("found")
            found =  True
        else:
            index += 1
        
if found:
    print("found")
else:
    print("not found")


print(linear_search(numbers, 10))