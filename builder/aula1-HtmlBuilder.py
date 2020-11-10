"""
O padrão de projetos conhecido como Builder faz parte do grupo de padrões titulado 
como padrões criacionais definidos pelo GoF, dos quais começamos a tratar no artigo 
anterior, onde trabalhamos com os padrões de fábrica, Abstract factory e Factory Method. 
O padrão builder, por outro lado, é utilizado para construção de objetos complexos fazendo-se 
uso de uma abordagem de desenvolvimento passo a passo.

Por que devemos utilizar o padrão de projetos Builder?

O padrão Builder é um padrão de projetos de software comum que é usado para encapsular a lógica de 
construção de um objeto. Este padrão é frequentemente utilizado quando o processo de construção de 
um objeto é considerado complexo e também é adequado quando se trata da construção de representações 
múltiplas de uma mesma classe.

Quanto mais complexa for uma aplicação, maiores serão as complexidades existentes nas classes e objetos 
criados. Objetos complexos passam a ser construídos a partir de peças geradas a partir de outros objetos, o 
que demanda uma necessidade maior em relação a sua construção, um cuidado especial poderíamos dizer. Desta forma, 
podemos dizer que uma aplicação poderá precisar de um mecanismo para a construção de objetos complexos, que será 
independente das que o compõem. Se este é o tipo de problema ao qual estamos nos deparando na nossa aplicação, que 
tal utilizarmos o padrão de projetos builder?

Este é o tipo de padrão que permite que um objeto cliente seja capaz de construir um objeto complexo, especificando 
apenas o seu tipo e o seu conteúdo, sendo então protegido dos detalhes relacionados com a representação do objeto, 
entrando aqui o conceito de encapsulamento. Desta forma, o processo de construção pode ser usado para a construção de 
diferentes representações. A lógica deste processo é isolar a forma que os passos reais usados na criação de objetos 
complexos tomam, de modo que o processo possa ser usado novamente para a criação de um conjunto de objetos simples de 
igual forma a criação do primeiro.

fonte e mais informaçõe : https://www.devmedia.com.br/design-patterns-aplicando-os-padroes-builder-singleton-e-prototype/31023

"""

# Suponha que queiramos fajez uma página web por meio de comandos python

text = 'hello'

parts = ['<p>', text, '</p>']

print(''.join(parts))
"""
Saída:
<p>hello</p>
"""

words = ['hello', 'world']
parts = ['<ul>']
for word in words:
    parts.append(f' <li>{word}</li>')
parts.append('</ul>')
print('\n'.join(parts))
"""
Saída:
<ul>
 <li>hello</li>
 <li>world</li>
</ul>

"""

"""
Até aqui foi fácíl porque só adicionamos uma tag. Mas e se fosse uma página mais complexa,
teríamos que fazer isso para cada tag? Além disso, sería péssimo fazermos manutenção.

Podemos solucionar parte desse problema com o design pattern builder
"""

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        '''
            Recebe uma tag como nome e um conteúdo para tag
        '''
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * ( indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, chlid_name, child_text):
        '''
            Permite adicionar tags aninhadas(filhos) dentro da tag 
            em uso.
        '''
        self.__root.elements.append(
            HtmlElement(chlid_name, child_text)
        )

    def add_child_fluent(self, chlid_name, child_text):
        '''
            Permite adicionar tags aninhadas(filhos) dentro da tag 
            em uso e chamar o método em sequência.
        '''
        self.__root.elements.append(
            HtmlElement(chlid_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


 # Testando a classe

builder = HtmlBuilder('ul')
builder.add_child('li', 'Hello world !!!')
builder.add_child('li', 'Este é um exemplo de lista não ordenada')
builder.add_child('li', 'Usando o padrão de projetos Builder!')
print('Exemplo de lista não ordenada:')
print(builder)
"""
Saída:
Exemplo de lista não ordenada:
<ul>
  <li>
    Hello world !!!
  </li>
  <li>
    Este é um exemplo de lista não ordenada
  </li>
  <li>
    Usando o padrão de projetos Builder!
  </li>
</ul>
"""

 # Testando a classe com método add_child_fluent

builder = HtmlBuilder('ul')
builder.add_child_fluent('li', 'Hello world !!!').\
        add_child_fluent('li', 'Este é um exemplo de lista não ordenada').\
        add_child_fluent('li', 'Usando o padrão de projetos Builder!')

print('Exemplo de lista não ordenada:')
print(builder)
"""
Saída:
Exemplo de lista não ordenada:
<ul>
  <li>
    Hello world !!!
  </li>
  <li>
    Este é um exemplo de lista não ordenada
  </li>
  <li>
    Usando o padrão de projetos Builder!
  </li>
</ul>
"""

"""
Além disso, na nossa classe HtmlElement temos o método statico que nos 
permite usar a palavracreate para deixar mais claro que estamos criando uma tag 
e usa por baixo dos panos a nossa classe construtora. 
"""

builder = HtmlElement.create('ul')
builder.add_child_fluent('li', 'Hello world !!!').\
        add_child_fluent('li', 'Este é um exemplo de lista não ordenada').\
        add_child_fluent('li', 'Usando o padrão de projetos Builder!')

print('Exemplo de lista não ordenada:')
print(builder)
"""
Saída;
Exemplo de lista não ordenada:
<ul>
  <li>
    Hello world !!!
  </li>
  <li>
    Este é um exemplo de lista não ordenada
  </li>
  <li>
    Usando o padrão de projetos Builder!
  </li>
</ul>
"""