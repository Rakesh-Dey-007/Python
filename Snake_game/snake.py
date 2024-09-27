import pygame as pg 
import sys
import random

pg.init()

WIDTH = 600
HEIGHT = 600

snake_speed = 25
snake_blocksize = 20
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
x = 0
y = 0
score = 0
direction = "none"
snake_body = [[WIDTH / 2, HEIGHT / 2]]
snake_length = 1
game_over = False
game_paused = True 


font = pg.font.Font("assets/arial.ttf", 20)
score_board = font.render(f"SCORE {score}", True, (255, 255, 255))
score_board_rect = score_board.get_rect(center=(50, 20))
restart_btn = font.render("Press R to restart & ESC to quit", True, (0, 0, 0))
restart_btn_rect = restart_btn.get_rect(center=(300, 560))

win = pg.display.set_mode((HEIGHT, WIDTH))
pg.display.set_caption("SNAKE GAME")
background_green = (0, 204, 92)
snake_blue = (0, 59, 209)
fruit_red = (245, 0, 4)

clock = pg.time.Clock()

fruit_x = random.randrange(1, 15) * 20
fruit_y = random.randrange(1, 15) * 20


crash_misic=pg.mixer.Sound("assets/crash.mp3")
collect_music=pg.mixer.Sound("assets/collect.mp3")
background_music=pg.mixer.Sound("assets/backgroundmusic.mp3")

pg.mixer.music.set_volume(0.5) 
collect_music.set_volume(1.0) 


def restartt():
    global snake_x, snake_y, x, y, score, snake_body, snake_length, fruit_x, fruit_y, game_over, direction, game_paused
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    x = 0
    y = 0
    score = 0
    direction = "none"
    snake_body = [[WIDTH / 2, HEIGHT / 2]]
    snake_length = 1
    fruit_x = random.randrange(1, 15) * 20
    fruit_y = random.randrange(1, 15) * 20
    game_over = False
    game_paused = True  
    update_score() 

def update_score():
    global score_board
    score_board = font.render(f"SCORE {score}", True, (255, 255, 255))

def main_snake(win, snake_body):
    for item in snake_body:
        pg.draw.rect(win, snake_blue, [item[0], item[1], snake_blocksize, snake_blocksize])
 
background_music.play(-1)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            if not game_over:
                if game_paused:
                    if event.key in (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_a, pg.K_s, pg.K_d):
                        game_paused = False

                if not game_paused: 
                    if (event.key == pg.K_UP or event.key == pg.K_w) and direction != "down":
                        x = 0
                        y = -snake_blocksize
                        direction = "up"
                    elif (event.key == pg.K_DOWN or event.key == pg.K_s) and direction != "up":
                        x = 0
                        y = snake_blocksize
                        direction = "down"
                    elif (event.key == pg.K_LEFT or event.key == pg.K_a) and direction != "right":
                        x = -snake_blocksize
                        y = 0
                        direction = "left"
                    elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and direction != "left":
                        x = snake_blocksize
                        y = 0
                        direction = "right"
            else:
                if event.key == pg.K_r:
                    restartt()

    if not game_over: 
        snake_x, snake_y = snake_body[0]
        snake_x += x
        snake_y += y

        if snake_x < 0:
            snake_x = WIDTH
        elif snake_x >= WIDTH:
            snake_x = 0
        if snake_y < 0:
            snake_y = HEIGHT
        elif snake_y >= HEIGHT:
            snake_y = 0

        snake_body.insert(0, [snake_x, snake_y])

        if snake_x == fruit_x and snake_y == fruit_y:
            fruit_x = random.randrange(1, 15) * 20
            fruit_y = random.randrange(1, 15) * 20
            snake_length += 1
            score += 1
            collect_music.play()
            update_score()
        else:
            snake_body.pop()

        if [snake_x, snake_y] in snake_body[1:]:
            game_over = True
            crash_misic.play()

    win.fill(background_green)

    main_snake(win, snake_body)

    pg.draw.rect(win, fruit_red, [fruit_x, fruit_y, snake_blocksize, snake_blocksize], 5, 5, 5, 5)
    win.blit(score_board, score_board_rect)
    if game_over:
        win.blit(restart_btn, restart_btn_rect)

    pg.display.update()
    clock.tick(snake_speed)
