from typing import Tuple


class Node:
    def __init__(self, COLOUR: Tuple[int, int, int],
                 X: float, Y: float, WIDTH: float):
        self.colour: Tuple[int, int, int] = COLOUR
        self.x: float = X
        self.y: float = Y
        self.width: float = WIDTH
        self.height: float = WIDTH
