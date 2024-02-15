from turtle import Turtle, Screen
from random import randint

tim = Turtle()

def random_colour():
    # Generate random RGB values
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    # Return a tuple of RGB values
    return (r, g, b)

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        # Convert tuple of RGB values to string using the 'join' method
        color = "#" + "".join([f"{x:02x}" for x in random_colour()])
        tim.color(color)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()


