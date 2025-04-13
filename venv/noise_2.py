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
    v_d1 = np.diff(x, axis=0)
    v_d2 = np.diff(v_d1, axis=0)
    h_d1 = np.diff(x, axis=1)
    h_d2 = np.diff(h_d1, axis=1)
    v_d2_padded = np.pad(v_d2, ((1, 1), (0, 0)), mode='constant')
    h_d2_padded = np.pad(h_d2, ((0, 0), (1, 1)), mode='constant')
    v_z = np.zeros_like(v_d2_padded)
    h_z = np.zeros_like(h_d2_padded)
    # https://stackoverflow.com/questions/3843017/efficiently-detect-sign-changes-in-python
    v_z[np.where(np.diff(np.sign(v_d2_padded)))] = 1
    h_z[np.where(np.diff(np.sign(h_d2_padded)))] = 1
    z = np.logical_or(v_z, h_z) * 255
    return z


if __name__ == "__main__":

    x = np.array([[0, -1, 3, 5, 3, 8]], dtype=np.int32)
    x_2 = np.array([[0, 3, 2, 5, 4, -1]], dtype=np.int32)
    r = x_2 > x
    c = np.logical_and(x, x_2)
    image = cv2.imread('images/result_4.jpeg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x = np.float32(gray_image)
    x_hat = x
    for i in range(100):
        x_hat, cost = d(x_hat, 0.1)
        print(cost)

    zero_c = zero_cross(x_hat)

    image_out = np.clip(x_hat, 0, 255).astype(np.uint8)
    cv2.imwrite('output/noise_2_test.png', image_out)
    cv2.imwrite('output/noise_2_zero_c.png', zero_c)
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


