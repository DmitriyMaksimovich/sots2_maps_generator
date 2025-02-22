import random, math


def random_chunks(list_of_items: list, base_value: int, delta: int):
    """
    Chunks with base_value +- delta elements
    """
    start = 0
    end = start + base_value + random.randint(-delta, delta)

    while start < len(list_of_items):
        yield list_of_items[start:end]
        start = end
        end = start + base_value + random.randint(0, delta + 1)


def random_point_in_sphere(center_x, center_y, center_z, radius) -> tuple[float, float, float]:
    r = radius * (random.uniform(0, 1) ** (1/3))

    # Generate a random direction using spherical coordinates
    theta = random.uniform(0, 2 * math.pi)  # Random angle around Z-axis
    phi = math.acos(random.uniform(-1, 1))  # Random angle from Z-axis

    # Convert spherical coordinates to Cartesian
    x = center_x + r * math.sin(phi) * math.cos(theta)
    y = center_y + r * math.sin(phi) * math.sin(theta)
    z = center_z + r * math.cos(phi)

    return x, y, z


def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
