from person import Person


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person
        
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person
    

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self
    
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self
    
    def in_city(self, city):
        self.person.city = city
        return self
    
    
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
        
    def at(self, company_name):
        self.person.company_name = company_name
        return self
    
    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self
