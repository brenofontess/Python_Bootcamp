# Pong Arcade Game
#
# Goal
#
# 1) Create the screen
# 2) Create and move a paddle
# 3) Create another paddle
# 4) Create the ball and make it move
# 5) Detect collision with wall and bounce
# 6) Detect collision with paddle
# 7) Detect when paddle misses
# 8) Keep score

from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

screen.listen()
screen.onkey(go_up,"Up")




screen.exitonclick()
