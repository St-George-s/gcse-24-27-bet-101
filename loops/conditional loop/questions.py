# #Q1
# code = "rzy"
# code = input("enter THE code: ")
# while code != "rzy":
#     code = input("enter THE code: ")
#     print("welcome in !!!!!!!!!!!!!!!!!!!")

#Q2
# code = "4003"
# userCode = input("enter THE code: ")
# while userCode != "4003":
#     userCode = input("enter THE code: ")
#     print("CODE ACCEPTED.")

#Q3
# age = "14"
# usersage = input("enter your age: ")
# while usersage >= "14":
#     usersage = input("enter your age: ")
#     print("age allowed on so cmon in")

#Q4
# password = input("input a password: ")
# while len(password) < 5:
#     print("too short make it longer")
#     password = input("enter password again: ")
# print("password accepted.")

#Q5
# wanttowatchstuff = input("want to watch another episode of modern family (Y/N):  ")
# while wanttowatchstuff == "Y":
#     print("okay on it")
#     wanttowatchstuff = input("want to watch another episode of modern family (Y/N):  ")
# print("good now sleep")

#Q6
money = int(input("how much of your money can i have?: "))
while money < 100:
    print("no, BUDDY i need more.")
    money = money + int(input("how much of your money can i have?: "))
print("thanks")
print("you have given me", money, "thanks")
