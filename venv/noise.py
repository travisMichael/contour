import numpy as np
import matplotlib.pyplot as plt
import cv2


def d(x, lamb):
    d1 = np.diff(x)
    d2 = np.diff(d1)
    cost = np.sum(d2 * d2)
    d2_padded = np.pad(d2, 1, mode='constant')
    x_hat = x + lamb * d2_padded
    return x_hat, cost


def sin_with_noise():
    # Generate x values (angles)
    x = np.linspace(0, 2 * np.pi, 100)  # 100 points between 0 and 2pi

    # Calculate corresponding y values (sine of x)
    noise = np.random.normal(0,1,100) / 10
    y = np.sin(x)
    y_noise = y + noise
    return x, y, y_noise


def iterate_and_update(y_noise):
    y_hat = y_noise
    for i in range(100):
        y_hat, cost = d(y_hat, 0.1)
        print(cost)
    return y_hat


if __name__ == "__main__":
    print("hello")

    x, y, y_noise = sin_with_noise()
    y_hat = iterate_and_update(y_noise)

    # Create the plot
    plt.plot(x, y)
    plt.plot(x, y_hat)
    plt.plot(x, y_noise)

    # Add labels and title
    plt.xlabel('Angle (radians)')
    plt.ylabel('sin(angle)')
    plt.title('Sine Function')

    # Display the plot
    plt.grid(True)  # Add grid lines
    plt.show()


