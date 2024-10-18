import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen width: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Internal clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        color = 'black'
        screen.fill(color)
        pygame.display.flip()

        # Sets the frame rate to 60 and tracks the elapsed time for each frame
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
