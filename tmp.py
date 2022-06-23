def create_polygon(sides, radius=1, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides
    points = [
        np.array(
            (
                math.sin(one_segment * i + rotation) * radius,
                math.cos(one_segment * i + rotation) * radius,
            )
        )
        for i in range(sides)
    ]
    if translation:
        points = [
            [np.array(sum(pair)) for pair in zip(point, translation)]
            for point in points
        ]

    return points


@dataclass(init=False)
class Polygon:
    corners: list[np.array]

    def __init__(self, *corners) -> None:
        self.corners = corners
