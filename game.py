"""
    Does the game logic (handling states and stuff).
"""
import pygame
from main_menu import MainMenu
from level_selection import LevelSelectionMenu
from playing import Playing


class Game:
    def __init__(self, window: pygame.Surface):
        """
            Handles the states of the game.
            :param window: the pygame display.
        """
        self.window = window

        self.already_pressed = []

        self.state = "menu"
        self.states = {
            "menu": MainMenu(window, self),
            "levels": LevelSelectionMenu(window, self),
            "playing": Playing(window, self)
        }

        self.current_state = self.states[self.state]

    def draw(self) -> None:
        """
            Draws the current state of the game on the given surface.
            :return: None
        """
        self.current_state.draw()

    def handle_input(self) -> None:
        """
            Responds to keyboard input.
            :return: None
        """
        if not isinstance(self.current_state, Playing):
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if pygame.K_ESCAPE not in self.already_pressed: # prevents the pause menu spamming when holding escape
                self.already_pressed.append(pygame.K_ESCAPE)
                self.current_state.pause()
        else:
            if pygame.K_ESCAPE in self.already_pressed:
                self.already_pressed.remove(pygame.K_ESCAPE)

    def run_level(self, level):
        print("\033[93mnu merge inca bc no levels\033[0m < probabil linia 27, game.py")


    def check_clicks(self):
        self.current_state.check_for_clicks()