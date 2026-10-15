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
UP_KEYS = [pygame.K_w, pygame.K_UP]
DOWN_KEYS = [pygame.K_s, pygame.K_DOWN]

# ---------------------------------------------------------------------------- #
#                                 pygame setup                                 #
# ---------------------------------------------------------------------------- #
def main():
    pygame.init()
    screen  = pygame.display.set_mode(BASE_DISPLAY)
    clock   = pygame.time.Clock()
    running = True

    ball = Ball((BASE_DISPLAY[0] // 2, BASE_DISPLAY[1] // 2))
    paddle = Paddle((10, BASE_DISPLAY[1] // 2))
    keyboard_controller = KeyboardController(UP_KEYS, DOWN_KEYS)

    # ------------------------------ principal loop ------------------------------ #
    while running:
        # poll/search for events
        # pygame.QUIT event means the user closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the movement of the ball
        ball.update(BASE_DISPLAY[0], BASE_DISPLAY[1])

        # Update the movement of the paddle
        paddle.update(BASE_DISPLAY[1], keyboard_controller.decide())

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # Draw the objects
        ball.draw(screen)
        paddle.draw(screen)

        # Swap buffers: show the frame drawn off-screen all at once (prevents flicker)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()