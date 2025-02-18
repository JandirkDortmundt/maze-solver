from maze_solver import Cell
import time
import random

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
        seed=None,
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
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = random.seed()

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
            time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.has_top_wall = False
        top_left.draw()
        self._animate()
        bottom_right = self._cells[-1][-1]
        bottom_right.has_bottom_wall = False
        bottom_right.draw()
        self._animate()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i - 1 >= 0 and self._cells[i-1][j].visited is False:
                to_visit.append([i-1,j])
            if i + 1 < self.num_cols and self._cells[i+1][j].visited is False:
                to_visit.append([i+1,j])
            if j - 1 >= 0 and self._cells[i][j-1].visited is False:
                to_visit.append([i,j-1])
            if j + 1 < self.num_rows and self._cells[i][j+1].visited is False:
                to_visit.append([i,j+1])
            if len(to_visit) == 0:
                current_cell.draw()
                self._animate()
                return
            else:
                next_ij = to_visit[random.randrange(len(to_visit))]
                print(f"next ij:{next_ij}")
                print(f"next ij first element:{next_ij[0]}")
                next_cell = self._cells[next_ij[0]][next_ij[1]]
                if next_ij[0] -i == -1: #next cell is left
                    #break left wall from current and the right wall from next
                    current_cell.has_left_wall = False
                    current_cell.draw()
                    self._animate()
                    next_cell.has_right_wall = False
                    next_cell.draw()
                    self._animate() 
                if next_ij[0] -i == 1: #next cell is right
                    #break right wall from current and the left wall from next
                    current_cell.has_right_wall = False
                    current_cell.draw()
                    self._animate()
                    next_cell.has_left_wall = False
                    next_cell.draw()
                    self._animate()
                if next_ij[1] -j == -1: #next cell is above 
                    #break top wall from current and the bottom wall from next
                    current_cell.has_top_wall = False
                    current_cell.draw()
                    self._animate()
                    next_cell.has_bottom_wall = False
                    next_cell.draw()
                    self._animate()
                if next_ij[1] -j == 1: #next cell is below
                    #break bottom wall from current and the top wall from next
                    current_cell.has_bottom_wall = False
                    current_cell.draw()
                    self._animate()
                    next_cell.has_top_wall = False
                    next_cell.draw()
                    self._animate()
                self._break_walls_r(next_ij[0],next_ij[1])








            



