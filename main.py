import pygame
from constants import *
from circleshape import CircleShape
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    #Set screen rez
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #Create pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Place groups into player container
    Player.containers = (updatable, drawable)
    #Create player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    AsteroidField.containers = (updatable,)
    #Asteroid field
    asteroidfield = AsteroidField()
  
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    #infinite loop
    while True:
        screen.fill("black")
        #draws player
        for item in drawable:
            item.draw(screen)
        #draws screen
        updatable.update(dt)
        #Checks collision for player and asteroid
        for ast in asteroids:
            if ast.collision(player):
                print("Game over!")
                pygame.QUIT
                return
        for ast in asteroids:
            for bullet in shots:
                if bullet.collision(ast):
                    ast.split()
                    bullet.kill()
        pygame.display.flip()

        #Allows to quit with x on gui
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta = clock.tick(60)
        dt = delta / 1000
if __name__ == "__main__":
    main()
