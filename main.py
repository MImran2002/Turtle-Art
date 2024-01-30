# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle

artistic_turtle = turtle.Turtle()
wn = turtle.Screen()
artistic_turtle.shape("circle")
for a in range(50):
    artistic_turtle.penup()
    artistic_turtle.forward(10)
    artistic_turtle.pendown()
    artistic_turtle.forward(10)
wn.exitonclick()