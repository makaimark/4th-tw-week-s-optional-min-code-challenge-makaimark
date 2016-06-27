import random


def g(b):
    for i in range(10):
        a, c = 0, random.randint(1, b)
        while c != a:
            a = int(input("Enter an integer from 1 to " + str(b) + ":"))
            print("guess is low" if a < c else "guess is high" if a > c else "you got it!")
g(99)
g(49)
