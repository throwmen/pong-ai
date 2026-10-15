# ---------------------------------------------------------------------------- #
#                                   Libraries                                  #
# ---------------------------------------------------------------------------- #
import pygame
from .entities.ball import Ball

# ---------------------------------------------------------------------------- #
#                                   Constants                                  #
# ---------------------------------------------------------------------------- #
BASE_DISPLAY = (150, 350) # screen_width, screen_height

# ---------------------------------------------------------------------------- #
#                                 pygame setup                                 #
# ---------------------------------------------------------------------------- #
def main():
    pygame.init()
    screen  = pygame.display.set_mode(BASE_DISPLAY)
    clock   = pygame.time.Clock()
    running = True

    ball = Ball((BASE_DISPLAY[0] // 2, BASE_DISPLAY[1] // 2))

    # ------------------------------ principal loop ------------------------------ #
    while running:
        # poll/search for events
        # pygame.QUIT event means the user closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the movement of the ball
        ball.update(BASE_DISPLAY[0], BASE_DISPLAY[1])

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        ball.draw(screen)

        # Swap buffers: show the frame drawn off-screen all at once (prevents flicker)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()