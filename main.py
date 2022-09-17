import pygame
from typing import List, Tuple
from Grid import Grid
from Util import GameUtils
from Solver import Solver
from Node import Node


class Main:
    def __init__(self):
        self._running: bool = False

        self._win_size: Tuple[int, int] = (1024, 1024)
        self._window = None
        self._game_stage = 0

        self._node_in_pixels: int = 32
        self._util: GameUtils = GameUtils()
        self._Grid: Grid = Grid(self._win_size,
                                self._node_in_pixels)

    def init_window(self):
        pygame.init()
        pygame.font.init()

        self._window = pygame.display.set_mode(self._win_size)
        self._Grid.display_nodes(self._window)

    def update_window(self):
        self._Grid.display_nodes(self._window)
        pygame.display.flip()

    def start(self):
        self._running = True

        self.init_window()

        while self._running:
            self.event_loop()
            self.update_window()

    def change_grid(self, remove: bool):
        click_x, click_y = pygame.mouse.get_pos()
        grid = self._Grid.get_grid()

        for row in grid:
            for node in row:
                if node.clicked(click_x, click_y):
                    if remove:
                        if self._game_stage == 2:
                            if node.colour == self._util.GREEN:
                                node.colour = self._util.WHITE
                                self._game_stage -= 1
                            elif node.colour != self._util.RED:
                                node.colour = self._util.WHITE
                        elif self._game_stage == 1:
                            if node.colour == self._util.RED:
                                self._game_stage -= 1
                            node.colour = self._util.WHITE
                    else:
                        if self._game_stage == 0:
                            self._game_stage += 1
                            node.colour = self._util.RED
                        elif self._game_stage == 1:
                            if node.colour != self._util.RED:
                                node.colour = self._util.GREEN
                                self._game_stage += 1
                        else:
                            if (node.colour != self._util.RED and
                               node.colour != self._util.GREEN):
                                node.colour = self._util.GRAY

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            matrix: List[List[Node]] = self._Grid.get_grid()
            solver = Solver(matrix, self.update_window)
            solver.bfs()
        elif pygame.mouse.get_pressed()[0]:
            self.change_grid(False)
        elif pygame.mouse.get_pressed()[2]:
            self.change_grid(True)

    def event_loop(self):
        for event in pygame.event.get():
            self.on_event(event)


if __name__ == "__main__":
    path_vis = Main()
    path_vis.start()
