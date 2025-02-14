import pygame
import random
from MainCharacter import *
from const import *
from Background import Background

WIDTH, HEIGHT = 800, 400
WHITE = 'classes\image\BG.png'
GREEN = (0, 255, 0)

# Настройки динозавров
DINO_WIDTH, DINO_HEIGHT = 50, 50
MOVE_HEIGHT = 30
GRAVITY = 3

# Настройки препятствий
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 30, 30
OBSTACLE_SPEED = 5
# Инициализация Pygame
pygame.init()

object = pygame.Rect(70, HEIGHT - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Динозаврики на троих")

# Создание динозавров
dinos = {
    "player1": MainCharacter((255, 0, 0), {'jump': pygame.K_w, 'right': pygame.K_d, 'left': pygame.K_a}, 'classes\image\image.png'),
    "player2": MainCharacter((0, 255, 0), {'jump': pygame.K_UP, 'right': pygame.K_RIGHT, 'left': pygame.K_LEFT}, 'classes\image\image.png'),
    "player3": MainCharacter((0, 0, 255), {'jump': pygame.K_i, 'right': pygame.K_j, 'left': pygame.K_l}, 'classes\image\image.png')
}

screen.fill([255, 255, 255])
BackGround = Background(WHITE, [0,0])
# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Движение динозавров
    for dino in dinos.values():
        dino.move(keys)

    # Отрисовка
    screen.blit(BackGround.image, BackGround.rect)
    for dino in dinos.values():
        pygame.draw.rect(screen, (255,0,0), object)
        pygame.draw.rect(screen, dino.color, dino.rect )
        screen.blit(dino.image, (dino.rect.x, dino.rect.y))

    if keys[pygame.K_e]:
        WHITE = "classes\image\BG2.png"
        BackGround.image = pygame.image.load(WHITE)
    elif keys[pygame.K_g]:
        WHITE = "classes\image\BG.png"
        BackGround.image = pygame.image.load(WHITE)

    for dino in dinos.values():
        if (dino.rect.x or dino.rect.y) == object:
            dino.ob = False
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()