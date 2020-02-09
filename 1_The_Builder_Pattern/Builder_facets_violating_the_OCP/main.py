from person_builder import PersonBuilder


if __name__ == "__main__":
    pb = PersonBuilder()
    person = pb\
        .lives\
            .at('55 London Road')\
            .with_postcode('58009')\
            .in_city('London')\
        .works\
            .at('Pretty Solution')\
            .as_a('Python Developer')\
            .earning('150.000')\
        .build()
        
    print(person)