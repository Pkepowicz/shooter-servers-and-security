import pygame
import math
from projectile import Projectile

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

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

        self.update()


    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def shoot(self, mouse_x, mouse_y):
        x_center = self.x + self.width / 2
        y_center = self.y + self.height / 2
        angle = self.calculate_angle(x_center, y_center, mouse_x, mouse_y)
        return Projectile(x_center, y_center, angle)

    def calculate_angle(self, x, y, mouse_x, mouse_y):
        # Calculate the angle in radians between the object and the mouse position
        print("Player x: " + str(x) + "Player y: " + str(y) + "Mouse x: " + str(mouse_x) + "Mouse y: " + str(mouse_y))
        delta_x = mouse_x - x
        delta_y = mouse_y - y
        angle_rad = math.atan2(delta_y, delta_x)
        return angle_rad
