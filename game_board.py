import pygame

from base_classes import Frame, Menu
from load_map import *


class Board(Frame):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[int, int] | list[int, int] = [0, 0],
                 size: tuple[int, int] | list[int, int] = [800, 800],
                 ):
        super().__init__(parent, xy, size, (0, 0, 0, 0))

        self.Surface = pygame.Surface(size, flags=pygame.SRCALPHA)

        self.load_level(2)

    def load_level(self, level):
        level_layout = load_map_layout("Levels", level)
        self.rooms = split_layout_into_rooms(level_layout)

        self.room = self.find_starting_room()   

        self.tiles = find_tiles_to_blit(self.rooms, 2, self.Surface)
        draw_tiles(self.tiles)

    def find_starting_room(self):
        for room, tiles in self.rooms.items():
            for row in tiles["pacman spawn"]:
                for tile in row:
                    if tile == '0':
                        print(f"starting in {room}")

    def draw(self):
        self.parent.window.blit(self.Surface, self.pos)