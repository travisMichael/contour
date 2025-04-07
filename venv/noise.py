import numpy as np
import matplotlib.pyplot as plt
import cv2


# a = np.array([5, 8, 4, 3, 4])
# d1 = np.diff(a)
# d2 = np.diff(d1)
# f = np.insert(d2, 0, 0)
# f2 = np.append(f, 0)
def d(x, lamb):
    d1 = np.diff(x)
    d2 = np.diff(d1)
    cost = np.sum(d2 * d2)
    f = np.insert(d2, 0, 0)
    f2 = np.append(f, 0)
    x_hat = x + lamb * f2
    return x_hat, cost


# def d_2(x, x_n, lamb, lamb2):
#     d1 = np.diff(x_n)
#     d2 = np.diff(d1)
#     cost = np.sum(d2)
#     f = np.insert(d2, 0, 0)
#     f2 = np.append(f, 0)
#     x_hat = x_n + lamb * f2
#     x_hat = (x_hat - x_n) * lamb2
#     return x_hat, cost


if __name__ == "__main__":
    print("hello")


    # Generate x values (angles)
    x = np.linspace(0, 2 * np.pi, 100)  # 100 points between 0 and 2pi

    # Calculate corresponding y values (sine of x)
    noise = np.random.normal(0,1,100) / 10
    y_true = np.sin(x)
    y = y_true + noise
    y_hat = y
    for i in range(100):
        y_hat, cost = d(y_hat, 0.1)
        print(cost)

    # Create the plot
    plt.plot(x, y)
    plt.plot(x, y_hat)
    plt.plot(x, y_true)

    # Add labels and title
    plt.xlabel('Angle (radians)')
    plt.ylabel('sin(angle)')
    plt.title('Sine Function')

    # Display the plot
    plt.grid(True)  # Add grid lines
    plt.show()


