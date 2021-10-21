a = int(input())  # min sleep hours
b = int(input())  # max sleep hours
h = int(input())  # actual sleep hours

if h < a:
    print("Deficiency")
else:
    if h > b:
        print("Excess")
    else:
        print("Normal")
