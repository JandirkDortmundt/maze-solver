import unittest
from maze import Maze
from maze_solver import Cell, Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_cells_are_not_none(self):
        """Test if all cells in the maze are initialized properly."""
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in range(num_cols):
            for row in range(num_rows):
                self.assertIsNotNone(m1._cells[col][row])

    def test_cell_walls_exist_by_default(self):
        """Test that a new cell has all walls by default."""
        cell = Cell()
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_draw_move(self):
        """Test if cell draw_move generates a valid move."""
        win = Window(100, 100)
        c1 = Cell(x1=0, y1=0, x2=50, y2=50, win=win)
        c2 = Cell(x1=50, y1=0, x2=100, y2=50, win=win)

        # Try moving from c1 to c2 (should be a valid move)
        try:
            c1.draw_move(c2)
        except Exception as e:
            self.fail(f"draw_move raised an exception: {e}")

    def test_maze_initialization_no_crash(self):
        """Ensure that initializing a large maze doesn't crash."""
        try:
            m1 = Maze(0, 0, 50, 50, 10, 10)
        except Exception as e:
            self.fail(f"Large maze initialization failed: {e}")

    def test_maze_entrance_and_exit(self):
        """Test that the entrance and exit walls are correctly removed."""
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Break entrance and exit
        m1._break_entrance_and_exit()

        # Check if top-left cell has no top wall
        self.assertFalse(m1._cells[0][0].has_top_wall, "Entrance wall was not removed!")

        # Check if bottom-right cell has no bottom wall
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall, "Exit wall was not removed!")

    def test_reset_cells_visited(self):
        """Test that reset_cells_visited properly resets all cells to unvisited."""
        # Create a small test maze
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Mark some cells as visited
        m1._cells[0][0].visited = True
        m1._cells[1][1].visited = True
        m1._cells[2][2].visited = True
        
        # Reset all cells
        m1._reset_cells_visited()
        
        # Verify all cells are now unvisited
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(
                    m1._cells[i][j].visited,
                    f"Cell at ({i},{j}) was not reset to unvisited"
                )

if __name__ == "__main__":
    unittest.main()
