import pygame
import math
from projectile import Projectile


class Player:
    def __init__(self, id, x, y, radius, color=(0, 0, 255)):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 3
        self.alive = True
        self.health = 100

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

    def shoot(self, mouse_x, mouse_y):
        angle = self.calculate_angle(self.x, self.y, mouse_x, mouse_y)
        x_shifted = self.x + self.radius * 1.5 * math.cos(angle)
        y_shifted = self.y + self.radius * 1.5 * math.sin(angle)
        return Projectile(x_shifted, y_shifted, angle)

    def take_damage(self):
        print('ohno got hit')
        self.health -= 10
        if self.health < 1:
            print('ohno im dead')
            self.alive = False


    def calculate_angle(self, x, y, mouse_x, mouse_y):
        # Calculate the angle in radians between the object and the mouse position
        print("Player x: " + str(x) + "Player y: " + str(y) + "Mouse x: " + str(mouse_x) + "Mouse y: " + str(mouse_y))
        delta_x = mouse_x - x
        delta_y = mouse_y - y
        angle_rad = math.atan2(delta_y, delta_x)
        return angle_rad
