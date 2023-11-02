from base_classes import Frame, Menu


UNAVAILABLE_ROOM_COLOR = (0, 0, 0) # rooms that u cant access
ROOM_COLOR = (100, 100, 100) # rooms that u can access
CURRENT_ROOM_COLOR = (255, 255, 255) # room that ur currently in

room_colors = [UNAVAILABLE_ROOM_COLOR, ROOM_COLOR, CURRENT_ROOM_COLOR]


class MiniMap(Frame):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[int, int] | list[int, int],
                 size: tuple[int, int] | list[int, int],
                 color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0)
                 ):
        super().__init__(parent, xy, size, color)

    def arrange(self, grid: list[list[int, int, int]]) -> None:
        self.grid = [[] for _ in range(3)]

        cell_size = (self.width - 5 * 4) / 3
        size = [cell_size, cell_size]

        for y in range(3):
            row = self.grid[y]
            for x in range(3):
                pos = [5 + (5 + cell_size) * x, 5 + (5 + cell_size) * y]
                room = Frame(self, pos, size, room_colors[grid[y][x]])
                row.append(room)
                self.add_child(room)



    def set_map(self, map: list[list[int]]):
        self.map = map
        self.update()

    def update(self):
        self.arrange(self.map)

