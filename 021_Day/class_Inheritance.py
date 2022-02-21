class Animal:

    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super(Fish, self).breath()
        print("Under water")

    def swim(self):
        print("moving under water")


nemo = Fish()
nemo.swim()
nemo.breath()

