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


def generate_blur(input_image):
    sigma = 1
    kernel_size = 3
    result = input_image
    for i in range(1):
        result = cv2.GaussianBlur(result, (kernel_size, kernel_size), sigma)
    return result


def generate_laplacian(input_image):
    blurred_image = generate_blur(input_image)
    return cv2.Laplacian(blurred_image, cv2.CV_16S, ksize=3)


def generate_zero_crossing_visual(input_image):
    laplacian_image = generate_laplacian(input_image)
    # blurred_image = generate_blur(input_image)
    gi = np.float32(laplacian_image)
    graph = g.Graph(gi)
    graph.step_zero_cross()
    image = d.draw_zero_crossings_from_graph(graph)
    cv2.imwrite('output/zero_crossings.png', image)


if __name__ == "__main__":
    poly_image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(poly_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('images/gray.jpeg', gray_image)
    generate_zero_crossing_visual(gray_image)

    print("done")