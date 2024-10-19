import pygame
from constants import *
from circleshape import *
from player import *

def main():
    # Starts the game and sets display mode
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Internal clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Quits the game when pressing the window's close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills the screen with the color black
        color = 'black'
        screen.fill(color)

        # Draws player on screen
        player.draw(screen)

        # Updates the player position
        player.update(dt)
        
        # Updates the display surface to the screen
        pygame.display.flip()

        # Sets the frame rate to 60 and tracks the elapsed time for each frame
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
