# required modules
from turtle import * 
import pyfiglet
from random import randint


highlight = pyfiglet.figlet_format('Turtle Race')
print(highlight)


# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)  # Decrease the screen size
screen.bgcolor('black')  # Set dark theme background color

# classic shape turtle
speed(0)
penup()
goto(-140, 140)
color('white')  # Change text color for visibility in dark theme

# racing track
for step in range(15):
    write(step, align ='center', font=('Arial', 12, 'normal'))
    right(90)
    
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
        
    penup()
    backward(160)
    left(90)
    forward(20)

# First player details
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# First player proceeds to racing track
player_1.penup()
player_1.goto(-160, 110)
player_1.pendown()

# 360 degree turn
for turn in range(10):
    player_1.right(36)

# Second player details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# Second player enters the racing track
player_2.penup()
player_2.goto(-160, 80)
player_2.pendown()

# 360 degree turn
for turn in range(72):
    player_2.left(5)

# Third player details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# Third player enters the racing track
player_3.penup()
player_3.goto(-160, 50)
player_3.pendown()

# 360 degree turn
for turn in range(60):
    player_3.right(6)

# Fourth player details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# Fourth player enters the racing track
player_4.penup()
player_4.goto(-160, 20)
player_4.pendown()

# 360 degree turn
for turn in range(30):
    player_4.left(12)

# Fifth player details (new turtle)
player_5 = Turtle()
player_5.shape('turtle')
player_5.color('purple')

# Fifth player enters the racing track
player_5.penup()
player_5.goto(-160, -10)
player_5.pendown()

# 360 degree turn
for turn in range(20):
    player_5.right(18)

# List to hold all turtles for easy manipulation
turtles = [player_1, player_2, player_3, player_4, player_5]

# Turtles run at random speeds
race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(randint(1, 5))
        # Check if any turtle reaches the finish line (x = 160)
        if turtle.xcor() >= 160:
            race_on = False
            winner = turtle
            break

# Display the winner
penup()
goto(-70, -160)
color('white')
style = ('Arial', 16, 'bold')
write(f"The winner is {winner.color()[0].capitalize()}!", font=style, align='center')

# Finish
done()
