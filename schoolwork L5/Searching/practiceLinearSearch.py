def linearSearch(searchValue, searchList):
    # linear search
    # create an array

    found = False 
    index = 0

    # conditional loop that stops when
    # 1. - search value is found
    # 2. - the search is at the end of the array

    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True
        else:
            index += 1

    # after the loop (unindent)

    if found:
        print("found at", index)
    else:
        print("not found")

linearSearch("emilia", ["debbie", "liyana", "emilia"])