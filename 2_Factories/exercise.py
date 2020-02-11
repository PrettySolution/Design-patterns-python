from unittest import TestCase


class Person:
    def __init__(self, p_id, name):
        self.p_id = p_id
        self.name = name


class PersonFactory:
    _p_id = 0
    @staticmethod
    def create_person(name):
        p = Person(PersonFactory._p_id, name)
        PersonFactory._p_id += 1
        return p


class Evaluate(TestCase):
    def test_exercise(self):
        p0 = PersonFactory.create_person('Chris')
        self.assertEqual(0, p0.p_id)
        self.assertEqual('Chris', p0.name)

        p1 = PersonFactory.create_person('Sarah')
        self.assertEqual(1, p1.p_id)
