#!/usr/bin/python3
""" A Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""
    if n <= 0:
        return []

    tria = [[1]]
    while len(tria) != n:
        tri = tria[-1]
        count = [1]
        for x in range(len(tri) - 1):
            count.append(tri[x] + tri[x + 1])
        count.append(1)
        tria.append(count)
    return tria
