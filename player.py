import pygame
import math
from projectile import Projectile
from constants import WIDTH, HEIGHT, PLAYER_SPEED
class Player:
    def __init__(self, id, x, y, radius, color=(0, 0, 255)):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = PLAYER_SPEED
        self.alive = True
        self.health = 100

    def draw(self, win, sprite):
        win.blit(sprite, (self.x - self.radius/2, self.y - self.radius))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            if self.x > 1:
                self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            if self.x < WIDTH - 1:
                self.x += self.speed

        if keys[pygame.K_UP]:
            if self.y > 1:
                self.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.y < HEIGHT - 1:
                self.y += self.speed

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
