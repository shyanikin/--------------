"""import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Многопользовательская игра")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройки игроков
player_size = 30
player_1_pos = [100, 300]
player_2_pos = [200, 300]
player_3_pos = [300, 300]

# Создание игрового цикла
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Управление игрока 1 (стрелки)
    if keys[pygame.K_LEFT]:
        player_1_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_1_pos[0] += 5
    if keys[pygame.K_UP]:
        player_1_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_1_pos[1] += 5

    # Управление игрока 2 (WASD)
    if keys[pygame.K_a]:
        player_2_pos[0] -= 5
    if keys[pygame.K_d]:
        player_2_pos[0] += 5
    if keys[pygame.K_w]:
        player_2_pos[1] -= 5
    if keys[pygame.K_s]:
        player_2_pos[1] += 5

    # Управление игрока 3 (IJKL)
    if keys[pygame.K_j]:
        player_3_pos[0] -= 5
    if keys[pygame.K_l]:
        player_3_pos[0] += 5
    if keys[pygame.K_i]:
        player_3_pos[1] -= 5
    if keys[pygame.K_k]:
        player_3_pos[1] += 5

    # Заполнение фона и отрисовка игроков
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_1_pos[0], player_1_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GREEN, (player_2_pos[0], player_2_pos[1], player_size, player_size))
    pygame.draw.rect(screen, BLUE, (player_3_pos[0], player_3_pos[1], player_size, player_size))

    pygame.display.flip()
    pygame.time.delay(30)

# Завершение работы Pygame
pygame.quit()"""

"""import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLAYER_SIZE = 50
ITEM_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра для троих")

# Игроки
players = {
    "player1": {"color": RED, "pos": [100, 100], "controls": [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]},
    "player2": {"color": GREEN, "pos": [200, 200], "controls": [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]},
    "player3": {"color": BLUE, "pos": [300, 300], "controls": [pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k]},
}

# Предмет
item_pos = [random.randint(0, WIDTH - ITEM_SIZE), random.randint(0, HEIGHT - ITEM_SIZE)]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Движение игроков
    for player in players.values():
        if keys[player["controls"][0]]:  # Влево
            player["pos"][0] -= 5
        if keys[player["controls"][1]]:  # Вправо
            player["pos"][0] += 5
        if keys[player["controls"][2]]:  # Вверх
            player["pos"][1] -= 5
        if keys[player["controls"][3]]:  # Вниз
            player["pos"][1] += 5

    # Проверка на сбор предмета
    for player in players.values():
        if (player["pos"][0] < item_pos[0] < player["pos"][0] + PLAYER_SIZE and
            player["pos"][1] < item_pos[1] < player["pos"][1] + PLAYER_SIZE):
            item_pos = [random.randint(0, WIDTH - ITEM_SIZE), random.randint(0, HEIGHT - ITEM_SIZE)]

    # Отрисовка
    screen.fill(WHITE)
    for player in players.values():
        pygame.draw.rect(screen, player["color"], (*player["pos"], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, (0, 0, 0), (*item_pos, ITEM_SIZE, ITEM_SIZE))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
"""

import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLAYER_SIZE = 50
ITEM_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра для троих")

# Игроки
players = {
    "player1": {"color": RED, "pos": [100, 100], "controls": [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], "score": 0},
    "player2": {"color": GREEN, "pos": [200, 200], "controls": [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN], "score": 0},
    "player3": {"color": BLUE, "pos": [300, 300], "controls": [pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k], "score": 0},
}

# Предмет
item_pos = [random.randint(0, WIDTH - ITEM_SIZE), random.randint(0, HEIGHT - ITEM_SIZE)]

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Движение игроков
    for player in players.values():
        if keys[player["controls"][0]]:  # Влево
            player["pos"][0] -= 5
        if keys[player["controls"][1]]:  # Вправо
            player["pos"][0] += 5
        if keys[player["controls"][2]]:  # Вверх
            player["pos"][1] -= 5
        if keys[player["controls"][3]]:  # Вниз
            player["pos"][1] += 5

    # Проверка на сбор предмета
    for player in players.values():
        if (player["pos"][0] < item_pos[0] < player["pos"][0] + PLAYER_SIZE and
            player["pos"][1] < item_pos[1] < player["pos"][1] + PLAYER_SIZE):
            item_pos = [random.randint(0, WIDTH - ITEM_SIZE), random.randint(0, HEIGHT - ITEM_SIZE)]
            player["score"] += 1  # Увеличиваем счет игрока

    # Отрисовка
    screen.fill(WHITE)
    for player in players.values():
        pygame.draw.rect(screen, player["color"], (*player["pos"], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, (0, 0, 0), (*item_pos, ITEM_SIZE, ITEM_SIZE))

    # Отображение счета
    font = pygame.font.Font(None, 36)
    for i, (player_name, player) in enumerate(players.items()):
        score_text = font.render(f"{player_name}: {player['score']}", True, player["color"])
        screen.blit(score_text, (10, 10 + i * 30))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()