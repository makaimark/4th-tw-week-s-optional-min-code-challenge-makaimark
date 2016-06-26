import random


def game_logic(b):
    for i in range(10):
        a, c = 0, random.randint(1, b)
        while c != a:
            a = int(input("Enter an int from 1 to " + str(b) + ":"))
            print("guess is low" if a < c else "guess is high" if a > c else "you guessed it!")
game_logic(99)
game_logic(49)
