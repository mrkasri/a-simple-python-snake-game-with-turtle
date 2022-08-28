
from turtle import Turtle, Screen


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A simple snake game')


# set up the starting snake
start_position = [(0, 0), (-20, 0), (-40, 0)]
for position in start_position:
    new_square = Turtle(shape='square')
    new_square.color('white')
    new_square.goto(position)


screen.exitonclick()
