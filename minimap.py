from base_classes import Frame, Menu


UNAVAILABLE_ROOM_COLOR = (0, 0, 0) # rooms that u cant access
ROOM_COLOR = (100, 100, 100) # rooms that u can access
CURRENT_ROOM_COLOR = (255, 255, 255) # room that ur currently in


class MiniMap(Frame):
    def __init__(self,
                 parent: Menu,
                 xy: tuple[int, int] | list[int, int],
                 size: tuple[int, int] | list[int, int],
                 color: tuple[int, int, int] | list[int, int, int] = (0, 0, 0)
                 ):
        super().__init__(parent, xy, size, color)
        self.arrange()
        print(self.parent)

    def arrange(self):
        pass

    def set_map(self, map: list[list[int]]):
        pass

    def update(self):
        pass

