
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, color: str = 'white') -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(color)
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center',
                   font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
