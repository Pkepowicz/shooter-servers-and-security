import math
from constants import WIDTH, HEIGHT, PROJECTILE_RADIUS, PROJECTILE_MAX_RANGE, PROJECTILE_SPEED, PROJECTILE_DAMAGE


class Projectile:
    def __init__(self, x, y, angle):
        self.id = None
        self.x = x
        self.y = y
        self.speed = PROJECTILE_SPEED
        self.change_x = -math.sin(angle - math.pi / 2) * self.speed
        self.change_y = math.cos(angle - math.pi / 2) * self.speed
        self.damage = PROJECTILE_DAMAGE
        self.radius = PROJECTILE_RADIUS
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
        if self.distance > PROJECTILE_MAX_RANGE:
            self.active = False

    def check_bounds(self):
        if self.x < 1 or self.x > WIDTH - 1:
            return False
        if self.y < 1 or self.y > HEIGHT - 1:
            return False
        return True
