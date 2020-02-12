import pygame
import constants
from pygame.locals import (
    K_ESCAPE,
    K_w,
    K_s,
    K_UP,
    K_DOWN,
    KEYDOWN,
    QUIT
)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Paddle, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLACK)
        self.image.set_colorkey(constants.BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.move_ip(0, -pixels)
        if self.rect.top <= 0:
            self.rect.top = 0

    def moveDown(self, pixels):
        self.rect.move_ip(0, pixels)
        if self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT
