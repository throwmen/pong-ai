# ---------------------------------------------------------------------------- #
#                                   Libraries                                  #
# ---------------------------------------------------------------------------- #
import pygame
from .entities.ball import Ball
from .entities.paddle import Paddle
from .controllers.keyboard import KeyboardController

# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #
BASE_DISPLAY = (250, 350) # screen_width, screen_height
LEFT_PADDLE_UP_KEYS = [pygame.K_w, pygame.K_UP]
LEFT_PADDLE_DOWN_KEYS = [pygame.K_s, pygame.K_DOWN]
RIGHT_PADDLE_UP_KEYS = [pygame.K_i, pygame.K_o]
RIGHT_PADDLE_DOWN_KEYS = [pygame.K_k, pygame.K_l]

# ---------------------------------------------------------------------------- #
#                                 pygame setup                                 #
# ---------------------------------------------------------------------------- #
def main():
    pygame.init()
    screen  = pygame.display.set_mode(BASE_DISPLAY)
    clock   = pygame.time.Clock()
    running = True

    ball = Ball((BASE_DISPLAY[0] // 2, BASE_DISPLAY[1] // 2))
    left_paddle = Paddle((10, BASE_DISPLAY[1] // 2))
    right_paddle = Paddle((BASE_DISPLAY[0] - 10, BASE_DISPLAY[1] // 2))
    left_paddle_controller = KeyboardController(LEFT_PADDLE_UP_KEYS, LEFT_PADDLE_DOWN_KEYS)
    right_paddle_controller = KeyboardController(RIGHT_PADDLE_UP_KEYS, RIGHT_PADDLE_DOWN_KEYS)

    # ------------------------------ principal loop ------------------------------ #
    while running:
        # poll/search for events
        # pygame.QUIT event means the user closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the movement of the ball
        ball.update(BASE_DISPLAY[0], BASE_DISPLAY[1])

        # Update the movement of the left_paddle
        left_paddle.update(BASE_DISPLAY[1], left_paddle_controller.decide())

        # Update the movement of the right_paddle
        right_paddle.update(BASE_DISPLAY[1], right_paddle_controller.decide())

        # Check colission between the paddle and the ball
        if(ball.rect.colliderect(left_paddle.rect)):
            ball.velocity.x *= -1
            ball.rect.left = left_paddle.rect.right

        elif(ball.rect.colliderect(right_paddle.rect)):
            ball.velocity.x *= -1
            ball.rect.right = right_paddle.rect.left

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # Draw the objects
        ball.draw(screen)
        left_paddle.draw(screen)
        right_paddle.draw(screen)

        # Swap buffers: show the frame drawn off-screen all at once (prevents flicker)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()