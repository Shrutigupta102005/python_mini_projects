from turtle import Turtle, Screen
tt_turtle_obj = Turtle()

for _ in range(15):
    tt_turtle_obj.forward(10)
    tt_turtle_obj.color("white")
    tt_turtle_obj.forward(10)
    tt_turtle_obj.color("black")

screen = Screen()
screen.exitonclick()
