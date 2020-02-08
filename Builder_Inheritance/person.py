class Person:
    def __init__(self):
        self.name = None
        self.date_of_birth = None
        self.company_name = None
        
        
    def __str__(self):
        return f'{self.name}:\n\t - born on {self.date_of_birth}\n' + \
            f'\t - Works at {self.company_name}'
            
    @staticmethod
    def new():
        return PersonJobBuilder()
    

class PersonBuilder:
    def __init__(self):
        self.person = Person()
        
    def build(self):
        return self.person
    

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self
    

class PersonBirthDateBuilder(PersonInfoBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self
            
            
class PersonJobBuilder(PersonBirthDateBuilder):
    def works_at(self, company_name):
        self.person.company_name = company_name
        return self
    

if __name__ == "__main__":
    person = Person.new()\
        .called('Vasyl Herman')\
            .born('28th of Feb')\
                .works_at('Pretty Solution')\
                    .build()

        
    print(person)