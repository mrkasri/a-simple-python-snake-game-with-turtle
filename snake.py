from turtle import Turtle


class Snake:
    # Constants
    START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVING_DISTANCE = 20
    DIRECTION_UP = 90
    DIRECTION_DOWN = 270
    DIRECTION_LEFT = 180
    DIRECTION_RIGHT = 0

    def __init__(self, color: str = 'white') -> None:
        self.color = color
        self.squares = []
        self.start_snake(self.color)
        self.head = self.squares[0]

    def start_snake(self, color: str):

        for position in Snake.START_POSITIONS:
            self.add_square(color, position)

    def add_square(self, color: str, position: tuple):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color(color)
        new_square.goto(position)
        self.squares.append(new_square)

    def _extend(self):
        self.add_square(self.color, self.squares[-1].position())

    def forward(self):
        for i in range(len(self.squares)-1, 0, -1):
            new_x = self.squares[i-1].xcor()
            new_y = self.squares[i-1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(Snake.MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != Snake.DIRECTION_DOWN:
            self.head.setheading(Snake.DIRECTION_UP)

    def down(self):
        if self.head.heading() != Snake.DIRECTION_UP:
            self.head.setheading(Snake.DIRECTION_DOWN)

    def left(self):
        if self.head.heading() != Snake.DIRECTION_RIGHT:
            self.head.setheading(Snake.DIRECTION_LEFT)

    def right(self):
        if self.head.heading() != Snake.DIRECTION_LEFT:
            self.head.setheading(Snake.DIRECTION_RIGHT)
