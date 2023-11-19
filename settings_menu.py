from base_classes import Menu, Button
import pygame
from typing import Any
from level_selection import BackToMenu


class FullScreenButton(Button):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [200, 50],
                 text: str = "Fullscreen",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            The fullscreen button.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size,
                         text_color)  # initializes the button class(gets the attributes it has)

        self.fullscreen = False

    def action(self):
        if self.fullscreen:
            self.fullscreen = False
            pygame.display.set_mode((1000, 800), flags=pygame.SCALED)
        else:
            self.fullscreen = True
            pygame.display.set_mode((1000, 800), flags=pygame.FULLSCREEN | pygame.SCALED)


class Settings(Menu):
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
            FullScreenButton,
            BackToMenu
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