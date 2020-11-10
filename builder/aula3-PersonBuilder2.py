"""
Nesse exemplo é possível notar que, caso seja adicionado atributos na classe Pessoa,
a classe PersonBuilder continuará imutável. Bastaria nós criarmos um novo construtos
para o atributo adicionado.
Por exemplo, se adicionarmos um atributo cpf para pessoa, bastaria criarmos uma classe
contrutora para cpf e chamá-la na hora de criar o objeto, e não precisaríamos mexer em 
nenhuma de nossas classes já criadas.
"""

class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.dete_of_birthday = None

    def __str__(self):
        return f'{self.name} nasceu em {self.dete_of_birthday} e trabalha como {self.position}.'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_bith):
        self.person.dete_of_birthday = date_of_bith
        return self

personBuilder = PersonBirthDateBuilder()
person = personBuilder.called('Fulano')\
                       .works_as_a('programador')\
                       .born('10/12/1980')\
                       .build()
print(person)
"""
Saída:
Fulano nasceu em 10/12/1980 e trabalha como programador.
"""