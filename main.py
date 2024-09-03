import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidField = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    n=1
    while n != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        clock.tick(60)
        dt = clock.tick(60)/1000
        #player.update(dt)
        #player.draw(screen)
        for instance in updatable:
            instance.update(dt)
        for instance in drawable:
            instance.draw(screen) 
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot) == True:
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()

if __name__ == "__main__":
    main()
