import matplotlib.pyplot as plt
import numpy as np
from chaos_game import ChaosGame



class Variations:
    """Class to generate a variation of chaos game which is stored as transformed x and y coordinates"""

    def __init__(
        self, x: float = None, y: float = None, name: str = "linear"
    ) -> None:
        self.name = name
        self._func = getattr(Variations, name)
        self.trans = self._func(x, y)
        self.y = self.trans[0]
        self.x = self.trans[1]

    @staticmethod
    def linear(x, y):
        return (x, y)

    @staticmethod
    def handkerchief(x, y):
        x = np.array(x)
        y = np.array(y)
        r = np.sqrt(np.power(x, 2) + np.power(y, 2))
        theta = np.arctan2(y, x)
        return (r * np.sin(theta + r), r * np.cos(theta - r))

    @staticmethod
    def swirl(x, y):
        x = np.array(x)
        y = np.array(y)
        r = np.sqrt(x ** 2 + y ** 2)
        r_sq = r ** 2
        return (
            x * np.sin(r_sq) - y * np.cos(r_sq),
            x * np.cos(r_sq) + y * np.sin(r_sq),
        )

    @staticmethod
    def disc(x, y):
        x = np.array(x)
        y = np.array(y)
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(y, x)
        return (
            (theta / np.pi) * np.sin(np.pi * r),
            (theta / np.pi) * np.cos(np.pi * r),
        )

    def transform(self):
        return self._func(self.x, self.y)

    @classmethod
    def from_chaos_game(cls, n, name):
        c = ChaosGame(n, 1 / 2)
        points = c.iterate()

        return cls(*zip(*points), name)


def plot_variations():
    grid_values = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [
        Variations(x_values, y_values, version) for version in transformations
    ]

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):

        u, v = variation.y, variation.x

        ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("off")

    plt.show()


def linear_combination_wrap(v1: tuple, v2: tuple) -> np.ndarray:
    array_v1 = np.array([v1.x, v1.y])
    array_v2 = np.array([v2.x, v2.y])

    def inner(w):
        return w * array_v1 + (1 - w) * array_v2

    return inner


def plot_linear_combination():
    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for ax, w in zip(axs.flatten(), coeffs):
        u, v = variation12(w)

        ax.scatter(u, -v, s=0.2, marker=".")
        ax.set_title(f"weight = {w:.2f}")
        ax.axis("off")
    plt.show()


if __name__ == "__main__":
    ngon = 3
    coeffs = np.linspace(0, 1, 4)

    variation1 = Variations.from_chaos_game(ngon, "linear")
    variation2 = Variations.from_chaos_game(ngon, "disc")
    variation12 = linear_combination_wrap(variation1, variation2)
    plot_linear_combination()
