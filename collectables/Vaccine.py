import os
import pygame
from images.CollectablesAssets import CollectablesAssets
from constants.CollectablesConstants import CollectableConstants


class Vaccine:

    def __init__(self):
        self.__images = CollectablesAssets()
        self.__vaccine_amount = 0
        self.__x = CollectableConstants.X_VACCINE
        self.__y = CollectableConstants.Y_VACCINE

    def draw(self, window):
        window.blit(self.__images.vaccine, (self.__x, self.__y, 100, 100))
        pinscher_font = os.path.join('font', 'SHPinscher-Regular.otf')
        font = pygame.font.Font(pinscher_font, 45, bold=True)
        text_a = str(self.__vaccine_amount).zfill(2) + ' x '
        text = font.render(text_a, True, (0, 0, 0))
        window.blit(text,  (self.__x-80, self.__y+5, 100, 100))

    def spend_vaccine(self):
        self.__vaccine_amount -= 1

    def zero_vaccine_left(self):
        return self.__vaccine_amount == 0

    def got_vaccine(self):
        if self.__vaccine_amount <= 99:
            self.__vaccine_amount += 1
