from unittest import TestCase


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)


class TestLine(TestCase):
    def test_exercise(self):
        line0 = Line()
        line1 = line0.deep_copy()
        line1.start.x = 1
        line2 = line1.deep_copy()
        line2.start.x = 2

        self.assertEqual(0, line0.start.x)
        self.assertEqual(1, line1.start.x)
        self.assertEqual(2, line2.start.x)
