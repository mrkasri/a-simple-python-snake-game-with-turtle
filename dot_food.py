

from turtle import Turtle
import random


class DotFood(Turtle):

    def __init__(self, color: str = 'blue') -> None:
        super().__init__()
        self.shape('circle')
        self.color(color)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(10)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
