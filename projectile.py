import pygame
import math

MAX_RANGE = 200
SPEED = 5
DAMAGE = 10


class Projectile:
    def __init__(self, x, y, angle):
        self.id = None
        self.x = x
        self.y = y
        self.speed = SPEED
        self.change_x = -math.sin(angle - math.pi / 2) * self.speed
        self.change_y = math.cos(angle - math.pi / 2) * self.speed
        self.damage = DAMAGE
        self.radius = 7
        self.distance = 0
        self.active = True
        self.known = 1

    def draw(self, win, sprite):
        win.blit(sprite, (self.x-7, self.y-7))

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        self.distance += self.speed
        if not self.check_bounds():
            self.active = False
        if self.distance > MAX_RANGE:
            self.active = False

    def check_bounds(self):
        if self.x < 1 or self.x > 499:
            return False
        if self.y < 1 or self.y > 499:
            return False
        return True
