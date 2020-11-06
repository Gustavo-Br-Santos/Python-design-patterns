"""
ISP - Princípio da segregação da interface

Na programação, o princípio de segregação da interface afirma que
nenhum cliente deve ser forçado a depender dos métodos que não usa.
Simplificando: interfaces maiores devem ser divididas em menores. 
Ao fazer isso, podemos garantir que as classes de implementação 
só precisam se preocupar com os métodos que são do seu interesse.
"""

class Machine:
    def printer(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def printer(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def printer(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

"""
Podemos notar que a Classe Máquina possui métodos que são padrão
para outras máquinas de imprimir. Ao se tratar de uma impressora multifuncional, 
OK, pois ela realmente possuí todas essas funcionalidades apresentadas pelos métodos de 
imprimir, fax e scanner e pode herdar e sobrescrever tais métodos. Porém uma impressora
antida que só imprime, não faz sentido herdar esses métodos. Mesmo nós conseguindo
implementar um erro ou mensagem de advertência, isso é totalmente ineficaz, pois ainda
poderia gerar requisiçoes desnecessárias para o servidor e é algo que não faz sentido 
termos implementado.

Segundo o princípio ISP, Essa classe não deveria herdar métodos que não irá usar.
"""
# Uma forma de melhoria
# Melhoria aplicando o princípio ISP

class Printer:
    @abstractmethod
    def printer(self, document):
        pass

class Sacanner:
    @abstractmethod
    def printer(self, document):
        pass

class MyPrinter(Printer):
    def printer(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def printer(self, document):
        pass
    def scan(self, document):
        pass

class MultiFunctionDevices(Printer, Scanner):
    @abstractmethod
    def printer(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionDevices(MultiFunctionDevices):
    def __init__(self, printer1, scanner):
        self.printer1 = printer1
        self.scanner = scanner

    def printer(self, document):
        self.printer1.printer(document)
    
    def scan(self, document):
        self.scanner.scan(document)

"""
Agora, dividimos em classes menores com funcionalidade específicas que
podem ser herdadas por máquinas com mais funções apenas quando for usar
algum de seus métodos.
"""