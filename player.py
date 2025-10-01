import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", points=self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        new_dt = abs(dt)
        self.timer -= new_dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            dt = -abs(dt)
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            dt = -abs(dt)
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
        if keys[pygame.K_LSHIFT]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * (PLAYER_SPEED * 2) * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position[0], self.position[1])
        shot_vel = pygame.Vector2(0, 1)
        shot_vel = shot_vel.rotate(self.rotation)
        shot_vel *= PLAYER_SHOOT_SPEED
        new_shot.velocity = shot_vel
        
