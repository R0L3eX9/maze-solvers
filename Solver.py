import time
from Node import Node
from Util import GameUtils
from typing import List, Tuple


class Solver:
    # We will denote the:
    #   blocked nodes as -1
    #   empty nodes as 0
    #   starting node as 1
    #   ending node as 2

    def __init__(self, grid: List[List[Node]], update_window):
        self._update_window = update_window
        self._grid: List[List[Node]] = grid
        self._util: GameUtils = GameUtils()

        self.dy: List[int] = [0, 0, -1, 1]
        self.dx: List[int] = [-1, 1, 0, 0]
        self._timer = 0.0001

    def inside_grid(self, X: int, Y: int, W: int, L: int):
        return 0 <= X < W and 0 <= Y < L

    def change_cell(self, node: Node, colour: Tuple[int, int, int], ms: float):
        if node.colour != self._util.RED and node.colour != self._util.GREEN:
            node.colour = colour
            self._update_window()
            time.sleep(ms)

    def reconstruct_path(self, dist: List[List[int]]):
        queue: List[Tuple[int, int]] = []
        mat: List[List[Node]] = self._grid
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col].colour == self._util.GREEN:
                    queue.append((row, col))

        while len(queue):
            cur: Tuple[int, int] = queue[0]
            queue.pop(0)

            min_dist = 1000
            node: Tuple[int, int] = (0, 0)

            for d in range(len(self.dy)):
                new_row: int = cur[0] + self.dx[d]
                new_col: int = cur[1] + self.dy[d]

                if (self.inside_grid(new_row, new_col, len(mat), len(mat[0]))
                   and mat[new_row][new_col].colour != self._util.GRAY
                   and dist[new_row][new_col] < min_dist):
                    min_dist = dist[new_row][new_col]
                    node = (new_row, new_col)
            if mat[node[0]][node[1]].colour == self._util.RED:
                break

            if min_dist != 1000:
                self.change_cell(mat[node[0]][node[1]],
                                 self._util.ORANGE,
                                 self._timer * 100)
                queue.append(node)

    def bfs(self):
        mat: List[List[Node]] = self._grid
        dist: List[List[int]] = [[1000 for _ in range(len(mat[0]))]
                                 for _ in range(len(mat))]

        queue: List[Tuple[int, int]] = []
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col].colour == self._util.RED:
                    dist[row][col] = 0
                    queue.append((row, col))

        while len(queue):
            cur: Tuple[int, int] = queue[0]
            queue.pop(0)

            self.change_cell(mat[cur[0]][cur[1]], self._util.BLUE, self._timer)

            for d in range(len(self.dy)):
                new_row: int = cur[0] + self.dx[d]
                new_col: int = cur[1] + self.dy[d]

                if (self.inside_grid(new_row, new_col, len(mat), len(mat[0]))
                   and mat[new_row][new_col].colour != self._util.GRAY):
                    if dist[cur[0]][cur[1]] + 1 < dist[new_row][new_col]:
                        dist[new_row][new_col] = dist[cur[0]][cur[1]] + 1

                        if mat[new_row][new_col].colour == self._util.GREEN:
                            queue.clear()
                            break

                        self.change_cell(mat[new_row][new_col],
                                         self._util.YELLOW, self._timer)
                        queue.append((new_row, new_col))

                        self._update_window()
                        time.sleep(0.01)

            self.change_cell(mat[cur[0]][cur[1]],
                             self._util.INDIGO,
                             self._timer)

        self.reconstruct_path(dist)
