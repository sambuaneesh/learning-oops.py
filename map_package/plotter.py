import matplotlib.pyplot as plt


def plot_movement(x, y):
    plt.plot(x, y, marker="o")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("2D Movement Plot")
    plt.grid(True)
    plt.show()
