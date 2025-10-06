# #Q1
# temperature = int(input("whats the temperature?  "))
# sun = str(input("is it sunny (Y/N):  "))

# if temperature > 15 and sun == "Y":
#     print("YAYAYAYAYAYAYYAYAYAYYAYAY")
# elif temperature < 15 and sun == "N":
#     print("big loss")
# elif temperature > 15:
#     print("good for you! go get burned")
# if sun == "N":
#     print("awweeee")
# elif sun == "Y":
#     print("pretty")
# if temperature <= 15:
#     print("brrr")

#Q2
# temperature = int(input("what is the temperature?  "))
# rain = input("is it raining?  ")
# if temperature > 15 or rain == "yes":
#     print("hot or wet")

#Q3
# apples = int(input("how many apples?  "))
# if apples <= 10:
#     print("hungry dawwg")

#Q4 
# age = int(input("how many years, bro?  "))
# licensed = input("do you have a license? (Y/N)?  ")
# if age > 18 and licensed == "Y":
#     print("you can drive fren")

#Q5
# speed = int(input("how fast are you going?  "))
# rain = input("is it raining? (Y/N) ")
# if speed > 60 or rain == "N":
#     print("fast or dry. That's an odd condition")

#Q6
# hours = int(input("how long have you studied?  "))
# prepd = input("are you prepared? (Y/N) ")
# if hours > 5 or prepd == "Y":
#     print("lots of revision or feel prepared anyway but may perish")

# Q7
# completed = int(input("how many assignments completed?  "))
# pending = int(input("how mamy still to go?  "))
# if completed > 5 and pending < 2:
#     print("Nearly there")

    
# Q8
# savings = int(input("how much have you saved?  "))
# price = int(input("how much does it cost?  "))
# itemOnSale = true # you didn't say how this is set
# if savings > price or itemOnSale:
#     print("Time to go shopping - yay")
    
# Q9
# Dad says error checking is basic coding skill - users are evil
sunny = "invalid"
while (sunny != "Y" and sunny != "N"):
    sunny = input("is it sunny or not? (Y/N)")
weekend = "invalid"
while (weekend != "Y" and weekend != "N"):
    weekend = input("is it a weekend? (Y/N)? ")
if (sunny == "Y" and weekend == "Y") or (sunny == "N" and weekend == "N"):
    print("let's go to the beach, let's go to the waves, waves, wave. What are they going to say? Starships...")

