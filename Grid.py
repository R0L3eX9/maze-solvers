import pygame
from typing import List
from typing import Tuple
from Util import GameUtils
from Node import Node


class Grid:
    def __init__(self, screen_size: Tuple[int, int], node_in_pixels: int):
        self._util: GameUtils = GameUtils()
        self._node_in_pixels: int = node_in_pixels
        self._rows: int = screen_size[0] // self._node_in_pixels
        self._cols: int = screen_size[1] // self._node_in_pixels
        self._grid: List[List[Node]] = self.create_grid(self._node_in_pixels)

    def create_grid(self, pixels: int) -> List[List[Node]]:
        nodes_list: List[List[Node]] = []
        for row in range(self._rows - 2):
            nodes: List[Node] = []
            for col in range(self._cols - 2):
                X: float = (col + 1) * pixels
                Y: float = (row + 1) * pixels
                COLOUR: Tuple[int, int, int] = self._util.WHITE

                nodes.append(Node(COLOUR, X, Y, pixels))
            nodes_list.append(nodes)
        return nodes_list

    def add_border(self, surface, node: Node):
        for i in range(4):
            rect = self._util.create_rect(int(node.x) - i,
                                          int(node.y) - i,
                                          self._node_in_pixels,
                                          self._node_in_pixels)
            pygame.draw.rect(surface, self._util.BLACK, rect,  1)

    def get_grid(self) -> List[List[Node]]:
        return self._grid

    def display_nodes(self, surface):
        for node_list in self._grid:
            for node in node_list:
                self.add_border(surface, node)
                pygame.draw.rect(surface,
                                 node.colour,
                                 self._util.create_rect(
                                     node.x,
                                     node.y,
                                     self._node_in_pixels,
                                     self._node_in_pixels)
                                 )
                # end
