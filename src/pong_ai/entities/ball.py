# ---------------------------------------------------------------------------- #
#                                   Libraries                                  #
# ---------------------------------------------------------------------------- #
import pygame
from pygame.typing import ColorLike, Point

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
        self.rect        = pygame.Rect(0, 0, radius * 2, radius * 2)
        self.rect.center = position
        self.color       = color
        self.radius      = radius
        self.velocity    = pygame.Vector2(speed)

    def update(self, screen_width: int, screen_height: int) -> None:
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.velocity.y *= -1

        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.velocity.x *= -1

    def draw(self, surface : pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)
