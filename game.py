import random


def g(b):
    for i in range(10):
        a, c = 0, random.randint(1, b)
        while c != a:
            a = int(input("1 to " + str(b) + ":"))
            print("low" if a < c else "high" if a > c else "ok")
g(99)
g(49)
