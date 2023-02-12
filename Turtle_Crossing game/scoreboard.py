FONT = ("Courier", 24, "normal")

from turtle import Turtle

num = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.write(f"Level {num}", align="center", font=(FONT))

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level {num + 1}", align="center", font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
