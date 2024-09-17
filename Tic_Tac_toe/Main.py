import pygame as pg
from sys import exit

# Initialize Pygame
pg.init()

# Set up the display
screen = pg.display.set_mode((600, 600))

# Load images and fonts
board_img = pg.image.load('board.png').convert_alpha()
font = pg.font.SysFont('arial', 30, bold=True)  # Correct font setup with bold style
label_info = font.render('Player 1 chance', True, (255, 255, 255))

# Correct rect positioning using 'center'
label_info_rect = label_info.get_rect(center=(300, 30))

cross_img = pg.image.load("cross.png").convert_alpha()
circle_img = pg.image.load("circle.png").convert_alpha()

button_img = pg.image.load("button.png").convert_alpha()
button_img_rect = button_img.get_rect(center=(300, 550))

block_size = 120
is_player1_chance = True
chance_count = 0
pos = (0, 0)
result = None
pieces = []
matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Set up the clock for frame rate control
clock = pg.time.Clock()

def checkClickedPosition(pos):
    if(pos[0] > 120 and pos[0] < 240) and (pos[1]>120 and pos[1] < 240):
        return(1,1)
    elif(pos[0] > 240 and pos[0] < 360) and (pos[1] > 120 and pos[1] < 240):
        return(1,2)
    elif(pos[0] > 360 and pos[0] < 480) and (pos[1] > 120 and pos[1] < 240):
        return(1,3)
    elif(pos[0] > 120 and pos[0] < 240) and (pos[1] > 240 and pos[1] < 360):
        return(2,1)
    elif(pos[0] > 240 and pos[0] < 360) and (pos[1] > 240 and pos[1] < 360):
        return(2,2)
    elif(pos[0] > 360 and pos[0] < 480) and (pos[1] > 240 and pos[1] < 360):
        return(2,3)
    elif(pos[0] > 120 and pos[0] < 240) and (pos[1] > 360 and pos[1] < 480):
        return(3,1)
    elif(pos[0] > 240 and pos[0] < 360) and (pos[1] > 360 and pos[1] < 480):
        return(3,2)
    elif(pos[0] > 360 and pos[0] < 480) and (pos[1] > 360 and pos[1] < 480):
        return(3,3)

    return None

def check_completion(matrix):
    # Initialize winner variable with a default value
    winner = "No one is Winner"  # Default message if no winner

    # Check for horizontal wins
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != '-':
            if matrix[i][0] == 'x':
                winner = "Player 1 is Winner."
            elif matrix[i][0] == 'o':
                winner = "Player 2 is Winner."
            return winner, (120, 120 * (i + 1) + 60), (480, 120 * (i + 1) + 60)

    # Check for vertical wins
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != '-':
            if matrix[0][i] == 'x':
                winner = "Player 1 is Winner."
            elif matrix[0][i] == 'o':
                winner = "Player 2 is Winner."
            return winner, (120 * (i + 1) + 60, 120), (120 * (i + 1) + 60, 480)

    # Check for diagonal wins (top-left to bottom-right)
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '-':
        if matrix[0][0] == 'x':
            winner = "Player 1 is Winner."
        elif matrix[0][0] == 'o':
            winner = "Player 2 is Winner."
        return winner, (120, 120), (480, 480)

    # Check for diagonal wins (top-right to bottom-left)
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != '-':
        if matrix[0][2] == 'x':
            winner = "Player 1 is Winner."
        elif matrix[0][2] == 'o':
            winner = "Player 2 is Winner."
        return winner, (480, 120), (120, 480)

    # If no winner, return the default message
    return winner, (0, 0),(0,0)




def restart():
    global is_player1_chance, chance_count, pos, result, pieces, matrix, label_info, someone_won
    is_player1_chance = True
    chance_count = 0
    pos = (0, 0)
    result = None
    pieces = []
    someone_won = False
    matrix = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    label_info = font.render("Player 1 chance", True, (255, 255, 255))

# Main game loop
someone_won = False  # Initialize someone_won variable
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if button_img_rect.collidepoint(pg.mouse.get_pos()) and (someone_won or chance_count == 9):
                restart()
    
    result = checkClickedPosition(pos)

    if result != None:
        if matrix[result[0]-1][result[1]-1] == "-":
            if is_player1_chance:
                pieces.append([cross_img, block_size * result[1] + 20, block_size * result[0]+20])
                is_player1_chance = False
                matrix[result[0]-1][result[1]-1] = "x"
                label_info = font.render("Player 2 Chance", True, (255,255,255))
                
            else:
                pieces.append([circle_img, block_size * result[1] + 20, block_size * result[0] + 20])
                is_player1_chance = True
                matrix[result[0]-1][result[1]-1] = "o"
                label_info = font.render("Player 1 Chance", True, (255,255,255))

            chance_count += 1

            temp = check_completion(matrix)
            if temp[1] != (0,0):
                label_info = font.render(temp[0], True, (255,255,255))
                someone_won = True
            elif chance_count == 9 and not someone_won:
                # Draw message if no one has won and all chances are used
                label_info = font.render("No one is Winner.", True, (255, 255, 255))

    pos = (0, 0)

    # Fill the screen with a color
    screen.fill((18, 18, 18))

    # Blit the board image and label onto the screen
    screen.blit(board_img, (120, 120))
    screen.blit(label_info, label_info_rect)

    # Draw all the pieces on the board
    for piece in pieces:
        screen.blit(piece[0], (piece[1], piece[2]))
    
    # Draw the winning line if someone has won
    if someone_won or chance_count == 9:
        if someone_won:
            pg.draw.line(screen, (255, 255, 255), temp[1], temp[2], 5)
        screen.blit(button_img, button_img_rect)

    # Update the display
    pg.display.update()

    # Cap the frame rate
    clock.tick(60)
