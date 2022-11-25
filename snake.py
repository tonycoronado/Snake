

import turtle
import time
import random
import winsound

delay = 0.2
 # Score
score = 0
high_score = 0

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

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Snake Food
food = turtle.Turtle()
food.speed(0)               
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Functions
def go_up():
    if head.direction != "down":    # Avoids snake going backwards
        head.direction = "up"

def go_down():
    if head.direction != "up":      # Avoids snake going backwards
        head.direction = "down"

def go_left():
    if head.direction != "right":   # Avoids snake going backwards
        head.direction = "left"

def go_right():
    if head.direction != "left":    # Avoids snake going backwards
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

# Play Initial Sound
winsound.PlaySound("StartGame.wav", winsound.SND_ASYNC)

# Main Game Loop
while True:
    wn.update()     # Always update the screen

    

    # Check for Border Collisions
    if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Play Losing Sound
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset Score
        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Reset Delay
        delay = 0.2

        # Play Initial Sound
        winsound.PlaySound("StartGame.wav", winsound.SND_ASYNC)

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move food to random stop
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        food.goto(x, y)


        # Add segment to the body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.01

        # Increase Score
        score += 10

        # PLay Eat Sound
        winsound.PlaySound("EatFood2.wav", winsound.SND_ASYNC)

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Play Losing Sound
            winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset Score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Reset Delay
            delay = 0.2

            # Play Initial Sound
            winsound.PlaySound("StartGame.wav", winsound.SND_ASYNC)
            

    time.sleep(delay)


wn.mainloop()


