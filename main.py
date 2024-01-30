# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
import random

artistic_turtle = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(num_sides):
    for b in range(num_sides):
        angle = 360 / num_sides
        artistic_turtle.forward(20)
        artistic_turtle.right(angle)


for shapes in range(3, 80):
    artistic_turtle.color(random_color())
    draw_shape(shapes)

wn.exitonclick()
