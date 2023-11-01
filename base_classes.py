"""
    In here you'll find classes used for making other, more complex classes.\n
    By that I mean you use these as a foundation then add onto them to make new classes.
"""
import pygame
from typing import Any


pygame.font.init()


class Button:
    def __init__(self,
                 parent: Any,
                 xy: tuple[float, float] | list[float, float],
                 size: tuple[float, float] | list[float, float],
                 text: str = "",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """

            :param parent: the GUI that holds the button.
            :param xy: the positon of the button.
            :param size: the size of the button.
            :param text: (optional) the text displayed on the button.
            :param text_size: (optional) the size of the text.
            :param text_color: (optional) the color of the text.
        """
        self.parent = parent

        self.text = text
        self.font_size = text_size
        self.text_color = text_color

        self.pos = xy
        self.size = size

        self.x, self.y = xy
        self.width, self.height = size

        self.surface = pygame.Surface(size)

        self.generate_text()


    def generate_text(self) -> None:
        """
            Puts the text on the button.
            Runs when the class is created.
            :return: None
        """
        font = pygame.font.SysFont("arial", self.font_size)
        text = font.render(self.text, 0, self.text_color)

        self.surface.blit(text, text.get_rect(center=(self.width // 2, self.height // 2)))

    def draw(self) -> None:
        """
            Renders the button on the window.
            :return: None
        """

        self.parent.window.blit(self.surface, self.pos)



class Menu():
    def __init__(self, window: pygame.Surface):
        """
            The foundation for a menu.
            :param window: the pygame window/display.
        """
        self.window = window

        self.buttons = []

    def check_for_clicks(self) -> None:
        """
            Checks if any interaction has occurred.
            :return: None
        """
        pass
