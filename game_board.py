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
        self.map = pygame.Surface(size, flags=pygame.SRCALPHA)

        self.dots_left = self.dot_count = 0

        self.room_index = 0

    def load_level(self, level):
        self.parent.score = 0
        self.parent.reset_score()

        level_layout = load_map_layout("Levels", level)
        self.rooms = split_layout_into_rooms(level_layout)
        self.count_dots()

        self.room = self.rooms[f"room{self.find_starting_room()}"]

        self.tiles = find_tiles_to_blit(self.rooms, self.start_room, self.map)
        self.map.fill((0, 0, 0, 0))
        draw_tiles(self.tiles)

        self.room_index = self.start_room

        self.grid = get_empty_rooms(self.rooms, self.start_room)
        self.parent.minimap.arrange(self.grid) # updates the minimap


    def count_dots(self) -> None:
        """
        Counts the number of dots in a level
        :return:
        """

        self.dots_left = self.dot_count = sum(i == "0" for room in self.rooms.values() for row in room["dots"] for i in row)



    def change_room(self, x_change, y_change):
        index = self.room_index - 1
        x, y = index % 3, index // 3
        x += x_change
        y += y_change
        room = x + y * 3 + 1
        self.room_index = room

        self.load_room(room)

    def load_room(self, room):
        self.room = self.rooms[f"room{room}"]

        self.tiles = find_tiles_to_blit(self.rooms, room, self.map)
        self.map.fill((0, 0, 0, 0))
        draw_tiles(self.tiles)

        self.grid = get_empty_rooms(self.rooms, room)
        self.parent.minimap.arrange(self.grid)  # updates the minimap


    def find_starting_room(self):
        for room, tiles in self.rooms.items():
            for y, row in enumerate(tiles["pacman spawn"]):
                for x, tile in enumerate(row):
                    if tile == '0':
                        self.start_room = int(room[-1])
                        self.start_tile = [x, y]
        return self.start_room

    def draw(self):
        self.Surface.fill((0, 0, 0, 0))
        self.Surface.blit(self.map, (0, 0))
        for entity in self.parent.entities:
            entity.draw(self.Surface)
        self.parent.window.blit(self.Surface, self.pos)