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



    def load_anim(self):
        path = fr".\animations\pacman animation"
        frames = 4
        for frame in range(1, frames + 1):
            image = pygame.image.load(fr"{path}\pacman_{frame}.png")
            self.frames.append(image)

        self.frame = self.frames[0]