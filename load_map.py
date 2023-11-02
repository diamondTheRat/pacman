"""
    Loads the map of the given level.
"""
import pygame
from csv import reader

sprite_sheets = {
    "walls": pygame.image.load("Levels/sprite sheets/wall.png"),
    "pacman spawn": pygame.image.load("Levels/sprite sheets/pacman spawn.png"),
    "dots": pygame.image.load("Levels/sprite sheets/dots.png"),
}


def load_map_layout(path, level):
    """
    Loads the layout of all the layers of a level's map.
    :param path: The folder containing all the levels.
    :param level: The level whose map you want to load.
    :return: A dictionary containing the layout of every block on the map.
    """
    level_folder = "".join(["Level ", str(level)])
    blocks = ["dots", "pacman spawn", "walls"]
    all_layouts = {}
    for block in blocks:
        csv_file_path = f"{str(path)}/{level_folder}/{level_folder}_{str(block)}.csv"
        block_layout = import_csv_layout(csv_file_path)
        if block_layout is not None:
            all_layouts[block] = block_layout
    return all_layouts


def import_csv_layout(file):
    """
    Creates a list that has the contents of the given csv file.
    """
    terrain_map = []
    try:
        with open(file) as t_map:
            level_map = reader(t_map, delimiter=",")
            for row in level_map:
                terrain_map.append(list(row))
            return terrain_map
    except FileNotFoundError:
        return None


def import_cut_graphics(img, t_size):
    surface = img
    tile_num_x = int(surface.get_size()[0] / int(t_size[0]))
    tile_num_y = int(surface.get_size()[1] / int(t_size[1]))

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * t_size[0]
            y = row * t_size[1]
            new_surf = pygame.Surface((t_size[0], t_size[1]), pygame.SRCALPHA)   # .convert_alpha()
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, t_size[0], t_size[1]))
            cut_tiles.append(new_surf)

    return cut_tiles


class Tile:
    def __init__(self, size, x, y, offset, screen):
        super().__init__()
        self.screen = screen
        self.x = x - offset[0]
        self.y = y - offset[1]
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=(x, y))
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))    # here it blits all tiles
        pass


class StaticTile(Tile):
    def __init__(self, size, x, y, surface, offset, screen):
        super().__init__(size, x, y, offset, screen)
        self.image = surface


def find_tiles_to_blit(rooms, current_room, screen):
    """
    Finds every tile's position and image.
    :param rooms: All rooms' layout.
    :param current_room: The room where Pacman currently is.
    :param screen: Surface on which the tiles will be drawn.
    :return: A list with the tiles that have to be blitted on the screen.
    """
    room = rooms[f"room{current_room}"]
    layers = list(room.keys())
    tiles_to_blit_list = []
    for layer in layers:
        for row_index, row in enumerate(room[layer]):
            for val_index, val in enumerate(row):
                if val != "-1":
                    x = val_index * 40
                    y = row_index * 40
                    if layer == "walls":
                        wall_tile_list = import_cut_graphics(sprite_sheets["walls"], [40, 40])
                        tile_surface = wall_tile_list[int(val)]
                        tile = StaticTile([40, 40], x, y, tile_surface, [0, 0], screen)
                    elif layer == "pacman spawn":
                        pacman_spawn_tile_list = import_cut_graphics(sprite_sheets["pacman spawn"], [40, 40])
                        tile_surface = pacman_spawn_tile_list[int(val)]
                        tile = StaticTile([40, 40], x, y, tile_surface, [0, 0], screen)
                    elif layer == "dots":
                        dots_tile_list = import_cut_graphics(sprite_sheets["dots"], [40, 40])
                        tile_surface = dots_tile_list[int(val)]
                        tile = StaticTile([40, 40], x, y, tile_surface, [0, 0], screen)
                    else:
                        tile = StaticTile([40, 40], 0, 0, pygame.Surface((0, 0)), [0, 0], screen)
                    tiles_to_blit_list.append(tile)
    return tiles_to_blit_list


def draw_tiles(tiles):
    """ Actually drawing the tiles on screen. """
    for tile in tiles:
        tile.draw()


def split_layout_into_rooms(layout):
    """
    Cuts all the layers and puts them in smaller pieces called rooms.
    :param layout: The map's layout containing all its layers.
    :return: A dictionary containing all 9 rooms (also dictionaries) containing all the layers.
    """
    rooms = {}
    layers = list(layout.keys())
    for room_nr in range(9):
        rooms[f"room{room_nr + 1}"] = {}
        for layer in layers:
            room_info = []
            for row in range(20*(room_nr % 3), 20*((room_nr % 3)+1)):
                room_info_row = []
                for val in range(20):
                    room_info_row.append(layout[layer][row][val])
                room_info.append(room_info_row)
            rooms[f"room{room_nr + 1}"][layer] = room_info
    return rooms


# Testing:
level1_layout = load_map_layout("Levels", 1)
all_rooms = split_layout_into_rooms(level1_layout)
tiles_to_blit = find_tiles_to_blit(all_rooms, 1, pygame.Surface((500, 500)))  # WIN
draw_tiles(tiles_to_blit)
