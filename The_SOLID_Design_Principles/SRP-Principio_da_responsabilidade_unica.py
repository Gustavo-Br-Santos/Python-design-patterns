"""
SRP — Princípio da responsabilidade única

Na programação, o Princípio da responsabilidade única declara que cada módulo ou classe deve ter responsabilidade sobre uma única parte da funcionalidade fornecida pelo software.
Você pode ter ouvido a citação: “ Faça uma coisa e faça bem “.

Isso se refere ao princípio da responsabilidade única.
Beneficios:
Teste — Uma classe com uma responsabilidade terá muito menos casos de teste
Menor acoplamento — menos funcionalidade em uma única classe terá menos dependências
Organização — Classes menores e bem organizadas são mais fáceis de pesquisar do que as classes monolíticas

fonte: https://medium.com/xp-inc/os-princ%C3%ADpios-do-solid-srp-princ%C3%ADpio-da-responsabilidade-%C3%BAnica-7897c55694fe
"""


class Journal:
    """Classe responsável por criar um jornal."""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, posicao):
        del self.entries[posicao]

    def __str__(self):
        return "\n".join(self.entries)

    """
	Note que, inicialmente colocamos a função de slavar e carregar dentro da classe
	Journal, porém, se pensarmos bem, elas tem uma responsabilidade a parte,
	para isso, vamos tirar elas daqui e criar uma classe própria para elas.
    """
    # break SRP
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    """Classe responsável por salvar arquivos."""
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Esta é a primeira linha do teste")
j.add_entry("Hello world !!!! :) ")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'C:\Users\Gustavo\Desktop\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
