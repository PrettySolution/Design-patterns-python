from math import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} and {self.y}'

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = Point.new_polar_point(1, 2)
    p2 = Point.new_cartesian_point(1, 2)
    print(p1)
    print(p2)


# What the factory method is?
# It's typically any method that creates an Object.
# A factory method is an alternative to initializer that has lots of advantages.
# You can have a good naming (better than init), you can have a better naming for arguments.
# Otherwise you would end up with a massive init constructor.
