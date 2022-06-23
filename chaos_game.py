import matplotlib.pyplot as plt
import numpy as np
import random


class ChaosGame:
    """Class to generate a sequence of chaos_game for a polygon of n number of edges"""

    def __init__(self, n, r=0.5):
        self.gradient_color = None

        def check_r(var, type, min, max) -> bool:
            if var > min and var < max and isinstance(var, type):
                return True
            else:
                raise Exception(f"r needs to be within 0<r<1 and of type: {type}")

        def check_n(var, type, min) -> bool:
            if var >= min and isinstance(var, type):
                return True
            else:
                raise Exception(f"n needs to be within n>=3 and of type: {type}")

        if check_n(n, int, 3) and check_r(r, float, 0, 1):
            self.n = n
            self.r = r

    def normalise(self, items: list) -> tuple:
        """Method to normalise items of a list to one"""
        normal = 1 / sum(items)
        return [item * normal for item in items]

    def _starting_point(self) -> list:
        """Method to generate a starting point by adding vectors with random normalised weights"""
        points = self._generate_ngon()
        weights = self.normalise([np.random.random() for item in range(len(points))])
        res = [item * weight for item, weight in zip(points, weights)]
        start_point = sum(res)
        return start_point

    def _generate_ngon(self) -> list:
        """Method to generate a n-gon based on the attribute n of the class"""
        angles = np.linspace(0, 2 * np.pi, self.n + 1)
        points = []
        for n, item in enumerate(angles):
            if n > 0:
                points.append(np.array([np.sin(item), np.cos(item)]))
        return points

    def plot_ngon(self):
        """Method to plot the generated n-gon"""
        points = self._generate_ngon()
        plt.scatter(*zip(*points))
        plt.show()

    def iterate(self, steps: int = 20000, discard: int = 5) -> list:
        """Method to iterate over the edges to generate the points of the chaos-game"""
        corners = self._generate_ngon()
        starting_point = self._starting_point()
        points = []

        nxt = self.r * starting_point + (1 - self.r) * random.choice(corners)
        for n in range(steps):
            nxt = self.r * nxt + (1 - self.r) * random.choice(corners)
            if n > discard:
                points.append(nxt)
        return points

    def plot(self, color: bool = False, cmap: str = "jet"):
        cm = plt.get_cmap(cmap)
        points = self.iterate()
        plt.scatter(*zip(*points), color="b", s=0.1, marker=".")

    def show(self):
        self.plot()
        plt.show()

    def savepng(self, outfile, color=False, cmap="jet"):
        self.plot(cmap=cmap, color=color)
        plt.savefig(outfile, transparent=False)


def starting_points(n: int):
    a = ChaosGame(n, 0.99)
    points = []
    for i in range(10000):
        points.append(a._starting_point())
    plt.scatter(*zip(*points))
    plt.show()
