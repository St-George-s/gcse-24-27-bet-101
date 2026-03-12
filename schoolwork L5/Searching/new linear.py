# linear search
# create an array

names = ["debbie", "jessie", "vigdis", "emilia"]
searchValue = "emilia"
found = False
index = 0

# conditional loop that stops when
# 1. - search value is found
# 2. - the search is at the end of the array

while not found and index < len(names):
    if searchValue == names[index]:
        found == True
    else:
        index += 1

# after the loop (unindent)

if found:
    print("found")
else:
    print("not found")