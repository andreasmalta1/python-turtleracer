import turtle
import random
import time



window = turtle.Screen()


def draw_court():
    window.bgcolor("green")
    window.tracer(False)  # Turned off animation

    # Draw the court
    court = turtle.Turtle()
    court.hideturtle()
    court.penup()
    court.goto(-300, 300)
    court.pendown()

    for i in range(5):
        court.forward(600)
        court.right(90)


def draw_racer():
    #  Give each turtle a random speed
    racer1_speed = random.randint(1, 11)
    racer2_speed = random.randint(1, 11)

    racer1 = turtle.Turtle()
    racer1.shape("turtle")
    racer1.color("blue")
    racer1.speed(racer1_speed)
    racer1.penup()
    racer1.goto(-250, 250)
    racer1.pendown()

    racer2 = turtle.Turtle()
    racer2.shape("arrow")
    racer2.color("red")
    racer2.speed(racer2_speed)
    racer2.penup()
    racer2.goto(-250, 200)
    racer2.pendown()

    window.tracer(True)
    racer1.forward(500)
    racer2.forward(500)

    # show the result
    result = turtle.Turtle()
    result.hideturtle()
    result.color("deep pink")
    style = ("Arial", 30, "bold")
    result.write(("Racer 1" if racer1_speed > racer2_speed else "Racer 2") + " wins!", font=style, align="center")
    time.sleep(3)


draw_court()
draw_racer()
