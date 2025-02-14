import pygame
import random

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Автоматически генерирующийся фон")

# Цвета
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)

# Параметры игрока
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 50
player_speed = 5

def draw_background(y_offset):
    """Функция для отрисовки фона в виде лужайки."""
    for y in range(-y_offset, HEIGHT, 50):
        # Рисуем лужайку с случайным темным зеленым цветом
        color = DARK_GREEN if random.random() > 0.5 else GREEN
        pygame.draw.rect(screen, color, (0, y % HEIGHT, WIDTH, 50))

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Обработка границ экрана
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

    # Обновление фона
    screen.fill((255, 255, 255))  # Заполнение белым цветом для очистки
    draw_background(player_pos[1] // 5)  # Генерируем фон, основываясь на позиции игрока

    # Рисуем игрока
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
