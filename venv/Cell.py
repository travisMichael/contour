import math
import Vertex as V
import Edge as E
import numpy as np
import color_util as cUtil


# utility method
def initialize_cells(img):
    array = []
    h, w = img.shape
    for i in range(h):
        row = []
        for j in range(w):
            color = img[i, j]
            node = Cell(color)
            row.append(node)
        array.append(row)

    return array


def intersection_points(x, y):
    m = max(abs(x), abs(y))
    new_x = x / m
    new_y = y / m
    return (new_x, new_y), (-1*new_x, -1*new_y)


# data structure for a receptive cell
class Cell:
    def __init__(self, color):
        self.color = color
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def get_mid_point(self):
        n_c, e_c, s_c, w_c = self.get_neighbors()
        if n_c is None or e_c is None or s_c is None or w_c is None:
            return None, None
        t_l = self.north.west
        t_r = self.north.east
        b_l = self.south.west
        b_r = self.south.east
        x = (t_l.x + t_r.x + b_l.x + b_r.x) / 4.0
        y = (t_l.y + t_r.y + b_l.y + b_r.y) / 4.0
        return x, y

    def get_neighbors(self):
        north_cell = self.north.north
        east_cell = self.east.north
        south_cell = self.south.south
        west_cell = self.west.south
        return north_cell, east_cell, south_cell, west_cell

    def get_gradient(self):
        n_c, e_c, s_c, w_c = self.get_neighbors()
        delta_y = (n_c.color - self.color) + (self.color - s_c.color)
        delta_x = (w_c.color - self.color) + (self.color - e_c.color)
        # todo: this is a temp hack
        # if n_c.color == 0 or e_c.color == 0 or s_c.color == 0 or w_c.color == 0:
        #     return 0, 0

        # theta = np.arctan2(1, -1)
        magnitude = np.sqrt(delta_x**2 + delta_y**2)
        return delta_x, delta_y, magnitude

    def create_initial_edge(self):
        m_x, m_y = self.get_mid_point()
        if m_x is None:
            return None
        delta_x, delta_y, magnitude = self.get_gradient()
        print(magnitude)
        color = cUtil.get_color_from_magnitude(magnitude)

        if abs(delta_x) < 0.01 and abs(delta_y) < 0.01:
            return None
        point_1, point_2 = intersection_points(delta_y, -1*delta_x)

        # divide by two, then add mid_point, then round
        vertex_1 = V.Vertex(point_1[0]/2 + m_x, point_1[1]/2 + m_y)
        vertex_2 = V.Vertex(point_2[0]/2 + m_x, point_2[1]/2 + m_y)
        #  color=(255, 0, 0)
        return E.Edge(vertex_1, vertex_2, color=color)

    def add_north(self, n):
        self.north = n

    def add_east(self, e):
        self.east = e

    def add_south(self, s):
        self.south = s

    def add_west(self, w):
        self.west = w
