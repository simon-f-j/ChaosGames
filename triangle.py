import matplotlib.pyplot as plt
import numpy as np
import random


def normalise(items: list) -> tuple:
    """Function to normalise a list of weights to 1"""
    normal = 1 / sum(items)
    return [item * normal for item in items]


def create_1000_points() -> list:
    """Function to generate 1000 random startingpoints"""
    a = []
    for n in range(1000):
        a.append(create_startingpoint())
    return a


def create_startingpoint(points: list) -> np.ndarray:
    """Function to generate a (singular) random startingpoint"""
    weights = normalise([np.random.random() for item in range(len(points) - 1)])
    res = [item * weight for item, weight in zip(points, weights)]
    start_point = sum(res)
    return start_point


def iterating_within(corners: list, start: np.ndarray, n: int) -> list:
    """Function to iterate within the corners of the triangle"""
    new_points = []
    new_points.append(start)

    nxt = (start + random.choice(corners)) / 2
    new_points.append(nxt)
    for i in range(n + 4):
        nxt = (nxt + random.choice(corners)) / 2
        if i > 5:
            new_points.append(nxt)
    return new_points


def iterating_within_colors(corners: list, start: np.ndarray, n: int) -> list:
    """Function to iterate within the corners of the triangle and save corner-indicies in a dict"""
    new_points = []
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    start_color = np.array(colors[0])

    new_points.append((start, start_color))

    nxt_choice = random.choice(corners)
    nxt = (start + nxt_choice) / 2

    nxt_color = np.array((start_color + np.array(colors[corner_name(nxt_choice)])) / 2)
    new_point_value = (nxt, nxt_color)
    new_points.append(new_point_value)

    for i in range(n + 4):
        nxt_choice = random.choice(corners)
        nxt = (nxt + nxt_choice) / 2
        nxt_color = np.array(
            (nxt_color + np.array(colors[corner_name(nxt_choice)])) / 2
        )

        if i > 5:
            new_point_value = (nxt, nxt_color)
            new_points.append(new_point_value)
    return new_points


def corner_name(corner: np.ndarray) -> int:
    c0 = np.array([0, 0])
    c1 = np.array([1, 0])
    c2 = np.array([0, 1])

    if (corner == c0).all():
        return 0
    elif (corner == c1).all():
        return 1
    elif (corner == c2).all():
        return 2


if __name__ == "__main__":
    c0 = np.array([0, 0])
    c1 = np.array([1, 0])
    c2 = np.array([0, 1])
    corners = [c1, c0, c2]

    a = iterating_within_colors(corners, create_startingpoint(corners), 10000)
    points = zip(*[item[0] for item in a])
    colors = [item[1] for item in a]

    plt.scatter(*points, s=0.2, color=colors)
    plt.show()
