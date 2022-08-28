
from turtle import Turtle, Screen

from snake import Snake


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A simple snake game')


# set up the starting snake

snake = Snake('white')

snake.move('left')
snake.move('left')
snake.move('left')


screen.exitonclick()
