from maze import Maze
from maze_solver import Window

def test_maze(num_rows, num_cols, cell_size_x, cell_size_y, seed, description):
    # Create new window for each test
    win_width = cell_size_x * num_cols + 40  # Add some padding
    win_height = cell_size_y * num_rows + 40
    win = Window(win_width, win_height)
    
    print(f"\nTesting {description}")
    maze = Maze(20, 20, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=seed)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    
    print("Attempting to solve maze...")
    if maze.solve():
        print("Maze solved successfully!")
    else:
        print("No solution found!")

    win.wait_for_close()

def main():
    # Test Case 1: Simple maze with seed=42
    test_maze(12, 16, 50, 50, 42, "simple maze with seed 42")
    
    # Test Case 2: Different path maze with seed=123
    test_maze(12, 16, 50, 50, 123, "different maze with seed 123")
    
    # Test Case 3: Small 3x3 maze for easier debugging
    test_maze(3, 3, 50, 50, 7, "small 3x3 maze")

if __name__ == "__main__":
    main()
