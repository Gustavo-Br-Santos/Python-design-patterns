"""
Factory é um padrão de design criativo que ajuda a ocultar o processo de criação de objetos.
Tipo de padrão - criativo
Benefícios -
A criação do objeto pode ser independente da implementação da classe.
Adicionar suporte a um novo tipo de objeto é muito fácil
A lógica da criação do objeto está oculta
Tipo de padrões -
Padrão de fábrica simples : Este design permite criar objetos sem expor a lógica de criação do objeto.
Padrão do método de fábrica : Este projeto permite criar objetos, mas adia a decisão para as subclasses
 de determinar a classe para a criação do objeto.
Padrão Abstract Factory : Um Abstract Factory é uma interface para criar objetos relacionados sem
especificar / expor suas classes. O padrão fornece objetos de outra fábrica, que cria outros objetos
internamente.

fonte: https://medium.com/@hnmpatel/design-patterns-in-python-factory-c728b88603eb
"""

"""
inicialmente, temos uma classe responsável por inicializar um ponto no sistema de coordenadas.
Porém, da forma que está implementado está perigoso, visto que caso queira adicionar um novo sistema,
teriamos que a classe Sistema cartesiano, e a classe Point, para cada novo sistema que adicionarmos.
Isso, além de violar o principio de open close, também se torna complicado para manutenção. 
"""

from enum import Enum
from math import *


class SistemaCartesiano(Enum):
    CARTESIANO = 1
    POLAR = 2

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PointFactory:
    @staticmethod
    def novo_ponto_cartesiano(x, y):
        p = Point()
        p.x = x
        p.y = y
        return p

    @staticmethod
    def novo_ponto_polar(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2,3)
    p2 = PointFactory.novo_ponto_polar(1, 2)
    print(p, p2)
"""
Saída:
x: 2, y: 3 x: -0.4161468365471424, y: 0.9092974268256817
"""