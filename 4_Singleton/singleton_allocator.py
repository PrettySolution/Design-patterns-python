# One vary simple way of implementing a singleton in Python is by essentially rewriting the Allocator.
import random
import unittest
from unittest import TestCase


class Database:

    def __init__(self):
        self.my_id = random.randint(1, 101)
        print(f'id = {self.my_id}')

    _instance = None  # make a static instance

    def __new__(cls, *args, **kwargs):  # redefining the Allocator
        if not cls._instance:  # if hasn't been initialized yet
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Test(TestCase):
    def test_exercise(self):
        db1 = Database()
        db2 = Database()

        self.assertEqual(True, db1 == db2)
        self.assertEqual(True, db1.my_id == db2.my_id)


if __name__ == '__main__':
    unittest.main()
