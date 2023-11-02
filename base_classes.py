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

        self.frames = []

    def check_for_clicks(self) -> None:
        """
            Checks if any interaction has occurred.
            :return: None
        """
        pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.click(pos)

        for frame in self.frames:
            frame.check_for_click(pos)

    def change_state(self, state):
        try:
            self.game.current_state = self.game.states[state]
            self.game.state = state
        except KeyError:
            print(f"\033[93m'{state}' menu is not currently implemented\033[0m")


class Frame:
    def __init__(self,
                 parent: Menu,
                 xy: tuple[int, int] | list[int, int],
                 size: tuple[int, int] | list[int, int],
                 color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0)
                 ):
        """
            This is basically just a container for other elements.
            It can contain other frames, buttons and wtv we'll add in the future.
            It will
            :param parent: the menu/frame that it's in
            :param xy: the position relative to its parent
            :param size: the size of the frame
        """
        self.parent = parent

        self.color = color

        self.pos = xy
        self.x, self.y = xy

        self.size = size
        self.width, self.height = size

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.Surface = pygame.Surface(size, flags=pygame.SRCALPHA)

        self.children = [] # this is just the stuff that stays in the frame

    def add_child(self, child: object) -> None:
        """
            Adds a child(element like frame or button) to the frame.
            :param child: the frame/button that u want to add
            :return: None
        """
        self.children.append(child)

    def check_for_click(self, pos: tuple[int, int] | list[int, int]) -> None:
        """
            Checks if any clickable child(button) in the frame was clicked.
            :param pos: the position of the click
            :return: None
        """
        for child in self.children:
            if isinstance(child, Frame):
                child.check_for_click(pos)
            elif isinstance(child, Button):
                child.click(pos)

    def draw(self) -> None:
        """
            Draws the frame and the stuff in it
            :return:
        """
        self.Surface.fill(self.color)

        for child in self.children:
            if hasattr(child, "draw"):
                child.draw()

        if isinstance(self.parent, Frame):
            self.parent.Surface.blit(self.Surface, self.rect)
        elif isinstance(self.parent, Menu):
            self.parent.window.blit(self.Surface, self.rect)
