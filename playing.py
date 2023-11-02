"""
    The menu class is defined in here.
"""
import pygame
from base_classes import Button, Menu, Frame
from typing import Any
from level_selection import BackToMenu
from minimap import MiniMap


class GoToMenu(BackToMenu):
    def click(self, pos: tuple[int, int] | list[int, int]):
        if self.rect.collidepoint(pos):
            self.action()
            self.parent.parent.state = "playing"
            return True
        return False


class PauseMenu(Menu):
    def __init__(self,
                 parent: Menu,
                 window: pygame.Surface,
                 game: Any,
                 button_size: tuple[int, int] | list[int, int] = [200, 50],
                 ):
        self.parent = parent

        self.button_size = button_size

        super().__init__(window, game)

        self.arrange()

    def arrange(self) -> None:
        """
            Centers the buttons.
            :return: None
        """
        self.background = pygame.Surface(self.window.get_size(), flags=pygame.SRCALPHA)
        self.background.fill((255, 255, 255, 30))

        buttons = [
            GoToMenu
        ]

        width, height = self.button_size

        window_width, window_height = self.window.get_size()

        button_count = len(buttons)
        for i, button in enumerate(buttons):
            x, y = window_width // 2 - width // 2, window_height // 2 - ((5 + height) * button_count - 5) / 2 + (
                        5 + height) * i
            xy = [x, y]
            self.buttons.append(button(self, xy=xy))


    def draw(self) -> None:
        self.window.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw()


class Playing(Menu):
    def __init__(self,
                 window: pygame.Surface,
                 game: Any,
                 button_size: tuple[int, int] | list[int, int] = [200, 50],
                 ):

        super().__init__(window, game)
        self.pause_menu = PauseMenu(self, window, game)
        self.state = "playing"
        self.arrange()

    def arrange(self):
        side_bar = Frame(self, [self.window.get_width() - 200, 0], [200, self.window.get_height()], (70, 75, 85))
        self.frames.append(side_bar)
        minimap = MiniMap(side_bar, [20, self.window.get_height() - 180], [160, 160], (60, 70, 80))
        side_bar.add_child(minimap)


    def pause(self):
        if self.state == "paused":
            self.state = "playing"
        else:
            self.state = "paused"

    def check_for_clicks(self) -> None:
        super().check_for_clicks()

        self.pause_menu.check_for_clicks()


    def draw(self) -> None:
        for frame in self.frames:
            frame.draw()

        for button in self.buttons:
            button.draw()


        if self.state == "paused":
            self.pause_menu.draw()
