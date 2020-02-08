class Person:
    def __init__(self):
        # Lives
        self.street_address = None
        self.postcode = None
        self.city = None
        # Works
        self.company_name = None
        self.position = None
        self.annual_income = None
        
    def __str__(self):
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' + \
            f'Employed at {self.company_name} as a {self.position} earning {self.annual_income}'
