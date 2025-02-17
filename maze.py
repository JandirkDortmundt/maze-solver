from maze_solver import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._cells = [[None for _ in range(num_rows)] for _ in range(num_cols)]
        
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                x1 = i * self.cell_size_x + self.x1
                y1 = j * self.cell_size_y + self.y1
                x2 = (i + 1) * self.cell_size_x + self.x1
                y2 = (j + 1) * self.cell_size_y + self.y1

                self._cells[i][j] = Cell(x1=x1, x2=x2, y1=y1, y2=y2, win=self.win)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        if cell:
            cell.draw()
            self._animate()

    def _animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)



