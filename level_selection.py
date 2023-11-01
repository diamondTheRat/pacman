import pygame
from typing import Any
from base_classes import Button, Menu

class LevelButton(Button):
    def __init__(self,
                 parent: Menu,
                 level: int,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [100, 100],
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            Plays the selected level.
            :param parent: the menu that it's in.
        """
        self.level = level
        self.text = str(level)
        super().__init__(parent, xy, size, self.text, text_size, text_color)

    def action(self) -> None:
        """
            This just runs the level.
            :return: None
        """
        self.parent.game.run_level(self.level)


class BackToMenu(Button):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[float, float] | list[float, float] = None,
                 size: tuple[float, float] | list[float, float] = [200, 50],
                 text: str = "Menu",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255)
                 ):
        """
            Returns to the main menu.
            :param parent: the menu that it's in.
        """

        super().__init__(parent, xy, size, text, text_size, text_color)

    def action(self):
        self.parent.change_state("menu")


class LevelSelectionMenu(Menu):
    def __init__(self,
                 window: pygame.Surface,
                 game: Any,
                 button_size: tuple[int, int] | list[int, int] = [100, 100],
                 ):
        self.button_size = button_size

        super().__init__(window, game)

        self.arrange()

    def arrange(self) -> None:
        """
            Arranges the buttons.
            :return: None
        """
        levels = 10 # this isn't final, it's just a way to test stuff yk
        levels_per_row = 5 # self-explanatory

        width, height = self.button_size

        window_width, window_height = self.window.get_size()

        spacing = (window_width - width * levels_per_row) / (levels_per_row + 1) # the spacing on the x-axis

        for i in range(levels):
            x, y = i % levels_per_row, i // levels_per_row
            x *= width + spacing
            x += spacing
            y *= height + spacing
            y += spacing
            xy = [x, y]
            self.buttons.append(LevelButton(self, i + 1, xy=xy, size=self.button_size))

        back_to_menu = BackToMenu(self, xy=[0, 0])
        back_to_menu.rect.center = [window_width // 2, window_height - back_to_menu.height * 2]
        self.buttons.append(back_to_menu)


    def draw(self) -> None:
        for button in self.buttons:
            button.draw()