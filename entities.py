import pygame
from base_classes import Menu, Frame


rotation_function = lambda r: r[1] * 90 + (r[0] - 1) // 2 * 180

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

        self.base_frames = []

        self.frames = []
        self.frame_index = 0
        self.frame = None
        self.frame_rate = 1 / frames

        self.start_pos = self.target = self.rect.topleft # the position it starts at and the position it's moving to
        self.move_vector = (0, 0)
        self.previous_move_vector = (0, 0)

        self.move_queue = (0, 0)

        self.steps = 0


        self.load_anim()

    def load_anim(self):
        pass

    def rotate_frames(self):
        if self.move_vector == (0, 0): return # pacman stopped moving

        new_frames = []
        for frame in self.base_frames:
            new_frame = pygame.transform.rotate(frame, rotation_function(self.move_vector))
            if self.move_vector == (-1, 0):
                new_frame = pygame.transform.flip(new_frame, flip_x=False, flip_y=True)
            new_frames.append(new_frame)

        self.frames = new_frames


    def update_anim(self):
        if not self.move_vector == self.previous_move_vector:
            self.rotate_frames()

        self.previous_move_vector = self.move_vector

        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.frames) or self.frame_index <= 0:
            self.frame_index -= self.frame_rate
            self.frame_rate *= -1

        self.frame = self.frames[int(self.frame_index)]

    def stop_moving(self):
        self.move_vector = (0, 0)
        self.move_queue = (0, 0)

    def collides(self, position: tuple[int, int]):
        x, y = position
        if self.parent.room["walls"][y][x] == "0":
            return True
        return False

    def move(self, horizontally: int, vertically: int, auto: bool=False):
        """
        :param auto: if u tell it to move leave this off, if it's in the update function leave it on
        """
        if not auto:
            self.move_queue = (horizontally, vertically)

        if not tuple(self.rect.topleft) == tuple(self.target): return # if it didn't finish moving it won't change direction
        x, y = self.rect.topleft

        self.start_pos = [x, y]
        pos = [x // self.width + self.move_queue[0], y // self.height + self.move_queue[1]]

        if not self.collides(pos):
            self.move_vector = self.move_queue
        else:
            self.move_vector = (horizontally, vertically)

        self.target = (x + self.height * self.move_vector[0], y + self.height * self.move_vector[1])
        self.steps = self.speed

    def update(self):
        if not self.steps: return

        x1, y1 = self.start_pos
        x2, y2 = self.target

        wx, wy = x2 // self.width, y2 // self.height
        if self.collides([wx, wy]):
            self.move_vector = self.move_queue
            self.target = self.start_pos
            self.move_vector = (0, 0)
            self.steps = 0
            return

        move_percent = 1 - self.steps / self.speed
        self.rect.topleft = [x1 + (x2 - x1) * move_percent, y1 + (y2 - y1) * move_percent]

        self.steps -= 1

        if not self.steps:
            self.rect.topleft = self.target
            x, y = self.move_vector
            self.move(x, y, True)

    def draw(self):
        if self.frame is not None:
            self.parent.parent.window.blit(self.frame, self.rect)

        self.update_anim()