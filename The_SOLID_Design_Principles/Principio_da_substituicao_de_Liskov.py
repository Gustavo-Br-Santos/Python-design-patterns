"""
Seja q(x) uma propriedade que se pode provar do objeto x do tipo T. 
Então, q(y) também é possível provar para o objeto y do tipo S,
sendo S um subtipo de T.

Significa dizer que classes derivadas devem poder substituídas por
suas classes base e que classes base podem ser substituídas por qualquer
uma das suas subclasses.   Uma subclasse deve sobrescrever os métodos da
superclasse de forma que a funcionalidade do ponto de vista do cliente
continue a mesma.

"""

class Retangle:
	def __init__(self, width, height):
		self._height = height
		self._width = width

	@property
	def area(self):
		return self._width * self._height

	def __str__(self):
		return f'Width: {self._width}, height: {self._height}'
	

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self, value):
		self._height = value
	

def use_it(retangulo):
	w = retangulo.width
	retangulo.height = 10
	expected = int(w*10)
	return print(f'Esperado uma área de {expected}, mas dado {retangulo.area}')


retangulo = Retangle(2,3)
use_it(retangulo)

"""
Saída:
Esperado uma área de 20, mas dado 20
"""
"""
Teste ok, porém esse teste mostra que é possível criar uma nova classe que quebra 
a respnsabilidade do método de tirar a raiz quadrada.
"""

class Square(Retangle):
	def __init__(self, size):
		Retangle.__init__(self, size, size)

	@Retangle.width.setter
	def width(self, value):
		self._width = self._height = value

	@Retangle.height.setter
	def height(self, value):
		self._width = self._height = value


quadrado = Square(5)
use_it(quadrado)
"""
Saída:
Esperado uma área de 50, mas dado 100
"""
"""
Fizemos uma classe quadrado e hedamos os métodos da classe triângulo,
e notamos que usando a função fora da classe, o calculo de 
área sai incorreto, visto que estamos pegando  o valor antes e 
alterando o valor depois, onde no caso do quadrado, o comprimento é igual a 
largura.

Isso ocorreu porque a classe Square violou o principio da substituição de
Liskov, visto que sobrescrevemose alteramos atributos que causam um impacto
no funcionamento da classe. Embora observamos que funcionou chamar os métodos direto da classe,
Segundo esse princípio, cou uma função fazendo o mesmo trabalho, o resultado deveria ser os mesmo.
"""