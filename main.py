# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
import random

artistic_turtle = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
artistic_turtle.shape("circle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def hirst_painting():
    for a in range(0, 501, 50):
        artistic_turtle.penup()
        artistic_turtle.goto(-250, -250 + a)
        artistic_turtle.pendown()
        for b in range(10):
            artistic_turtle.color(random_color())
            artistic_turtle.stamp()
            artistic_turtle.penup()
            artistic_turtle.forward(50)
            artistic_turtle.pendown()



hirst_painting()

wn.exitonclick()
