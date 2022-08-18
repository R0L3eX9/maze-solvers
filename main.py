import pygame
from typing import Tuple
from Grid import Grid


class Main:
    def __init__(self):
        self._running: bool = False

        # TODO Play with the window size
        self._win_size: Tuple[int, int] = (1024, 1024)
        self._window = None

        # For now since window size is a power of 2
        # Node length will also be a power of two for convenience
        self._node_in_pixels: int = 32
        self._Grid: Grid = Grid(self._win_size,
                                self._node_in_pixels)

    def init_window(self):
        pygame.init()
        pygame.font.init()

        self._window = pygame.display.set_mode(self._win_size)
        self._Grid.display_nodes(self._window)

    def update_window(self):
        pass

    def start(self):
        self._running = True

        self.init_window()

        while self._running:
            self.event_loop()
            pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def event_loop(self):
        for event in pygame.event.get():
            self.on_event(event)


if __name__ == "__main__":
    path_vis = Main()
    path_vis.start()
