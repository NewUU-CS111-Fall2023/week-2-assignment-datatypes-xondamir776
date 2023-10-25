# * Author: Zokirjonov Xondamir
# * Date: 25.10.2023
import random
import math


print("task2:")

n = random.randint(1, 100)
while True:
    player = int(input("Enter your numper: "))
    if(player==n):
        break
    elif player > n :
        print("too high")
    elif player < n :
        print("too low")
print("You win!")

print("\ntask3:")
h = random.randint(100, 2147483647)
n = float(input("Input numer: "))
print(h/n)

print("\ntask4:")
def check(w, S):
    if S.find(w) > -1:
        print("index of word", S.find(w))
        return True
    else:
        print("no match")
        return False
word = input("Input word: ")
sentence = input("Input sentence: ")

print(check(word, sentence))

print("\ntask5:")

n = 3
c = [0, 0]
cc = list()
for i in range(0, n):
    print("new coordinates")
    for d in range(0, 2):
        c[d]=int(input("coord: "))

    cc.append(c)

player = []
print("Enter player's coord: ")
for d in range(0, 2):
    player.append(int(input("coord: ")))

for i in range(0, n):
    dis = pow((pow((cc[i][0] - player[0]), 2) + pow((cc[i][1] - player[1]), 2)), 0.5)
    if dis < 15:
        print("Game over")
        break
else:
    print("Game is continuing")

