from turtle import *
from random import randrange
from freegames import square, vector

# Initial position for the food and snake
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)  # The direction in which the snake will move

def change(x, y):
    """Change the direction of the snake."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head is inside the boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move the snake forward by one segment."""
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake hits the boundary or itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Draw red square on the hit position
        update()
        return

    snake.append(head)  # Append the new head position to the snake

    # Check if the snake has reached the food
    if head == food:
        print('snake length:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Remove the tail if no food is eaten

    clear()

    # Draw the snake
    for body in snake:
        square(body.x, body.y, 9, 'green')

    # Draw the food
    square(food.x, food.y, 9, 'red')
    update()

    # Move the snake every 100 milliseconds
    ontimer(move, 100)

# Setup the game screen
screen = Screen()
screen.bgcolor('black')  # Set the background color to black
hideturtle()
tracer(False)
listen()

# Define controls for snake movement
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Start the game
move()
done()
