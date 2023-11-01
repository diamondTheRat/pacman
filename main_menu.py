"""
    The menu class is defined in here.
"""
import pygame
from base_classes import Button, Menu
from typing import Any


class LevelsButton(Button):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [200, 50],
                 text: str = "Levels",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            The play button.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size, text_color) # initializes the button class(gets the attributes it has)

    def action(self):
        self.parent.change_state("levels")


class PlayButton(Button):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [200, 50],
                 text: str = "Play",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            Opens the levels menu.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size, text_color) # initializes the button class(gets the attributes it has)

    def action(self):
        self.parent.change_state("playing")


class MainMenu(Menu):
    def __init__(self,
                 window: pygame.Surface,
                 game: Any,
                 button_size: tuple[int, int] | list[int, int] = [200, 50],
                 ):
        self.button_size = button_size

        super().__init__(window, game)

        self.arrange()

    def arrange(self) -> None:
        """
            Centers the buttons.
            :return: None
        """
        buttons = [
            PlayButton,
            LevelsButton
        ]

        width, height = self.button_size

        window_width, window_height = self.window.get_size()

        button_count = len(buttons)
        for i, button in enumerate(buttons):
            x, y = window_width // 2 - width // 2, window_height // 2 - ((5 + height) * button_count - 5) / 2 + (5 + height) * i
            xy = [x, y]
            self.buttons.append(button(self, xy=xy))

    def draw(self) -> None:
        for button in self.buttons:
            button.draw()