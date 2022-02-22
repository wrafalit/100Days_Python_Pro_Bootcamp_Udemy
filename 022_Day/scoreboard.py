from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.ht()
        self.pu()
        self.color("white")
        self.goto(0, 280)
        self.r_point = 0
        self.l_point = 0
        self.board_print()

    def board_print(self):
        self.clear()
        text = f"{self.l_point} : {self.r_point}"
        self.write(text,False, align= "center")

    def add_l_point(self):
        self.l_point += 1
        self.board_print()

    def add_r_point(self):
        self.r_point += 1
        self.board_print()

