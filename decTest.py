for i in range(1,11):
    import random
    child = random.randint(1,101)
    if child > 50:
        kid = "good"
        print(child, "points? wow a gift for you as you are", kid)
    elif child <= 50:
        kid = "naughty"
        print(child, "points? wow no gift for you as you are", kid)

