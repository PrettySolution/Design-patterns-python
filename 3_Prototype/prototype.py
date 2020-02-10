import copy
# The prototype pattern:
# In order to implement the prototype design pattern, you basically take a partially constructed object
# or indeed you can have a fully initialized object and you store it somewhere
# and then you deep copy the prototype whenever somebody wants to get an instance of it
# you allow the user to customize the resulting instance or if you are using a factory to provide
# a convenient API for actually using the protos in your code.
# The idea is that you've already got an existing design and you want to name a copy of that design,
# customize it somehow and then start using it. All you need is copy.deepcopy
# When it's easier to copy an existing object to fully initialize a new one.

class Address:
    def __init__(self, street_address, suite, city):
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street_address}, {self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name}, {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123A East Dr', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Dr', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_e(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_e(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


if __name__ == '__main__':
    john = EmployeeFactory.new_main_office_e('John', 100)
    jane = EmployeeFactory.new_aux_office_e('Jane', 500)
    print(john)
    print(jane)