class Person:
    '''
        Inicializa uma pessoa com endereço e trabalho vazio
    '''
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Endereço: {self.street_address}, {self.postcode}, {self.city}. \n' +\
            f'Trabalha em uma {self.company_name} como {self.position} e ganha {self.annual_income}.'

class PersonBuilder:
    '''
        Classe construtora de pessoa.
    '''
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


class PersonJobBuilder(PersonBuilder):
    '''
        Classe construtora do trabalho da pessoa
    '''
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def eraning(self, annual_incomming):
        self.person.annual_income = annual_incomming
        return self


class PersonAddressBuilder(PersonBuilder):
    '''
        Classe construtora do endereço da pessoa
    '''
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

# Testando:

personBuilder = PersonBuilder()
person = personBuilder.lives\
                            .at('123 London Road')\
                            .in_city('London')\
                            .with_postcode('SW12BC')\
                        .works\
                            .at('Fabrica')\
                            .as_a('Engenheiro')\
                            .eraning(123000)\
                        .build()

print(person)
"""
Saída:
Endereço: 123 London Road, SW12BC, London.
Trabalha em uma Fabrica como Engenheiro e ganha 123000.
"""