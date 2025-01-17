import turtle

# 1. From our starting position we will first try going north one square and then recursively try our procedure from there.
# 2. If we are not successful by trying a northern path as the first step then we will take a step to the south and recursively repeat our procedure.
# 3. If south does not work then we will try a step to the West as our first step and recursively apply our procedure.
# 4. If north, south, and west have not been successful then we will apply the procedure recursively from a position one step to our east.
# 5. If none of these directions works then there is no way to get out of the maze and we fail

# In this algorithm, there are four base cases to consider:
#     1. The turtle has run into a wall. Since the square is occupied by a wall, no further exploration can take place.
#     2. The turtle has found a square that has already been explored. We do not want to continue exploring from this position so we don’t get into a loop.
#     3. We have found an outside edge, not occupied by a wall. In other words, we have found an exit from the maze.
#     4. We have explored a square unsuccessfully in all four directions.


START = "S"
OBSTACLE = "+"
TRIED = "."
DEAD_END = "-"
PART_OF_PATH = "O"


class Maze:
    def __init__(self, maze_filename):
        with open(maze_filename, "r") as maze_file:
            self.maze_list = [
                [ch for ch in line.rstrip("\n")]
                for line in maze_file.readlines()
            ]
        self.rows_in_maze = len(self.maze_list)
        self.columns_in_maze = len(self.maze_list[0])
        for row_idx, row in enumerate(self.maze_list):
            if START in row:
                self.start_row = row_idx
                self.start_col = row.index(START)
                break

        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(self.columns_in_maze - 1) / 2 - 0.5,
            -(self.rows_in_maze - 1) / 2 - 0.5,
            (self.columns_in_maze - 1) / 2 + 0.5,
            (self.rows_in_maze - 1) / 2 + 0.5,
        )

    def draw_maze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_from(maze, start_row, start_column):
    # try each of four directions from this point until we find a way out. 
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.update_position(start_row, start_column)
    if maze[start_row][start_column] == OBSTACLE:
        return False
    #  2. We have found a square that has already been explored
    if (
        maze[start_row][start_column] == TRIED
        or maze[start_row][start_column] == DEAD_END
    ):
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use logical short circuiting to try each direction in turn (if needed)
    found = (
        search_from(maze, start_row - 1, start_column)
        or search_from(maze, start_row + 1, start_column)
        or search_from(maze, start_row, start_column - 1)
        or search_from(maze, start_row, start_column + 1)
    )
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


my_maze = Maze("maze2.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)

my_maze.wn.exitonclick()