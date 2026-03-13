trainingdata = str("2\n" + "New Trent Park\n" + "True\n" + "12.7\n") 
trainingdata = ["2", "New Trent Park", "True", "12.7"]
print("Venue is: ", trainingdata[1], "\n")
with open("allsessions.txt", "w") as file:
    for value in trainingdata:
        file.write(value + "\n")
    
# [Data recorded	Example data
# Number of goals scored	2
# Training venue	New Trent Park
# Session completed (True/False)	True
# Best sprint time (seconds)	12.7

# Finish the algorithm below to add the new trainingdata to the text file. 4]