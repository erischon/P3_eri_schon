from .position import Position


class MacGyver:
    """ I'm the player. """

    def __init__(self, maze):
        """ Initialize position and bag. """
        self.maze = maze
        self.paths = maze.paths
        self.mg_pos = self.maze.start_pos
        self.item1_pos = self.maze.item1_pos
        self.item2_pos = self.maze.item2_pos
        self.item3_pos = self.maze.item3_pos
        self.bag = []
        self.mac_goal = False

    def move(self, direction):
        """ I move player and check if there is something to do after. """
        direction_mov = getattr(self.mg_pos, direction)
        if direction_mov() in self.paths:
            self.mg_pos = direction_mov()
            special_cell = self.maze.is_special_cell(self.mg_pos)
            if special_cell is not False:
                self.search_special(special_cell)
            return True

    def search_special(self, special_cell):
        """ I'm looking if there is something special on the cell. """
        if special_cell in ["item1", "item2", "item3"]:
            self.pouch_bag(special_cell)
        elif special_cell == "goal":
            self.mac_goal = True

    def pouch_bag(self, item):
        """ I pouch an item in the bag. """
        self.bag.append(item)
