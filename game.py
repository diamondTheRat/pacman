"""
    Does the game logic (handling states and stuff).
"""
import pygame
from main_menu import MainMenu
from level_selection import LevelSelectionMenu


class Game:
    def __init__(self, window: pygame.Surface):
        """
            Handles the states of the game.
            :param window: the pygame display.
        """
        self.window = window

        self.state = "menu"
        self.states = {
            "menu": MainMenu(window, self),
            "levels": LevelSelectionMenu(window, self)
        }

        self.current_state = self.states[self.state]

    def draw(self):
        self.current_state.draw()

    def run_level(self, level):
        print("\033[93mnu merge inca bc no levels\033[0m < probabil linia 27, game.py")


    def check_clicks(self):
        self.current_state.check_for_clicks()