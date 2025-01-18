import numpy as np

import Edge as e
import Vertex as v
import cv2


def draw_edges_from_graph(graph):
    image = np.ones((graph.h * graph.scale, graph.w * graph.scale, 3)) * 255
    for edge in graph.edges:
        draw_edge_at_scale(edge, graph.scale, image)

    return image


def draw_edges(edgeList):
    image = np.ones((50, 50, 3)) * 255
    for edge in edgeList:
        draw_edge(edge, image)

    return image


def draw_edge_at_scale(edge, scale, image):
    start_point = (round(edge.west.x*scale), round(edge.west.y*scale))
    end_point = (round(edge.east.x*scale), round(edge.east.y*scale))
    if edge.border:
        draw_edge_gradient(edge, scale, image)
    thickness = 1
    cv2.line(image, start_point, end_point, edge.color, thickness)


def draw_edge_gradient(edge, scale, image):

    mid = (round((edge.west.x + edge.east.x) / 2.0*scale), round((edge.west.y + edge.east.y) / 2.0*scale))
    l = round(scale / 4.0)
    if edge.west.x == edge.east.x:
        # edge is vertical
        start_point = (mid[0] - l, mid[1])
        end_point = (mid[0] + l, mid[1])
    else:
        # edge is horizontal
        start_point = (mid[0], mid[1]+l)
        end_point = (mid[0], mid[1]-l)

    color = (0, 0, 0)
    if edge.north is None or edge.south is None:
        return
    n_color = edge.north.color
    s_color = edge.south.color
    center = start_point
    if n_color == s_color:
        return
    if n_color > s_color:
        center = end_point
    # draw a line
    thickness = 1
    cv2.line(image, start_point, end_point, color, thickness)
    # draw a point
    # Draw a point at (256, 256) with radius 5 and color (0, 0, 255) (red)
    radius = 1
    cv2.circle(image, center, radius, color, -1)


def draw_edge(edge, image):
    start_point = (edge.west.x, edge.west.y)
    end_point = (edge.east.x, edge.east.y)
    color = (255, 0, 0)
    if edge.border:
        color = (0, 0, 0)
    thickness = 1
    cv2.line(image, start_point, end_point, color, thickness)


def draw_triangle_with_anti_aliasing():
    height = 20
    width = 20
    img = np.zeros((height,width,3), np.uint8)

    # Define an array of endpoints of triangle
    points = np.array([[4, 10], [15, 3], [16, 17]])

    cv2.fillPoly(img, pts=[points], color=(255, 0, 0), lineType=cv2.LINE_AA)

    cv2.imwrite("output/polygon.png", img)


if __name__ == "__main__":
    draw_triangle_with_anti_aliasing()
    vertex_1 = v.Vertex(20, 20)
    vertex_2 = v.Vertex(30, 20)
    edge_1 = e.Edge(vertex_1, vertex_2)
    edgeList = [edge_1]
    image_1 = draw_edges(edgeList)
    cv2.imwrite('output/out.png', image_1)