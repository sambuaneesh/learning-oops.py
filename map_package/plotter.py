import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math


def plot_movement(person):
    fig, ax = plt.subplots()
    (line,) = ax.plot([], [], marker="o")

    def init():
        ax.set_xlim(min(person.x) - 1, max(person.x) + 1)
        ax.set_ylim(min(person.y) - 1, max(person.y) + 1)
        return (line,)

    def animate(i):
        line.set_data(person.x[: i + 1], person.y[: i + 1])

        # total_displacement = math.hypot(person.x[i], person.y[i])
        # total_displacement_x = person.x[i]
        # total_displacement_y = person.y[i]

        # print(f"Total Displacement: {total_displacement:.2f} cm")
        # print(f"Displacement in X: {total_displacement_x:.2f} cm")
        # print(f"Displacement in Y: {total_displacement_y:.2f} cm")

        return (line,)

    anim = FuncAnimation(
        fig, animate, init_func=init, frames=len(person.x), repeat=False, blit=True
    )
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("2D Movement Plot")
    plt.grid(True)
    plt.show()
