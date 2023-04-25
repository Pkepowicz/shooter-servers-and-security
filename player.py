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

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # self.update()


    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def shoot(self, mouse_x, mouse_y):
        x_center = self.x
        y_center = self.y
        angle = self.calculate_angle(x_center, y_center, mouse_x, mouse_y)
        return Projectile(x_center, y_center, angle)

    def calculate_angle(self, x, y, mouse_x, mouse_y):
        # Calculate the angle in radians between the object and the mouse position
        print("Player x: " + str(x) + "Player y: " + str(y) + "Mouse x: " + str(mouse_x) + "Mouse y: " + str(mouse_y))
        delta_x = mouse_x - x
        delta_y = mouse_y - y
        angle_rad = math.atan2(delta_y, delta_x)
        return angle_rad
