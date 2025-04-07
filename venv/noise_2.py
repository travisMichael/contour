import numpy as np
import matplotlib.pyplot as plt
import cv2


def d(x, lamb):
    v_d1 = np.diff(x, axis=0)
    v_d2 = np.diff(v_d1, axis=0)
    h_d1 = np.diff(x, axis=1)
    h_d2 = np.diff(h_d1, axis=1)
    cost = np.sum(h_d2 * h_d2) + np.sum(v_d2 * v_d2)
    v_d2_padded = np.pad(v_d2, ((1, 1), (0, 0)), mode='constant')
    h_d2_padded = np.pad(h_d2, ((0, 0), (1, 1)), mode='constant')

    x_hat = x + lamb * v_d2_padded + lamb * h_d2_padded
    return x_hat, cost


def zero_cross(x):


if __name__ == "__main__":

    # x = np.array([[0, 1, 3, 5, 3, 8]], dtype=np.float32)
    image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x = np.float32(gray_image)
    x_hat = x
    for i in range(200):
        x_hat, cost = d(x_hat, 0.1)
        print(cost)

    image_out = np.clip(x_hat, 0, 255).astype(np.uint8)
    cv2.imwrite('output/noise_2_test.png', image_out)
    print("done")
    # # Create the plot
    # plt.plot(x, y)
    # plt.plot(x, y_hat)
    # plt.plot(x, y_true)
    #
    # # Add labels and title
    # plt.xlabel('Angle (radians)')
    # plt.ylabel('sin(angle)')
    # plt.title('Sine Function')
    #
    # # Display the plot
    # plt.grid(True)  # Add grid lines
    # plt.show()


