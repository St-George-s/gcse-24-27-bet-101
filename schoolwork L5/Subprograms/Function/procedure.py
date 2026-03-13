#to make a subprogram (This is how to make a procedure)
def getAreaRectangle(length, breadth):
    area = length * breadth
    return(area)

# to call a subprogram
print(getAreaRectangle(2, 5))

returnedArea = getAreaRectangle(2,5)
print(returnedArea)