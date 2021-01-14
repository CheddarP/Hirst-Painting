import colorgram
import turtle as t
import random

colors = colorgram.extract("rainbow.jpg", 10)

timmy = t.Turtle()
timmy.shape("circle")
t.colormode(255)
timmy.pensize(20)
timmy.speed("fastest")

dots_per_row = 10

def draw_dots():
    for _ in range(dots_per_row):
        num = random.randint(0, 9)
        timmy.color((colors[num].rgb))
        timmy.pendown()
        timmy.forward(1)
        timmy.penup()
        timmy.forward(50)
        timmy.penup()

for space in range(1, dots_per_row + 1):
    timmy.penup()
    timmy.setposition(-225, -300 + space*50)
    draw_dots()

timmy.hideturtle()

screen = t.Screen()
screen.exitonclick()