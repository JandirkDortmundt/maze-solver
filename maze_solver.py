from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        """Initialize the window with a given width and height."""
        self.__root = Tk()  # Create the main window
        self.__root.title("Maze Solver!")  # Set the window title
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)  # Expand to fit the window

        self.__running = False  # Tracks if the window is running

        # Ensure window closes properly when 'X' button is clicked
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Redraw the window by updating the event loop."""
        self.__root.update_idletasks()  # Handle background tasks
        self.__root.update()  # Process pending events

    def wait_for_close(self):
        """Keep the window open until manually closed."""
        self.__running = True  # Mark window as running
        while self.__running:
            self.redraw()  # Continuously refresh the window

    def close(self):
        """Close the window by stopping the event loop."""
        self.__running = False

    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Line:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas,fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self
                 ,has_left_wall=True
                 ,has_right_wall=True
                 ,has_top_wall=True
                 ,has_bottom_wall=True
                 ,x1=0
                 ,x2=50
                 ,y1=0
                 ,y2=50
                 ,win=None
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win= win

    def draw(self):
        if self._win is not None:
            if self.has_left_wall:
                self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"black")
            if self.has_right_wall:
                self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"black")
            if self.has_top_wall:
                self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"black")
            if self.has_bottom_wall:
                self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"black")

    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2

        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2

        color = "red" if not undo else "gray"

        self._win.draw_line(Line(Point(x1, y1), Point(x2, y2)), fill_color=color)









