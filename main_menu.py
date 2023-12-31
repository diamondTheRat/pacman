"""
    The menu class is defined in here.
"""
import pygame
from base_classes import Button, Menu
from typing import Any
from title import Title


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
            The levels button.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size, text_color) # initializes the button class(gets the attributes it has)

    def action(self):
        self.parent.change_state("levels")

class SettingsButton(Button):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [200, 50],
                 text: str = "Settings",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            The settings button.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size, text_color) # initializes the button class(gets the attributes it has)

    def action(self):
        self.parent.change_state("settings")


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
        self.parent.game.run_level(self.parent.game.states["playing"].level)

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
            LevelsButton,
            SettingsButton
        ]

        width, height = self.button_size

        self.title = Title(self)


        window_width, window_height = self.window.get_size()

        offset = self.title.y + self.title.height
        offset /= 2 # makes the buttons go higher
        window_height -= offset

        button_count = len(buttons)
        for i, button in enumerate(buttons):
            x, y = window_width // 2 - width // 2, window_height // 2 - ((5 + height) * button_count - 5) / 2 + (5 + height) * i
            xy = [x, y + offset]
            self.buttons.append(button(self, xy=xy))


    def draw(self) -> None:
        self.title.draw()
        for button in self.buttons:
            button.draw()