import cv2
import numpy as np
import Graph as g
import Draw as d


def generate_derivative_visual():
    poly_image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(poly_image, cv2.COLOR_BGR2GRAY)
    gi = np.float32(gray_image)
    graph = g.Graph(gi)
    graph.step_0()
    image = d.draw_edges_from_graph(graph)
    cv2.imwrite('output/graph.png', image)


def generate_laplacian(input_image):
    blurred_image = cv2.GaussianBlur(input_image, (3, 3), 1.0)
    return cv2.Laplacian(blurred_image, cv2.CV_16S, ksize=3)


def generate_zero_crossing_visual(input_image):
    laplacian_image = generate_laplacian(input_image)
    # todo create graph edges where there is a zero crossing


if __name__ == "__main__":
    poly_image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(poly_image, cv2.COLOR_BGR2GRAY)
    generate_zero_crossing_visual(gray_image)

    print("done")