import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TITLE = 'Snake Game'

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

CELL_SIZE = 10
direction = 1
update_snake = 0
score = 0

snake_pos = [[int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)]]
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2) + CELL_SIZE])
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2) + CELL_SIZE * 2])
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2) + CELL_SIZE * 3])

BG = (255,200,150)
RED = (255,0,0)
BLACK = (0,0,0)
BODY_INNER = (50,175,25)
BODY_OUTER = (100,100,200)
APPLE_COLOR = 	(139,2,2)

apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE-1) * CELL_SIZE]

font = pygame.font.SysFont(None, 35)

pygame.mixer.music.load('Chest Pains (I Love).mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def draw_screen():
    screen.fill(BG)

def draw_apple():
    pygame.draw.rect(screen,APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score():
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, [10,10])

running = True
while running:
    draw_screen()
    draw_apple()
    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            elif event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    if update_snake > 99:
        update_snake = 0

        head_x, head_y = snake_pos[0]

        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y += CELL_SIZE
        elif direction == 4:
            head_x -= CELL_SIZE

        snake_pos.insert(0, [head_x,head_y])
        snake_pos.pop

        if snake_pos[0] == apple_pos:
            apple_pos = [random.randint(0,SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            snake_pos.append(snake_pos[-1])
            score += 1

        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            running = False

    for i in range(len(snake_pos)):
        segment = snake_pos[i]
        if i == 0:
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else:
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        
    pygame.display.flip()

    update_snake += 1

pygame.quit()
sys.exit()