class Task4():
    w = str()
    S = str()
    def get(cls):
        cls.w = input("Input word: ")
        cls.S = input("Input sentence: ")
    def check(cls):
        if cls.S.find(cls.w) > -1:
            print("index of word", cls.S.find(cls.w))
            return True
        else:
            print("no match")
            return False


