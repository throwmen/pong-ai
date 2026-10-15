import pygame
from .controller import Controller

class KeyboardController(Controller):
    def __init__(self, up_keys: list[int], down_keys: list[int]) -> None:
        self.up_keys   = up_keys
        self.down_keys = down_keys

    def decide(self) -> int:
        pressed_keys = pygame.key.get_pressed()
        moving_up    = any(pressed_keys[key] for key in self.up_keys)
        moving_down  = any(pressed_keys[key] for key in self.down_keys)
        return moving_down - moving_up