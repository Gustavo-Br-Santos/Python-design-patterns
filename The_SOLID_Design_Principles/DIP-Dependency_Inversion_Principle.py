"""
DIP- Princípio da inversão de dependência

O princípio da inversão de dependência refere-se à dissociação de 
módulos de software. Dessa forma, em vez de módulos de alto nível, 
dependendo de módulos de baixo nível, ambos dependerão de abstrações.
Para cumprir esse princípio, precisamos usar um padrão de design 
conhecido como padrão de inversão de dependência , geralmente resolvido 
usando injeção de dependência .
A injeção de dependência é um tópico enorme e pode ser tão complicado ou 
simples quanto se possa perceber.
Normalmente, a injeção de dependência é usada simplesmente ‘injetando’ quaisquer 
dependências de uma classe através do construtor da classe ‘como um parâmetro de entrada’.
"""
from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING =2 

class Person:
    def __init__(self, name):
        self.name = name

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

class Research:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}.')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
"""
Saída:
John has a child called Chris.
John has a child called Matt.
"""

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING =2 

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')
        

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
"""
Saída:
John has a child called Chris.
John has a child called Matt.
"""

"""
Embora a saída seja a mesma, percebemos que a classe Research não tem mais dependência
com a lista de relations que tinha anteriormente, o que aumenta o nível de uso dessa classe.
"""