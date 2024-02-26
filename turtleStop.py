import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon to center it
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle
turtle.speed(ANIMATION_SPEED)  
turtle.penup()

# Move the turtle to the starting point
start_x = -diameter / 4             # getting these coordinates was just trial and error... took a lot of time :(
start_y = diameter / 1.75  
turtle.goto(start_x, start_y)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()

# Draw the octagon
for _ in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

turtle.end_fill()

# Display "STOP"
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", align="center", font=("Arial", 40, "bold"))

# Hide the turtle and show the result
turtle.hideturtle()
turtle.done()



