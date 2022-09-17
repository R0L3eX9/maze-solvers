from typing import Tuple


class Node:
    def __init__(self, COLOUR: Tuple[int, int, int],
                 X: float, Y: float, WIDTH: float):
        self.colour: Tuple[int, int, int] = COLOUR
        self.x: float = X * 1.00
        self.y: float = Y * 1.00
        self.width: float = WIDTH
        self.height: float = WIDTH

    def clicked(self, X, Y):
        return ((self.x <= X and X <= self.x + self.width) and
                (self.y <= Y and Y <= self.y + self.width))
