# ---------------------------------------------------------------------------- #
#                                   Libraries                                  #
# ---------------------------------------------------------------------------- #
import pygame
from pygame.typing import ColorLike, Point

# ---------------------------------------------------------------------------- #
#                                   Paddle                                     #
# ---------------------------------------------------------------------------- #
class Paddle:
    def __init__(
        self, 
        position: Point,
        color:    ColorLike = "white",
        width:    int       = 15,          
        height:   int       = 80,
        speed:    float       = 5
    ) -> None:
        self.rect        = pygame.Rect(0, 0, width, height)
        self.rect.center = position
        self.color       = color
        self.velocity    = speed

    def update(self, screen_height: int, direction: int = 0) -> None:
        self.rect.y += self.velocity * direction

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def draw(self, surface : pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
