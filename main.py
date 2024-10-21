import sys
import pygame

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    # Starts the game and sets display mode
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Internal clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Create the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Instantiate player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Instantiate asteroid objects
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield = AsteroidField()

    # Instantiate shot objects
    Shot.containers = (shots, updatable, drawable)
    
    while True:
        # Quits the game when pressing the window's close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills the screen with the color black
        color = 'black'
        screen.fill(color)

        # Draws everything to the screen
        for item in drawable:
            item.draw(screen)

        # Updates the state of every object
        for item in updatable:
            item.update(dt)
        
        # Updates the display surface to the screen
        pygame.display.flip()
        
        # Checks if the player has collided with an asteroid
        for asteroid in asteroids:
            collision = asteroid.check_collision(player)

            if collision:
                print ("Game over!")
                sys.exit()

        # Checks if a bullet has collided with an asteroid
        for asteroid in asteroids:
            for shot in shots:
                collision = asteroid.check_collision(shot)

                if collision:
                    asteroid.kill()
                    shot.kill()
        
        # Sets the frame rate to 60 and tracks the elapsed time for each frame
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
