import os
import pygame


class Images:
    IMAGE_BOTTOM_CITY = os.path.join(
        'assets', 'background', 'Background_layer_1.png')
    IMAGE_BACK_BUILDINGS = os.path.join(
        'assets', 'background', 'Background_layer_2.png')
    STARS = os.path.join('assets', 'background', 'Stars.png')
    IMAGE_TOP_CITY = os.path.join(
        'assets', 'background', 'Background_layer_3.png')
    MOON = os.path.join('assets', 'background', 'Moon.png')
    MAIN_CHARACTER = os.path.join('assets', 'characters', 'main-character.png')
    SQUAT_CHARACTER = os.path.join('assets', 'characters', 'nurse_down.png')
    CHARACTER_RIGHT_RUN = os.path.join(
        'assets', 'characters', 'nurse_right_run.png')
    BOX_OBSTACLE = os.path.join('assets', 'obstacles', 'box.png')
    BOXES_OBSTACLE = os.path.join('assets', 'obstacles', 'box_on_top.png')

    def __init__(self):
        self.__bottom_city = pygame.image.load(self.IMAGE_BOTTOM_CITY)
        self.__top_city = pygame.image.load(self.IMAGE_TOP_CITY)
        self.__starts = pygame.image.load(self.STARS)
        self.__back_buildings = pygame.image.load(self.IMAGE_BACK_BUILDINGS)
        self.__moon = pygame.image.load(self.MOON)
        self.__main_character = pygame.image.load(self.MAIN_CHARACTER)
        self.__squat_character = pygame.image.load(self.SQUAT_CHARACTER)
        self.__character_right_run = pygame.image.load(
            self.CHARACTER_RIGHT_RUN)
        self.__box_obstacle = pygame.image.load(self.BOX_OBSTACLE)
        self.__boxes_obstacle = pygame.image.load(self.BOXES_OBSTACLE)

    @property
    def bottom_city(self):
        return self.__bottom_city

    @property
    def top_city(self):
        return self.__top_city

    @property
    def stars(self):
        return self.__starts

    @property
    def back_buildings(self):
        return self.__back_buildings

    @property
    def moon(self):
        return self.__moon

    @property
    def main_character(self):
        return self.__main_character

    @property
    def squat_character(self):
        return self.__squat_character

    @property
    def character_right_run(self):
        return self.__character_right_run

    @property
    def box_obstacle(self):
        return self.__box_obstacle

    @property
    def boxes_obstacle(self):
        return self.__boxes_obstacle
