import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_vol_1 = self.velocity.rotate(new_angle)
        new_vol_2 = self.velocity.rotate(-new_angle)
        smol_Ast = old_radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, smol_Ast)
        new_ast_2 = Asteroid(self.position.x, self.position.y, smol_Ast)
        new_speed_1 = 1.2 * new_vol_1
        new_speed_2 = 1.2 * new_vol_2
        new_ast_1.velocity = new_speed_1
        new_ast_2.velocity = new_speed_2



        