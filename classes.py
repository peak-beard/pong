import pygame
from random import randint
import constants


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


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Ball, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLACK)
        self.image.set_colorkey(constants.BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
