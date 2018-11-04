def is_exact_split(points, x_split):
    for point in points:
        mirror_point = (point[0] + 2*(x_split-point[0]), point[1])
        print(mirror_point)
        if mirror_point not in points:
            return False
    return True
