import pygame
import math

MAX_RANGE = 200
SPEED = 5
DAMAGE = 10

class Projectile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = SPEED
        self.change_x = -math.sin(angle - math.pi / 2) * self.speed
        self.change_y = math.cos(angle - math.pi / 2) * self.speed
        self.damage = DAMAGE
        self.distance = 0
        self.active = True

    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 0), (self.x, self.y), 3)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        self.distance += self.speed
        if self.distance > MAX_RANGE:
            self.active = False
