import math


# your code here
def cheater(number):
    print("Don't cheat!")


math.factorial = cheater

# don't delete this line, please
math.factorial(23)
