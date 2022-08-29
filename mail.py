
from turtle import Screen
import time
from dot_food import DotFood
from snake import Snake


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A simple snake game')
screen.tracer(1)


# set up the starting snake
game_on = True
snake = Snake('white')
dot = DotFood('blue')


# Moving the snake
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    snake.forward()
    time.sleep(0.1)

    # detect collision
    if snake.head.distance(dot) < 15:
        dot.refresh()


screen.exitonclick()
