from turtle import Turtle


class Snake:
    def __init__(self, color: str) -> None:
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.squares = []

        for position in self.positions:
            new_square = Turtle(shape='square')
            new_square.penup()
            new_square.color(color)
            new_square.goto(position)
            self.squares.append(new_square)

    def move(self, dirction: str):

        for i in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[i-1].xcor()
            new_y = self.squares[i-1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.squares[0].forward(20)
