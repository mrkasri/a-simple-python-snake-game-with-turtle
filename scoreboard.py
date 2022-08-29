
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, color: str = 'white') -> None:
        super().__init__()
        self.score = 0
        self.color(color)
        self.write(f"Score: {self.score}", align='center',
                   font=('Arial', 24, 'normal'))
