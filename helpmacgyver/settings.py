class Settings:
    """ I'm the settings of the game. """

    def __init__(self):
        # Maze settings
        self.START_CHAR = "S"
        self.GOAL_CHAR = "G"
        self.PATH_CHAR = "."
        self.WALL_CHAR = "#"
        self.FILENAME = "helpmacgyver/map-1.txt"

        # Pygame Images
        self.floor = "helpmacgyver/images/floor.bmp"
        self.wall = "helpmacgyver/images/wall.bmp"
        self.goal = "helpmacgyver/images/Gardien.png"
        self.macgyver = "helpmacgyver/images/MacGyver.png"
        self.item1 = "helpmacgyver/images/ether.png"
        self.item2 = "helpmacgyver/images/seringue.png"
        self.item3 = "helpmacgyver/images/tube_plastique.png"
        self.img_dimension_x = 40
        self.img_dimension_y = 40

        # Pygame dimensions
        self.cell_dimension_x = 44
        self.cell_dimension_y = 44
        self.nb_cell_x = 15
        self.nb_cell_y = 15
        self.maze_dimensions = (
            (self.nb_cell_x * self.cell_dimension_x),
            (self.nb_cell_y * self.cell_dimension_y),
        )
