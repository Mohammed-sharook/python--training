li = [1, "ayd", 4.4, 52, 6, "7", 8.6]
for i in li:
    if type(i) == int:
        print("This is integer -->", i)

    elif type(i) == str:
        print("This are strings -->", i)

    else:
        print("This is float -->", i)