from entities import Entity
from base_classes import Menu, Frame
import pygame


class Pacman(Entity):
    def __init__(self,
                 parent: Menu | Frame,
                 tile_size: int,
                 xy: tuple[int, int] | list[int, int],
                 speed: int,
                 frames: int = 5
                 ):
        """
            Pacman.
            :param parent: the menu or frame that pacman will be drawn in
            :param tile_size: the size of a tile in the grid
            :param xy: spawn position on the grid
            :param speed: tiles / second
            :param frames: the frames it takes to change the image
        """
        super().__init__(parent, tile_size, xy, speed, frames)


    def out_of_bounds(self):
        change = False
        if self.rect.top < 0:
            self.rect.top = self.height * 20 - 40
            change = (0, -1)
        elif self.rect.top >= self.height * 20:
            self.rect.top = 0
            change = (0, 1)
        elif self.rect.left < 0:
            self.rect.left = self.height * 20 - 40
            change = (-1, 0)
        elif self.rect.left >= self.width * 20:
            self.rect.left = 0
            change = (1, 0)

        if change:
            self.target = self.rect.topleft
            x, y = change
            self.parent.change_room(x, y)

    def load_anim(self):
        path = fr".\animations\pacman animation"
        frames = 4
        for frame in range(1, frames + 1):
            image = pygame.image.load(fr"{path}\pacman_{frame}.png")
            self.frames.append(image)

        self.base_frames = self.frames

        self.frame = self.frames[0]
