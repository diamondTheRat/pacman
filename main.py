import pygame


WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

<<<<<<< HEAD
# Woahhh
BGCOLOR = (50, 54, 61)
# dddddddddDDDDDDDDDDDdDDDD
=======

BGCOLOR = (51, 54, 61)
>>>>>>> 0454659ebe433ffe65545ecc6ca1e50765df93b8


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