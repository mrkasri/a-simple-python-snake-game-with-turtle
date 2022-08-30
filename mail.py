
from turtle import Screen
import time
from dot_food import DotFood
from scoreboard import ScoreBoard
from snake import Snake


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('A simple snake game')
screen.tracer(0)


# set up the starting snake
game_on = True
snake = Snake('white')
dot = DotFood('blue')
score = ScoreBoard()
score.FONT_SIZE = 10


# Moving the snake
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    snake.forward()
    time.sleep(0.2)

    # detect collision
    if snake.head.distance(dot) < 15:

        dot.refresh()
        snake._extend()
        score.increase_score()

    # detect collision with the wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        score.game_over()

    # detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
