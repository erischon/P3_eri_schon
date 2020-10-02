
class Position:
    """ Calculate the position """

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    @property
    def x(self):
        return list(self.position)[0]

    @property
    def y(self):
        return list(self.position)[1]

    def up(self):
        x, y = self.position
        return Position(x-1, y)

    def down(self):
        x, y = self.position
        return Position(x+1, y)

    def right(self):
        x, y = self.position
        return Position(x, y+1)

    def left(self):
        x, y = self.position
        return Position(x, y-1)
