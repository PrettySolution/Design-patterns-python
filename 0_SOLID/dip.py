from abc import abstractmethod
from enum import Enum, auto


class Person:
    def __init__(self, name):
        self.name = name


class Relation(Enum):
    PARENT = auto()
    CHILD = auto()
    SIBLING = auto()


# High level classes or high level modules in you code shouldn't directly depend on low level modules
class RelationshipBrowser:  # instead they should depend on abstractions (abstract class or class with abstract methods)
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relations(RelationshipBrowser):  # low-level module
    relations = []  # kind of storage of relationships

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relation.PARENT, child))
        self.relations.append((child, Relation.CHILD, parent))  # reverse
        return self

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relation.PARENT:
                yield r[2].name


class Research: # high-level class, a tool to print all child stored in a storage (relationships browser)
    def __init__(self, browser, parent_name):
        for child in browser.find_all_children_of(parent_name):  # here is a dependency on abstractmethod
            print(f'{parent_name} has a child called {child}')


if __name__ == '__main__':
    parent1 = Person('Vasyl')
    child1 = Person('Emily')
    child2 = Person('Max')

    relations = Relations() \
        .add_parent_and_child(parent1, child1) \
        .add_parent_and_child(parent1, child2)

    Research(relations, parent1.name)

