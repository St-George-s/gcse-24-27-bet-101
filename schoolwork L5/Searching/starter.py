def search(searchValue, searchList, names):
    found = False 
    index = 0

    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            print("found")
            found = True
        else:
            index += 1

    if found:
         print("found at", index)
         print("student is", names[index])
    else:
         print("not found")

# call it
search(False, [True, True, False], ["jessie", "debbie", "maggie"])