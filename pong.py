import pygame
import classes
import constants
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
paddleA = classes.Paddle(constants.WHITE, 10, 100)
paddleA.rect.x = constants.paddle_a_x
paddleA.rect.y = constants.paddle_a_y

paddleB = classes.Paddle(constants.WHITE, 10, 100)
paddleB.rect.x = constants.paddle_b_x
paddleB.rect.y = constants.paddle_b_y

ball = classes.Ball(constants.WHITE, 10, 10)
ball.rect.x = constants.ball_x
ball.rect.y = constants.ball_y

all_sprites = pygame.sprite.Group()

all_sprites.add(paddleA)
all_sprites.add(paddleB)
all_sprites.add(ball)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites.update()

    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(constants.BLACK)
    pygame.draw.line(screen, constants.WHITE, constants.line_start_pos, constants.line_end_pos, constants.line_width)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.flip()
    clock.tick(60)
