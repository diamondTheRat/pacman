import pygame


WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


BGCOLOR = (50, 54, 61)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


def draw():
    WIN.fill(BGCOLOR)


    pygame.display.update()


def main():


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        handle_events()


        draw()


if __name__ == "__main__":
    main()