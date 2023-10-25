import random

class Task2():
    n = random.randint(1, 100)
    player = 0
    def play(cls):
        while True:
            cls.player = int(input("Enter your numper: "))
            if (cls.player == cls.n):
                break
            elif cls.player > cls.n:
                print("too high")
            elif cls.player < cls.n:
                print("too low")
        print("You win!")

