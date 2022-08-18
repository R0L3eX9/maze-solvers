from typing import Tuple
import pygame


class GameUtils:
    def __init__(self):
        self.WHITE: Tuple[int, int, int] = (255, 255, 255)
        self.YELLOW: Tuple[int, int, int] = (226, 255, 0)
        self.RED: Tuple[int, int, int] = (255, 0, 0)
        self.BLACK: Tuple[int, int, int] = (0, 0, 0)

    def create_rect(self, X: float, Y: float, WIDTH: float, HEIGHT: float):
        return pygame.Rect(X, Y, WIDTH, HEIGHT)
