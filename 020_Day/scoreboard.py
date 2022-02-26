from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.ht()
        self.pu()
        self.color("white")
        self.goto(0,280)
        self.point = 0
        self.high_score = 0
        self.board_print()

    def board_print(self):
        self.clear()
        text = f"Score: {self .point} High Score: {self.high_score}"
        self.write(text, False, align="center")

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
        self.point = 0
        self.board_print()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", False, align="center")

    def add_point(self):
        self.point += 1
        self.board_print()

