import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
DINO_WIDTH, DINO_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Динозаврики на троих")

# Класс динозаврика
class Dino:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, DINO_WIDTH, DINO_HEIGHT)
        self.color = color

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - DINO_WIDTH:
            self.rect.x = WIDTH - DINO_WIDTH

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Класс препятствия
class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def move(self):
        self.rect.x -= 5

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Основная функция игры
def main():
    clock = pygame.time.Clock()
    dino1 = Dino(100, HEIGHT - DINO_HEIGHT, GREEN)
    dino2 = Dino(300, HEIGHT - DINO_HEIGHT, (0, 0, 255))
    dino3 = Dino(500, HEIGHT - DINO_HEIGHT, (255, 255, 0))
    obstacles = []
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Игрок 1
            dino1.move(-5)
        if keys[pygame.K_d]:
            dino1.move(5)
        if keys[pygame.K_LEFT]:  # Игрок 2
            dino2.move(-5)
        if keys[pygame.K_RIGHT]:
            dino2.move(5)
        if keys[pygame.K_j]:  # Игрок 3
            dino3.move(-5)
        if keys[pygame.K_l]:
            dino3.move(5)

        # Генерация препятствий
        if random.randint(1, 30) == 1:
            obstacles.append(Obstacle())

        # Движение и удаление препятствий
        for obstacle in obstacles:
            obstacle.move()
            if obstacle.rect.x < 0:
                obstacles.remove(obstacle)
                score += 1

        # Проверка на столкновение
        for obstacle in obstacles:
            if dino1.rect.colliderect(obstacle.rect) or dino2.rect.colliderect(obstacle.rect) or dino3.rect.colliderect(obstacle.rect):
                running = False

        # Отрисовка
        screen.fill(WHITE)
        dino1.draw()
        dino2.draw()
        dino3.draw()
        for obstacle in obstacles:
            obstacle.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
