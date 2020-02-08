class Person:
    def __init__(self):
        self.name = None
        self.birth_date = None
        self.company_name = None

    @staticmethod
    def new():
        return PersonJobBuilder() # here is going to be the most derived builder

    def __str__(self):
        return f'{self.name}\n' + \
            f'\t - born on {self.birth_date}\n' + \
            f'\t - works at {self.company_name}'


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

# Good! Now, let's say it deployed to prod
# Time is gone
# Here I am going to add a new builder trying to not breaking OCP
# let's go


class PersonBirthDateBuilder(PersonInfoBuilder):
    def born(self, date):
        self.person.birth_date = date
        return self


# Ok, fine. More time is gone, I need one more builder
# Keep in mind the OCP


class PersonJobBuilder(PersonBirthDateBuilder):
    def works_at(self, company_name):
        self.person.company_name = company_name
        return self


if __name__ == '__main__':
    person = Person.new() \
        .called('Vasyl Herman') \
        .born('28th of Feb') \
        .works_at('Pretty Solution') \
        .build()

    print(person)

    # Do I break any principles here?