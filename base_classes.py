"""
    In here you'll find classes used for making other, more complex classes.\n
    By that I mean you use these as a foundation, then add onto them to make new classes.
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
            A text button.
            :param parent: the menu that holds the button.
            :param xy: the position of the button.
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
        self.rect = self.surface.get_rect(topleft=xy)


        self.generate_text()

    def action(self) -> None:
        """
            This runs when u interact with the button(click).
            :return: None
        """
        print("Hi you clicked me but i dont do anything :(")

    def click(self, pos: tuple[int, int] | list[int, int]):
        """
            Checks if the button was clicked.
            :param pos: the position of the mouse
            :return: bool
        """
        if self.rect.collidepoint(pos):
            self.action()
            return True
        return False

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

        self.parent.window.blit(self.surface, self.rect)



class Menu:
    def __init__(self,
                 window: pygame.Surface,
                 game: Any
                 ):
        """
            The foundation for a menu.
            :param window: the pygame window/display.
        """
        self.window = window

        self.game = game

        self.buttons = []

    def check_for_clicks(self) -> None:
        """
            Checks if any interaction has occurred.
            :return: None
        """
        for button in self.buttons:
            pos = pygame.mouse.get_pos()
            button.click(pos)

    def change_state(self, state):
        try:
            self.game.current_state = self.game.states[state]
            self.game.state = state
        except KeyError:
            print(f"\033[93m'{state}' menu is not currently implemented\033[0m")

