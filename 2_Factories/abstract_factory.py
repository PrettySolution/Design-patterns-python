from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious!')


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious!')

# If you have hierarchy of types then you can have
# a corresponding hierarchy of factories

# Let's suppose that the operation of making drinks
# is so sophisticated that you need a factory to prepare a drink for you


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class HotDrinkMachine:
    class AvailableDrink(Enum):  # here we are breaking OCP when you make a new kind of drink
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for f in self.AvailableDrink:
                name = f.name[0] + f.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for idx, d in enumerate(self.factories):
            print(f'#{idx}: {d[0]}')
        s = input(f'Please, pick a drink (0-{len(self.factories) - 1}):')
        idx = int(s)
        s = input('Please, specify amount (ml): ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()

# Fine!
