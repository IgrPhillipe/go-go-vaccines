from crocodile.Crocodile import Crocodile
from constants.CrocodileConstants import CrocodileConstants
from humans.ManWithBag import ManWithBag
from humans.OldLady import OldLady
from humans.RedHeadWoman import RedHeadWoman
from humans.Woman import Woman
from constants.HandleCrocodileToHumanConstants import HandleCrocodileToHumanConstants
import random

class HandleCrocodileToHuman:

    def __init__(self):
        self.__crocodile = Crocodile(680)
        self.__humans = [
            ManWithBag(),
            OldLady(),
            RedHeadWoman(),
            Woman()
        ]
        self.__current_human_choice = 3
        self.__is_human = False


    def draw(self, window):
        if not self.__is_human:
            self.__crocodile.draw(window)
        else:
            self.__humans[self.__current_human_choice].draw(window, self.__crocodile.axis_x)
        self.__change_to_crocodile()
        self.__crocodile.move()

        
    def __change_to_crocodile(self):
        if self.__is_human and self.__crocodile.axis_x < -HandleCrocodileToHumanConstants.AXIS_X_TO_CHANGE_ABSTRACTION:
            self.__current_human_choice += HandleCrocodileToHumanConstants.CHANGE_PLAYER
            self.__current_human_choice %= len(self.__humans)
            self.__is_human = False

    def hit_crocodile_with_vaccine(self):
        self.__is_human = True

    @property
    def crocodile(self):
        return self.__crocodile

    