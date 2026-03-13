counter = 0
with open("/workspaces/gcse-24-27-bet-101/fileHandling/fileHandlingQuestions/fileUno.txt", "r") as file:
    for line in file:
         print(line)
         counter = counter + 1
    print("there are", counter, "lines")

