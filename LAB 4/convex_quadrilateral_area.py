import math


def four_lines_area(koeficient1, differ1, koeficient2, differ2,\
     koeficient3, differ3, koeficient4, differ4):
    """
    Function to get the area of the quadrangle

    Args:
        k1 (float): Koeficient of the line
        c1 (float): Difference of the line
        k2 (float): Koeficient of the line
        c2 (float): Difference of the line
        k3 (float): Koeficient of the line
        c3 (float): Difference of the line
        k4 (float): Koeficient of the line
        c4 (float): Difference of the line
    """
    x1, y1 = lines_intersection(koeficient1, differ1, koeficient2, differ2)
    x2, y2 = lines_intersection(koeficient2, differ2, koeficient3, differ3)
    x3, y3 = lines_intersection(koeficient3, differ3, koeficient4, differ4)
    x4, y4 = lines_intersection(koeficient4, differ4, koeficient1, differ1)

    a = distance(x1, y1, x2, y2)
    a = round(a, 2)
    b = distance(x2, y2, x3, y3)
    b = round(b, 2)
    c = distance(x3, y3, x4, y4)
    c = round(c, 2)
    d = distance(x4, y4, x1, y1)
    d = round(d, 2)
    f1 = (distance(x1, y1, x3, y3))
    f1 = round(f1, 2)
    f2 = (distance(x2, y2, x4, y4))
    f2 = round(f2, 2)
    return round(quadrangle_area(a, b, c, d, f1, f2), 2)

def lines_intersection(koeficient1, differ1, koeficient2, differ2):
    """ Function to find x and y

    Args:
        k1 (float): Koeficient
        c1 (float): Difference
        k2 (float): Koeficient
        c2 (float): Difference
    """
    if koeficient1 == koeficient2:
        return None
    x = (differ2 - differ1)/(koeficient1 - koeficient2)
    y = koeficient1 * x + differ1
    x = round(x, 2)
    y = round(y,2)

    return x, y


def distance(x1, y1, x2, y2):
    """
    Function to get the distance between to points

    Args:
        x1 (float): X
        y1 (float): Y
        x2 (float): X
        y2 (float): Y
    """
    distance_x = math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
    distance_x = round(distance_x, 2)
    return distance_x


def quadrangle_area(a, b, c, d, f1, f2):
    """[summary]

    Args:
        a (float): Length of the side of the quadrangle
        b (float): Length of the side of the quadrangle
        c (float): Length of the side of the quadrangle
        d (float): Length of the side of the quadrangle
        f1 (float): Diagonals of the quadrangle
        f2 (float): Diagonals of the quadrangle
    """
    square = ((4*(f1 ** 2) * (f2 ** 2) - (b ** 2 + d **
              2 - a ** 2 - c ** 2) ** 2) / 16) ** 0.5
    if type(square) == complex:
        return None
    square = round(square, 2)
    return square
print(quadrangle_area(3,4,3,4,5,5))