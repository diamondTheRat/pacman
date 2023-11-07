from base_classes import TextLabel
import pygame
from typing import Any, Literal
from base_classes import Frame, Menu


class LivesLabel(TextLabel):

    def __init__(self,
                 parent: Any,
                 xy: tuple[float, float] | list[float, float],
                 size: tuple[float, float] | list[float, float],
                 text: str = "",
                 text_size: int = 16,
                 text_color: tuple[int, int, int] | list[int, int, int] = (255, 255, 255),
                 color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0),
                 side: Literal["left", "center", "right"] = "center"
                 ):
        """
            The lives label.
            :param parent: the menu that holds the label.
            :param xy: the position of the label.
            :param size: the size of the label.
            :param text: (optional) the text displayed on the label.
            :param text_size: (optional) the size of the text.
            :param text_color: (optional) the color of the text.
        """

        self.image = pygame.image.load("./animations/pacman animation/pacman_1.png")
        self.image = pygame.transform.scale(self.image, (40, 40))

        super().__init__(parent, xy, size, text, text_size, text_color, color, side)

    def add_image(self) -> None:
        """
            Draws the image onto the text label
            :return: None
        """
        y = (self.height - self.image.get_height()) // 2
        x = 0 # self.width - self.image.get_width()
        self.surface.blit(self.image, (x, y))

    def generate_text(self) -> None:
        """
            Puts the text on the label.
            Runs when the class is created.
            :return: None
        """
        self.surface.fill(self.color)

        self.add_image()

        font = pygame.font.Font("Pixel Font.ttf", self.font_size)
        text = font.render(self.text, 1, self.text_color)
        # x_text = font.render("x", 1, self.text_color)

        # self.surface.blit(x_text, x_text.get_rect(center=(self.width // 2, self.height // 2)))

        # self.surface.blit(text, text.get_rect(center=(self.width - text.get_width() // 2, self.height // 2)))
        self.surface.blit(text, text.get_rect(center=(self.image.get_width() + text.get_width() // 2, self.height // 2)))

    def draw(self) -> None:
        """
            Renders the text label on the parent surface.
            :return: None
        """

        if isinstance(self.parent, Frame):
            self.parent.Surface.blit(self.surface, self.rect)
        elif isinstance(self.parent, Menu):
            self.parent.window.blit(self.surface, self.rect)
        else:
            raise ValueError("Bro who's my parent ._.")
