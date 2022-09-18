# Self Study 4
# Create a Python program that draws an interesting shape.

import turtle
import time

# Set the screen and background color using the Screen class

window = turtle.Screen()
window.bgcolor("white")

# Function to draw the canvas


def draw_canvas():
    window.tracer(False)
    pen_draw = turtle.Turtle()
    pen_draw.hideturtle()
    pen_draw.penup()
    pen_draw.color("black")
    pen_draw.goto(-300, 300)
    pen_draw.pendown()

    for i in range(5):
        pen_draw.forward(600)
        pen_draw.right(90)


# Function to write the description

def write_text():
    pen_write = turtle.Turtle()
    pen_write.color("medium blue")
    style = ("Arial", 30, "normal")
    pen_write.hideturtle()

    pen_write.penup()
    pen_write.goto(0, 250)
    pen_write.write("Self Study 4", move=False, align="center", font=style)

    pen_write.penup()
    pen_write.goto(0, 200)
    pen_write.write("Olympic Logo", move=False, align="center", font=style)

# Function to draw the chosen shape = Olympic Logo


def draw_shape():

    window.tracer(True)
    pen_olympic = turtle.Turtle()
    pen_olympic.pensize(6)
    pen_olympic.hideturtle()

    # Set the colors of the first row and second row for the Olmpic Logo

    first_row = ["blue", "black", "red"]
    second_row = ["", "yellow", "", "green"]

    # Set the initial positions for the both rows

    x_pos_first = -75
    x_pos_second = -37.5

    # Two loops to draw both rows. Circles are drawn using the circle function

    for i in range(3):
        pen_olympic.penup()
        pen_olympic.pencolor(first_row[i])
        pen_olympic.goto(x_pos_first, 0)
        x_pos_first += 75
        pen_olympic.pendown()
        pen_olympic.circle(50)

    for i in range(1, 4, 2):
        pen_olympic.penup()
        pen_olympic.pencolor(second_row[i])
        pen_olympic.goto(x_pos_second, -50)
        x_pos_second += 75
        pen_olympic.pendown()
        pen_olympic.circle(50)


draw_canvas()
write_text()
draw_shape()
time.sleep(3)
