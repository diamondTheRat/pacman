"""
    The menu class is defined in here.
"""
import pygame
from base_classes import Button, Menu, Frame, TextLabel
from typing import Any
from level_selection import BackToMenu
from minimap import MiniMap
from side_bar_text_labels import LivesLabel
from game_board import Board


class GoToMenu(BackToMenu):
    def click(self, pos: tuple[int, int] | list[int, int]):
        if not self.parent.parent.state == "paused": return # makes it so u can click it only when the game is paused

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

        self.level = 1
        self.lives = 3
        self.score = 0

        self.entities = []

        self.arrange()


    def load_entities(self):
        self.frames[1].load_entities()


    def arrange(self) -> None:
        # the frame that holds the stuff on the side
        side_bar = Frame(self, [self.window.get_width() - 200, 0], [200, self.window.get_height()], (70, 75, 85))
        self.frames.append(side_bar)

        # the game board/map
        board = Board(self)
        self.frames.append(board)

        # level counter
        pos = [10, 10]
        size = [180, 50]
        level_label = TextLabel(side_bar, pos, size, text=f"level: {self.level}", text_size=32, color=[0, 0, 0, 0])

        side_bar.add_child(level_label)

        # score
        pos = [10, 60]
        size = [180, 50]
        score_label = TextLabel(side_bar, pos, size, text=f"score: {self.score}", text_size=32, color=[0, 0, 0, 0])

        side_bar.add_child(score_label)

        # lives
        pos = [10, 120]
        size = [180, 50]
        lives_label = LivesLabel(side_bar, pos, size, text=f"   x   {self.lives}", text_size=32, color=[0, 0, 0, 0])

        side_bar.add_child(lives_label)

        # minimap
        grid = [
            [0, 1, 1],
            [0, 2, 0],
            [0, 1, 1]
        ]

        minimap = MiniMap(side_bar, [20, self.window.get_height() - 180], [160, 160], (60, 70, 80))
        side_bar.add_child(minimap)

        minimap.set_map(grid)


    def pause(self):
        if self.state == "paused":
            self.state = "playing"
        else:
            self.state = "paused"

    def check_for_clicks(self) -> None:
        super().check_for_clicks()

        self.pause_menu.check_for_clicks()

    def update(self):
        if self.state == "paused": return

        for entity in self.entities:
            entity.update()

    def draw(self) -> None:
        self.update()

        for child in self.frames + self.buttons + self.labels:
            child.draw()

        if self.state == "paused":
            self.pause_menu.draw()
