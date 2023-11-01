"""
    Does the game logic(handling states and stuff)
"""
import pygame
from menu import MainMenu


class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window

        self.state = "menu"
        self.states = {
            "menu": MainMenu(window)
        }

        self.current_state = self.states[self.state]

    def draw(self):
        self.current_state.draw()