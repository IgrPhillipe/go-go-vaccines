import pygame
import random
from images.ObstacleAssets import ObstacleAssets
from constants.BackgroundConstants import BackgroundConstants

# 900 no x
# 580 no y
class Box:

    def __init__(self, axis_x, axis_y):
        self.__images = ObstacleAssets()
        self.__mult = 1
        self.__axis_x = axis_x
        self.__axis_y =  axis_y

    def draw(self, window):
        window.blit(self.__images.box_obstacle,
                    (self.__axis_x, self.__axis_y, 100, 100))           
        #pygame.display.update()

    def move(self):
        self.__axis_x -= BackgroundConstants.VELOCITY * self.__mult

        if self.__axis_x < BackgroundConstants.WIDTH * BackgroundConstants.AXIS_ADJUSTMENT:
            self.__axis_x = 900 + random.randint(200, 900)

    @property
    def axis_x(self):
        return self.__axis_x
    
    @property
    def axis_y(self):
        return self.__axis_y