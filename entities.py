import pygame
from base_classes import Menu, Frame


class Entity:
    def __init__(self,
                 parent: Menu | Frame,
                 tile_size: int,
                 xy: tuple[int, int] | list[int, int],
                 speed: int,
                 frames: int = 5
                 ):
        """
            An enemy / character.
            :param parent: the menu or frame that the entity will be drawn in
            :param tile_size: the size of a tile in the grid
            :param xy: spawn position on the grid
            :param speed: tiles / second
            :param frames: the frames it takes to change the image
        """
        self.parent = parent

        self.width = self.height = tile_size
        self.size = [tile_size, tile_size]

        self.rect = pygame.Rect(xy[0] * self.width, xy[1] * self.height, tile_size, tile_size)

        self.speed = speed

        self.frames = []
        self.frame_index = 0
        self.frame = None
        self.frame_rate = 1 / frames

        self.start_pos = self.target = self.rect.topleft # the position it starts at and the position it's moving to
        self.move_vector = [0, 0]

        self.steps = 0


        self.load_anim()

    def load_anim(self):
        pass

    def update_anim(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.frames) or self.frame_index <= 0:
            self.frame_index -= self.frame_rate
            self.frame_rate *= -1

        self.frame = self.frames[int(self.frame_index)]

    def stop_moving(self):
        self.move_vector = (0, 0)

    def move(self, vertically: bool, horizontally: bool):
        self.move_vector = (vertically, horizontally)
        if not self.rect.topleft == self.target: return # if it didn't finish moving it won't change direction
        x, y = self.rect.topleft

        self.start_pos = [x, y]
        self.target = (x - self.height * horizontally, y + self.height * vertically)

        self.steps = self.speed

    def update(self):
        if not self.steps: return

        x1, y1 = self.start_pos
        x2, y2 = self.target

        move_percent = 1 - self.steps / self.speed
        self.rect.topleft = [x1 + (x2 - x1) * move_percent, y1 + (y2 - y1) * move_percent]

        self.steps -= 1

        if not self.steps:
            self.rect.topleft = self.target
            x, y = self.move_vector
            self.move(x, y)

    def draw(self):
        if self.frame is not None:
            if isinstance(self.parent, Menu):
                self.parent.window.blit(self.frame, self.rect)
            elif isinstance(self.parent, Frame):
                self.parent.Surface.blit(self.frame, self.rect)

        self.update_anim()