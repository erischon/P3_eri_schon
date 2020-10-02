
class Settings:
    """ I'm the settings of the game. """
    def __init__(self):
        # Maze settings
        self.START_CHAR = 'S'
        self.GOAL_CHAR = 'G'
        self.PATH_CHAR = '.'
        self.WALL_CHAR = '#'
        self.FILENAME = 'map-1.txt'

        # Pygame Images
        self.floor = 'images/floor.bmp'
        self.wall = 'images/wall.bmp'
        self.goal = 'images/Gardien.png'
        self.macgyver = 'images/MacGyver.png'
        self.item1 = 'images/ether.png'
        self.item2 = 'images/seringue.png'
        self.item3 = 'images/tube_plastique.png'
        self.img_dimension_x = 40
        self.img_dimension_y = 40

        # Pygame dimensions
        self.cell_dimension_x = 44
        self.cell_dimension_y = 44
        self.nb_cell_x = 15
        self.nb_cell_y = 15
        self.maze_dimensions =  ((self.nb_cell_x * self.cell_dimension_x), (self.nb_cell_y * self.cell_dimension_y))
