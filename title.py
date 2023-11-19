import pygame

class Title:
    def __init__(self, parent):
        """
        The title for the main menu
        :param parent:
        """

        self.parent = parent

        self.title = pygame.transform.scale(pygame.image.load("placeholder_title.png"), (400, 100))

        width, height = self.title.get_size()
        height *= 1.5
        self.Surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

        self.y = 200
        self.x = (parent.window.get_width() - self.Surface.get_width()) / 2

        self.width, self.height = self.Surface.get_size()

        self.title_y = height - self.title.get_height()
        self.move_direction = -0.5

        self.size_difference = self.height - self.title.get_height()

        self.shiny_line = pygame.Surface((self.title.get_height(), ) * 2, pygame.SRCALPHA)

        # this isnt that efficient but it only happens once ig
        pygame.draw.line(self.shiny_line, (255, 150, 0, 0), (0, 0), (self.title.get_height(), ) * 2, 10)
        pygame.draw.line(self.shiny_line, (255, 190, 0, 0), (0, 0), (self.title.get_height(), ) * 2, 6)
        pygame.draw.line(self.shiny_line, (255, 230, 0, 0), (0, 0), (self.title.get_height(), ) * 2, 4)
        pygame.draw.line(self.shiny_line, (255, 255, 0, 0), (0, 0), (self.title.get_height(), ) * 2, 2)

        self.line_x = -self.shiny_line.get_width()

        self.count = self.delay = 5 * 60 # the delay between the shines

    def animate(self):
        temp = self.title.copy()
        temp.blit(self.shiny_line, (self.line_x, 0), special_flags=pygame.BLEND_RGBA_ADD)
        self.Surface.fill((0, 0, 0, 0))
        self.Surface.blit(temp, (0, self.title_y))

        self.title_y += self.move_direction
        if self.title_y <= 0 or self.title_y >= self.size_difference:
            self.move_direction *= -1

        self.line_x += 10 * (self.count < 0)
        self.count -= 1
        if self.line_x >= self.width + self.shiny_line.get_width():
            self.line_x = -self.shiny_line.get_width()
            self.count = self.delay


    def draw(self):
        self.animate()

        self.parent.window.blit(self.Surface, (self.x, self.y))