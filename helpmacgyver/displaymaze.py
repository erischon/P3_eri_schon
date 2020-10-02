import pygame

from settings import Settings


class DisplayMaze:
    """ I'm the object who display the maze with Pygame. """

    def __init__(self, paths, walls, start, goal, item1, item2, item3):
        """ I'm initialize the object DisplayMaze. """
        self.data = Settings()
        self.window = pygame.display.set_mode(self.data.maze_dimensions)
        self.paths = paths
        self.walls = walls
        self.start = start
        self.goal = goal
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

        self.display_maze(paths)
        self.display_maze(walls)
        self.display_maze(start)
        self.display_maze(goal)
        self.display_maze(item1)
        self.display_maze(item2)
        self.display_maze(item3)

    def display_maze(self, type):
        """ I'm the function who put a image on each cells. """
        cells = list(type)
        if type == self.paths:
            self.image = pygame.image.load(self.data.floor).convert()
        elif type == self.walls:
            self.image = pygame.image.load(self.data.wall).convert()
        elif type == self.start:
            self.img_mg = pygame.image.load(self.data.macgyver).convert()
        elif type == self.goal:
            self.image = pygame.image.load(self.data.goal).convert()
        elif type == self.item1:
            self.image = pygame.image.load(self.data.item1).convert()
        elif type == self.item2:
            self.image = pygame.image.load(self.data.item2).convert()
        elif type == self.item3:
            self.image = pygame.image.load(self.data.item3).convert()
        i = 0
        for path in cells:
            pos = list(cells)[i]
            pos_x = pos.y * self.data.cell_dimension_x
            pos_y = pos.x * self.data.cell_dimension_y
            self.window.blit(self.image, (pos_x, pos_y))
            i = i + 1
        pygame.display.flip()
