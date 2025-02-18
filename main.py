from maze import Maze
from maze_solver import Window

def main():
    win_width = 800
    win_height = 600
    cell_size_x = 50
    cell_size_y = 50
    num_cols = win_width // cell_size_x  # Number of columns
    num_rows = win_height // cell_size_y  # Number of rows

    win = Window(win_width, win_height)  # Create window

    # Create and draw the maze
    maze = Maze(20, 20, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    win.wait_for_close()  # Keep window open

if __name__ == "__main__":
    main()


