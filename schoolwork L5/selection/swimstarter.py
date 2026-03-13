swimtime = float(input("input a swim time: "))
if swimtime < 55.0:
    print("you qualified for gold category")
elif swimtime > 55.0 and swimtime < 60.0:
    print("you have qualified for silver category")
elif swimtime > 60.0 and swimtime < 65.0:
    print("you have qualified for bronze category")
else:
    print("you have not qualified")