import pygame
from classes.Background import Background
import pickle

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

class Levels:
    def __init__(self, backgrounD, levelNum):
        self.background = Background(backgrounD, [0,0])
        self.levelnum = levelNum
        
    def SaveLevel(self, keys):
        if keys[pygame.k_q]:
            with open("classes\file\save", "wb") as f:
                pickle.dump(self, self.levelnum)
        
        