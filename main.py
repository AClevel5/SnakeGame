import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
x = 0
y = 0

def grow_snake(x_cord, y_cord):
    t = turtle.Turtle()
    t.color("white")
    t.shape("square")
    t.goto(x_cord, y_cord)

for a in range(3):
    grow_snake(x, y)
    x -= 20











screen.exitonclick()