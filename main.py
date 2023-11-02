import pygame
from game import Game

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.RESIZABLE)

game = Game(WIN)


BGCOLOR = (50, 54, 61)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                game.check_clicks()


def draw():
    WIN.fill(BGCOLOR)

    game.draw()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        handle_events()

        draw()


if __name__ == "__main__":
    main()