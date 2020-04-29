import pygame
from core.physics import distance, gravity
from constants import WIDTH, HEIGHT


screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_colour = (0, 0, 0)


class Particle:
    def __init__(self, name, color, size, mass, location, velocity):
        self.name = name
        self.size = size
        self.colour = color
        self.velocity = velocity
        self.mass = mass
        self.location = location

    def distance_from(self, other):
        return distance(self.location.x, self.location.y, other.location.x, other.location.y)

    def gravity_between(self, other):
        return gravity(self.location.x, self.location.y, other.location.x, other.location.y, self.mass)

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.location.x), int(self.location.y)), self.size)

    def moving(self, delta_t, gx, gy):
        self.velocity.x += gx * delta_t
        self.velocity.y += gy * delta_t
        self.location.x += self.velocity.x * delta_t + 0.5 * gx * delta_t ** 2
        self.location.y += self.velocity.y * delta_t + 0.5 * gy * delta_t ** 2
