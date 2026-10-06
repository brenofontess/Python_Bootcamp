from turtle import Turtle, Screen, _Screen

tim = Turtle()
screen: _Screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_circle():
    tim.circle(180)

def move_right():
    tim.right(45) # angle = 45 degrees

def move_left():
    tim.left(45) # angle = 45 degrees

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="q", fun=move_circle)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

