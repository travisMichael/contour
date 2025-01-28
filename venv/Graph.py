import Vertex as V
import Edge as E
import Cell as C
import color_util as cUtil


def get_zero_crossing_info(intensity_1, intensity_2):
    return ((intensity_1 > 0 > intensity_2) or (intensity_1 < 0 < intensity_2),
            abs(intensity_1 - intensity_2))


# container class for vertices and edges
class Graph:
    def __init__(self, image):
        # construct nodes, vertices, and edges
        vertices = []
        edges = []
        h, w = image.shape
        self.h = h
        self.w = w
        self.scale = 20
        self.isZeroCrossing = False
        self.maxZeroCrossMag = 0.0
        nodes = C.initialize_cells(image)
        dic = {}
        # create horizontal edges
        for i in range(h+1):
            last_v = None
            for j in range(w+1):
                v = V.Vertex(j, i)
                dic[str(j)+"-"+str(i)] = v
                vertices.append(v)
                if last_v is not None:
                    e = E.Edge(last_v, v, border=True)
                    # add bidirectional relationships
                    if i == 0:
                        e.add_south(nodes[i][j-1])
                        nodes[i][j-1].add_north(e)
                    elif i == h:
                        e.add_north(nodes[i-1][j-1])
                        nodes[i-1][j-1].add_south(e)
                    else:
                        e.add_south(nodes[i][j-1])
                        nodes[i][j-1].add_north(e)
                        e.add_north(nodes[i-1][j-1])
                        nodes[i-1][j-1].add_south(e)
                    edges.append(e)
                last_v = v

        # create vertical edges. edge.north = west cell, edge.south=east cell
        for j in range(w+1):
            last_v = None
            for i in range(h+1):
                v = dic[str(j)+"-"+str(i)]
                vertices.append(v)
                if last_v is not None:
                    e = E.Edge(last_v, v, border=True)
                    if j == 0:
                        e.add_north(nodes[i-1][j])
                        nodes[i-1][j].add_west(e)
                    elif j == w:
                        e.add_south(nodes[i-1][j-1])
                        nodes[i-1][j-1].add_east(e)
                    else:
                        e.add_north(nodes[i-1][j])
                        nodes[i-1][j].add_west(e)
                        e.add_south(nodes[i-1][j-1])
                        nodes[i-1][j-1].add_east(e)
                    edges.append(e)
                last_v = v
        self.nodes = nodes
        self.vertices = vertices # 882
        self.edges = edges # 840

    def step_0(self):
        for i in range(self.h):
            for j in range(self.w):
                e = self.nodes[i][j].create_initial_edge()
                if e is not None:
                    self.edges.append(e)

    def step_zero_cross(self):
        # todo - for each cell, check if south edge is zc, check if east edge is zc
        max_mag = 0.0
        for i in range(self.h):
            for j in range(self.w):
                node = self.nodes[i][j]
                if j != self.w - 1:
                    east_edge = node.east
                    is_zero, mag = get_zero_crossing_info(node.color, east_edge.north.color)
                    if mag > 1:
                        east_edge.isZeroCrossing = is_zero
                        east_edge.zeroCrossMag = mag
                        max_mag = max(max_mag, mag)
                        east_edge.color = cUtil.get_color_from_magnitude(mag, 50)
                if i != self.h - 1:
                    south_edge = node.south
                    is_zero, mag = get_zero_crossing_info(node.color, south_edge.south.color)
                    if mag > 1:
                        south_edge.isZeroCrossing = is_zero
                        south_edge.zeroCrossMag = mag
                        max_mag = max(max_mag, mag)
                        south_edge.color = cUtil.get_color_from_magnitude(mag, 50)
        self.maxZeroCrossMag = max_mag


if __name__ == "__main__":
    print("done")



