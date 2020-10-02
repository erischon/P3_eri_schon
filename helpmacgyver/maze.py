import random

from settings import Settings
from position import Position


class Maze:
    """ I create the board of the maze. """

    def __init__(self, filename):
        """ initialize the maze. """
        self.settings = Settings()
        self.filename = filename
        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        self.item1 = set()
        self.item2 = set()
        self.item3 = set()
        self.player = set()

        self.organize_the_maze()
        self.put_items()

    @property
    def start_pos(self):
        return list(self.start)[0]

    @property
    def item1_pos(self):
        return list(self.item1)[0]

    @property
    def item2_pos(self):
        return list(self.item2)[0]

    @property
    def item3_pos(self):
        return list(self.item3)[0]

    def organize_the_maze(self):
        """ Organize the cells of the maze. """
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    if col == self.settings.PATH_CHAR:
                        self.paths.add(Position(x, y))
                    elif col == self.settings.START_CHAR:
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                        self.player.add(Position(x, y))
                    elif col == self.settings.GOAL_CHAR:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == self.settings.WALL_CHAR:
                        self.walls.add(Position(x, y))

    def put_items(self):
        """ put the items in the maze. """
        free_paths = self.paths.difference(self.start)
        free_paths = free_paths.difference(self.goal)
        items_object = set(random.sample(free_paths, 3))
        self.item1.add(list(items_object)[0])
        self.item2.add(list(items_object)[1])
        self.item3.add(list(items_object)[2])

    def is_valid_cell(self, position):
        """ Return if a cell is valid or not. """
        return position in self.paths

    def is_special_cell(self, cell_pos):
        """ I Determine if a cell is special """
        if cell_pos in self.start:
            return False
        elif cell_pos in self.goal:
            return "goal"
        elif cell_pos in self.item1:
            return "item1"
        elif cell_pos in self.item2:
            return "item2"
        elif cell_pos in self.item3:
            return "item3"
        else:
            return False
