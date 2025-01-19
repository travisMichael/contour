import numpy as np


class Edge:
    def __init__(self, west, east, border=False, color=np.zeros(3)):
        # vertex
        self.west = west
        # vertex
        self.east = east
        # node
        self.north = None
        # node
        self.south = None
        self.border = border,
        self.color = color
        self.isZeroCrossing = False
        self.zeroCrossMag = 0.0

    def add_south(self, s):
        self.south = s

    def add_north(self, n):
        self.north = n

    def __str__(self):
        return "west(" + str(self.west) + "), east(" + str(self.east) + ")"
