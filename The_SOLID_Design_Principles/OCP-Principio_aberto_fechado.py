"""
OCP — Princípio aberto-fechado (Open/Closed Principle)

Esse principio diz que as classes “devem estar abertas para extensão, mas fechadas para modificação”, com isso passamos evitar possíveis erros a um aplicativo em ambiente produtivo, claro que se a modificação for para corrigir um erro existente no código esse principio não deveria ser aplicado.

Se você tem uma compreensão geral do POO, provavelmente já conhece o polimorfismo. Podemos garantir que nosso código esteja em conformidade com o princípio aberto / fechado, utilizando herança e / ou implementando interfaces que permitem que as classes se substituam polimorficamente uma pela outra
"""

from enum import Enum


class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3

class Size(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3

class Product:
	def __init__(self, name, color, size):
		self.name = name
		self.color = color
		self.size = size
		
class ProductFilter:
	def filter_by_color(self, products, color):
		for p in products:
			if p.color == color: yield p

	def filter_by_size(self, products, size):
		for p in products:
			if p.size == size: yield p

	def filter_by_color_and_size(self, products, size, color):
		for p in products:
			if p.size == size and p.color == color:
				yield p


"""
Segundo o princípio OCP, não podemos modificar as funcionalidades
da classe, apenas crescentear novas. Isso pode não ser escalavel 
dependendo da situação. Nesse exemplo, só estamos comparando com
2 casos, tamanho e cor, porém caso tivessemos 10 ou mais e tivessemos
que fazer combinações entre eles, essa classe ficaria com muitos métodos
e dificil para fazer manutenção.
"""

# Aplicando o OCP:

class Specification:
	def is_satisfied(self, item):
		pass

	def __and__(self, other):
		return AndSpecification(self, other)

class Filter:
	def filter(self, items, spec):
		pass

class ColorSpecification(Specification):
	def __init__(self, color):
		self.color = color

	def is_satisfied(self, item):
		return item.color == self.color

class SizeSpecification(Specification):
	def __init__(self, size):
		self.size = size

	def is_satisfied(self, item):
		return item.size == self.size

class AndSpecification(Specification):
	def __init__(self, *args):
		self.args = args

	def is_satisfied(self, item):
		return all(map(
			lambda spec: spec.is_satisfied(item), self.args
		))

class BetterFilter(Filter):
	def filter(self, items, spec):
		for item in items:
			if spec.is_satisfied(item):
				yield item


if __name__ == '__main__':
	apple = Product('Apple', Color.GREEN, Size.SMALL)
	tree = Product('Tree', Color.GREEN, Size.LARGE)
	house = Product('House', Color.BLUE, Size.LARGE)

	products = [apple, tree, house]

	pf = ProductFilter()
	print('Produtos verdes (Sem OCP):')
	for p in pf.filter_by_color(products, Color.GREEN):
		print(f'- {p.name} é verde. ')

	bf = BetterFilter()

	print('Produtos verdes (Com OCP):')
	green = ColorSpecification(Color.GREEN)
	for p in bf.filter(products, green):
		print(f'- {p.name} é verde. ')

	print('Produtos Grandes:')
	large = SizeSpecification(Size.LARGE)
	for p in bf.filter(products, large):
		print(f'- {p.name} é grande.')


	print('Produtos Grandes e azul:')
	large = SizeSpecification(Size.LARGE)
	blue = ColorSpecification(Color.BLUE)
	large_blue = AndSpecification(large, blue)
	for p in bf.filter(products, large_blue):
		print(f'- {p.name} é grande e azul.')