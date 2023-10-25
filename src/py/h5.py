class Task5():
    c = [0, 0]
    cc = list()
    player = []
    def __init__(self, n):
        self.n = n

    def get_coord(self):
        for i in range(0, self.n):
            print("new coordinates")
            for d in range(0, 2):
                self.c[d] = int(input("coord: "))

            self.cc.append(self.c)
        print("Enter player's coord: ")
        for d in range(0, 2):
            self.player.append(int(input("coord: ")))

    def check(self):
        for i in range(0, self.n):
            dis = pow((pow((self.cc[i][0] - self.player[0]), 2) + pow((self.cc[i][1] - self.player[1]), 2)), 0.5)
            if dis < 15:
                print("Game over")
                break
        else:
            print("Game is continuing")