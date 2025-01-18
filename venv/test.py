import cv2
import numpy as np


if __name__ == "__main__":
    # poly_image = cv2.imread('output/polygon.png')
    poly_image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(poly_image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 1.0)

    laplacian_image = cv2.Laplacian(blurred_image, cv2.CV_16S, ksize=3)

    print()