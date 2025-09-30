#Q1
temperature = int(input("whats the tempature?  "))
sun = str(input("is it sunny (Y/N):  "))

if temperature > 15 and sun == "Y":
    print("YAYAYAYAYAYAYYAYAYAYYAYAY")
elif temperature > 15:
    print("wowee")
elif sun == "N":
    print("awweeee")
elif sun == "Y":
    print("pretty")
elif temperature <= 15:
    print("brrr")
