from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} and {self.y}'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = PointFactory.new_polar_point(1, 2)
    p2 = PointFactory.new_cartesian_point(1, 2)
    print(p1)
    print(p2)


# A factory is an implementation of Single Responsibility Principle or the Separation of concerns
