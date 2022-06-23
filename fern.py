import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    """Class to hold the affine transform of the barnsley fern"""

    def __init__(
        self,
        a: float = 0,
        b: float = 0,
        c: float = 0,
        d: float = 0,
        e: float = 0,
        f: float = 0,
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x: float, y: float) -> np.ndarray:
        a_array = np.array([[self.a, self.b], [self.c, self.d]])
        b_array = np.array([[x], [y]])
        c_array = np.array([[self.e], [self.f]])

        result_matrix = np.concatenate(np.matmul(a_array, b_array) + c_array)
        return result_matrix


def random_choice():
    # Transforms
    f1 = AffineTransform(d=0.16)
    f2 = AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.60)
    f3 = AffineTransform(a=0.20, b=-0.26, c=0.23, d=0.22, f=1.60)
    f4 = AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44)
    transforms = [f1, f2, f3, f4]

    # Probabilities
    p1 = 0.01
    p2 = 0.85
    p3 = 0.07
    p4 = 0.07

    f = np.random.choice(transforms, p=[p1, p2, p3, p4])
    return f


def iterating_fern():
    start = (0, 0)
    f = random_choice()
    next = f(start[0], start[1])
    points = []
    for n in range(50000):
        points.append(next)
        f = random_choice()
        next = f(next[0], next[1])

    return points


def plot_fern():
    points = iterating_fern()
    plt.scatter(*zip(*points), s=0.1)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plot_fern()
