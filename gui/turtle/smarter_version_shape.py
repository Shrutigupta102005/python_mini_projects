from turtle import *

tim = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 110):
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
