import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Настройки динозавров
DINO_WIDTH, DINO_HEIGHT = 50, 50
JUMP_HEIGHT = 30
GRAVITY = 3

# Настройки препятствий
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 30, 30
OBSTACLE_SPEED = 5

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Динозаврики на троих")

# Класс Динозавра
class Dino:
    def __init__(self, color, controls):
        self.rect = pygame.Rect(50, HEIGHT - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)
        self.color = color
        self.jump = False
        self.jump_velocity = 0
        self.controls = controls

    def move(self, keys):
        if keys[self.controls['jump']] and not self.jump:
            self.jump = True
            self.jump_velocity = JUMP_HEIGHT

        if self.jump:
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= GRAVITY
            if self.rect.y >= HEIGHT - DINO_HEIGHT:
                self.rect.y = HEIGHT - DINO_HEIGHT
                self.jump = False

# Создание динозавров
dinos = {
    "player1": Dino((255, 0, 0), {'jump': pygame.K_w}),
    "player2": Dino((0, 255, 0), {'jump': pygame.K_UP}),
    "player3": Dino((0, 0, 255), {'jump': pygame.K_i}),
}

# Список препятствий
obstacles = []
obstacle_timer = 0

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

    # Создание препятствий
    obstacle_timer += 1
    if obstacle_timer > 60:  # Генерируем новое препятствие каждую секунду
        obstacles.append(pygame.Rect(WIDTH, HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        obstacle_timer = 0

    # Движение препятствий
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED

    # Проверка на столкновение
    for dino in dinos.values():
        for obstacle in obstacles:
            if dino.rect.colliderect(obstacle):
                print(f"{dino.color} динозавр попал в препятствие!")

    # Удаление пройденных препятствий
    obstacles = [obs for obs in obstacles if obs.x > -OBSTACLE_WIDTH]

    # Отрисовка
    screen.fill(WHITE)
    for dino in dinos.values():
        pygame.draw.rect(screen, dino.color, dino.rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 0, 0), obstacle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()