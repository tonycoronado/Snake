

import turtle
import time

delay = 0.3

# Set Up Screen
wn = turtle.Screen()
wn.title("Snake Game by TonyDev")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)    #Turns off the screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0)               #speed of Animation NOT speed
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Keyboard bindings
wn.listen()

wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Main Game Loop
while True:
    wn.update()     #Always update the screen

    move()

    time.sleep(delay)


wn.mainloop()


