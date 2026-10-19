# ---------------------------------------------------------------------------- #
#                                   Libraries                                  #
# ---------------------------------------------------------------------------- #
import pygame
from pygame.typing import ColorLike, Point
import time

# ---------------------------------------------------------------------------- #
#                                     Ball                                     #
# ---------------------------------------------------------------------------- #
class Ball:
    def __init__(
        self, 
        position: Point,
        color:    ColorLike           = "white", 
        radius:   int                 = 8, 
        speed:    tuple[float, float] = (4, 3)
    ) -> None:
        self.initial_position = position
        self.initial_velocity = pygame.Vector2(speed)
        self.rect             = pygame.Rect(0, 0, radius * 2, radius * 2)
        self.rect.center      = position
        self.color            = color
        self.radius           = radius
        self.velocity         = self.initial_velocity.copy()

    def update(self, screen_width: int, screen_height: int) -> None:
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.velocity.y *= -1

    def reset(self) -> None:
        self.rect.center = self.initial_position
        self.velocity    = self.initial_velocity.copy()

    def draw(self, surface : pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)
