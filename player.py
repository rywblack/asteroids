import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
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
        # sub-classes must override
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points,2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.timer -= dt

        if keys[pygame.K_a]:
           self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
           self.acceleration -= forward * ACCELERATION_RATE * dt 

        if keys[pygame.K_w]:
           self.acceleration += forward * ACCELERATION_RATE * dt

        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)
                self.timer = PLAYER_SHOOT_COOLDOWN

            

        self.velocity += self.acceleration * dt

        damping = 0.9 
        self.velocity *= damping

        speed = self.velocity.length()
        if speed > MAX_SPEED:
            self.velocity = self.velocity.normalize() * MAX_SPEED

        self.move(dt)

        

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        self.position += self.velocity * dt
    
    def shoot(self, dt):
        shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
