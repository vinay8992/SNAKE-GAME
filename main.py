# import random
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
s=Screen()
s.setup(width=500,height=500)
s.bgcolor("black")
s.tracer(0)
s.title("--------:My Snake Game:---------")
snake=Snake()
Food=Food()
scoreboard=Scoreboard()
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(Food)<15:
        Food.refresh()
        snake.extend()
        scoreboard.inc_score()
    if snake.head.xcor()>799 or snake.head.xcor()<-799 or snake.head.ycor()>400 or snake.head.ycor()<-400:
        game_is_on=False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

s.exitonclick()

