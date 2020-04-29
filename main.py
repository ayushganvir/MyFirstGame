import pygame
from core.loop import game_loop
from nbody.game import game
from nbody.parts import background_colour, screen
from setup import Universe

pygame.display.set_caption('Space')
universe = Universe(100, 10)
game_loop(True, background_colour, screen, game, universe)
