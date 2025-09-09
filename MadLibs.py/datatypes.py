#data types
name = "liz" #a string
myAge = 10 #a integer
height = 100 #a float/reel
hasADriversLicense = True #a boolean (True/False question)

# casting = changing from data types
age = input("enter an age: ")
print(age)
print(age + "10") #concatenate 2 strings together (join them together)
ageAsAnInt = int(age) 
print(ageAsAnInt + 10) # add two integers together (maths addition)
print("your age is " + str(ageAsAnInt))

#data types - more examples
stillAnInteger = -4 #an integer
myNumber = "0706040030" #phone numbers should be stored as a string bc they start with a 0

#arithmetic operators (operator is +, -, *, /, //, %)
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
divide = 10 / 10 #will output (answer) as a float
integerDivision = 10 // 10 #forces output to be an integer+
print(add, subtract, multiply, divide, integerDivision)
modulo = 5 % 41 #modulo is the leftover of the division
print(modulo)
exponent = 2 ** 3 #exponent is to the power of
print(exponent)


#activity 1 - take two inputs multiply them together and output answer

input1 = float(input("enter a input: "))
input2 = float(input("enter a input: "))
multiply = int(input1) * int(input2)
print(multiply)

#activity 2 - input users age, output age times 7

usersage = input("enter a new age: ")
multiply2 =  int(usersage) * 7
print(multiply2)

#activity 3 - take radius as input, output volume of sphere (v = 4/3 x pi x r^^3)

radius = float(input("input a radius: ")) 
multiply3 = int(radius) ** 3 * 3.14159 * 4 / 3
print(multiply3)