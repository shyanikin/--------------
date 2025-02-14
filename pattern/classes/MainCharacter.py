from const import *
import pygame
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Настройки динозавров
DINO_WIDTH, DINO_HEIGHT = 50, 50
MOVE_HEIGHT = 30
GRAVITY = 3

# Настройки препятствий
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 30, 30
OBSTACLE_SPEED = 5

class MainCharacter:
    def __init__(self, color, move_controls, image):
        self.rect = pygame.Rect(50, HEIGHT - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)
        self.color = color
        self.jump = False
        self.move_velocity = 0
        self.move_controls = move_controls
        self.right = False
        self.left = False
        self.image = pygame.image.load(image).convert_alpha()
        self.ob = True

    def move(self, keys):
        if keys[self.move_controls['right']] and not (self.jump or self.right or self.left) and self.ob:
            self.right = True
            self.move_velocity = MOVE_HEIGHT
        
        if keys[self.move_controls['left']] and not (self.jump or self.right or self.left) and self.ob:
            self.left = True
            self.move_velocity = MOVE_HEIGHT
        
        if keys[self.move_controls['jump']] and not (self.jump or self.right or self.left) and self.ob:
            self.jump = True
            self.move_velocity = MOVE_HEIGHT

        if self.left:
            self.rect.x -= 10
            self.move_velocity -= GRAVITY
            self.left = False
        
        if self.right:
            self.rect.x += 10
            self.move_velocity -= GRAVITY
            self.right = False   
        
        if self.jump:
            self.rect.y -= self.move_velocity
            self.move_velocity -= GRAVITY
            if self.rect.y >= HEIGHT - DINO_HEIGHT:
                self.rect.y = HEIGHT - DINO_HEIGHT
                self.jump = False
