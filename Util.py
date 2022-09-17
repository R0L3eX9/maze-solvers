from typing import Tuple
import pygame


class GameUtils:
    def __init__(self):
        self.WHITE: Tuple[int, int, int] = (255, 255, 255)
        self.YELLOW: Tuple[int, int, int] = (255, 236, 0)
        self.RED: Tuple[int, int, int] = (225, 16, 16)
        self.BLUE: Tuple[int, int, int] = (0, 145, 255)
        self.INDIGO: Tuple[int, int, int] = (0, 17, 255)
        self.PURPLE: Tuple[int, int, int] = (106, 0, 255)
        self.GREEN: Tuple[int, int, int] = (16, 255, 0)
        self.BLACK: Tuple[int, int, int] = (0, 0, 0)
        self.ORANGE: Tuple[int, int, int] = (255, 127, 0)
        self.GRAY: Tuple[int, int, int] = (50, 52, 54)
        self.STEELBLUE: Tuple[int, int, int] = (142, 186, 202)

    def create_rect(self, X: float, Y: float, WIDTH: float, HEIGHT: float):
        return pygame.Rect(X, Y, WIDTH, HEIGHT)
