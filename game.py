"""
    Does the game logic (handling states and stuff).
"""
import pygame
from main_menu import MainMenu
from level_selection import LevelSelectionMenu
from playing import Playing


class Game:
    def __init__(self, window: pygame.Surface):
        """
            Handles the states of the game.
            :param window: the pygame display.
        """
        self.window = window

        self.already_pressed = []

        self.state = "menu"
        self.states = {
            "menu": MainMenu(window, self),
            "levels": LevelSelectionMenu(window, self),
            "playing": Playing(window, self)
        }

        self.current_state = self.states[self.state]

    def draw(self) -> None:
        """
            Draws the current state of the game on the given surface.
            :return: None
        """
        self.current_state.draw()

    def handle_input(self) -> None:
        """
            Responds to keyboard input.
            :return: None
        """
        if not isinstance(self.current_state, Playing):
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if pygame.K_ESCAPE not in self.already_pressed: # prevents the pause menu spamming when holding escape
                self.already_pressed.append(pygame.K_ESCAPE)
                self.current_state.pause()
        else:
            if pygame.K_ESCAPE in self.already_pressed:
                self.already_pressed.remove(pygame.K_ESCAPE)

        if not self.current_state.state == "paused":
            if keys[pygame.K_LCTRL]:
                self.current_state.entities[0].stop_moving()

            if keys[pygame.K_a]:
                self.current_state.entities[0].move(0, 1) # moves 0 tiles vertically and 1 tile horizontally

            if keys[pygame.K_d]:
                self.current_state.entities[0].move(0, -1) # moves 0 tiles vertically and -1 tile horizontally

            if keys[pygame.K_w]:
                self.current_state.entities[0].move(-1, 0) # moves -1 tiles vertically and 0 tile horizontally

            if keys[pygame.K_s]:
                self.current_state.entities[0].move(1, 0) # moves 1 tiles vertically and 0 tile horizontally


    def run_level(self, level):
        try:
            self.states["playing"].frames[1].load_level(level)
        except KeyError:
            print("\033[93mnu merge inca bc this level wasnt added\033[0m < probabil linia 53, game.py")
            return
        self.state = "playing"
        self.current_state = self.states[self.state]
        self.current_state.level = level
        self.current_state.load_entities()

        text_label = self.current_state.frames[0].children[0]
        text_label.text = f"level: {level}"
        text_label.generate_text()



    def check_clicks(self):
        self.current_state.check_for_clicks()