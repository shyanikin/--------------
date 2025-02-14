import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
BACKGROUND_HEIGHT = 1200  # высота фона
BACKGROUND_WIDTH = 800      # ширина фона

# Цвета
WHITE = (255, 255, 255)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Автомatically Генерирующийся Беграунд")

# Загрузка изображений
def load_background():
    return pygame.Surface((BACKGROUND_WIDTH, BACKGROUND_HEIGHT))  # Создаем текстуру фона

def generate_background(surface):
    # Генерируем фон случайными цветами
    for y in range(BACKGROUND_HEIGHT):
        for x in range(BACKGROUND_WIDTH):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            surface.set_at((x, y), color)

# Игрок
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

# Генерация фонового изображения
background_surface = load_background()
generate_background(background_surface)
background_offset = 0

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Обновляем фоновое смещение по мере движения игрока
    background_offset += PLAYER_SPEED / 4  # Меняем скорость генерации фона
    if background_offset >= BACKGROUND_HEIGHT:
        background_offset = 0
        generate_background(background_surface)  # Генерируем новый фон при необходимости

    # Отрисовка
    screen.fill(WHITE)
    # Отображаем часть фона в зависимости от смещения
    screen.blit(background_surface, (0, -background_offset + HEIGHT // 2))
    screen.blit(background_surface, (0, -background_offset + HEIGHT // 2 + BACKGROUND_HEIGHT))

    pygame.draw.rect(screen, (255, 0, 0), player)  # Рисуем игрока
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
