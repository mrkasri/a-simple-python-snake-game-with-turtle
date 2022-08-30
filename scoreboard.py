
from turtle import Turtle


class ScoreBoard(Turtle):

    FONT = ('Courier', 24, 'normal')
    ALIGN = 'center'

    def __init__(self, color: str = 'white') -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(color)
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ScoreBoard.ALIGN,
                   font=ScoreBoard.FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ScoreBoard.ALIGN,
                   font=ScoreBoard.FONT)
