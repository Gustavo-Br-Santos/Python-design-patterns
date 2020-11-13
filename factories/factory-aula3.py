from abc import ABC
from enum import Enum, auto


# class HotDrink(ABC):
#     def consume(self):
#         pass

# class Tea(HotDrink):
#     def consume(self):
#         print('Este chá está delicioso!')

# class Coffee(HotDrink):
#     def consume(self):
#         print('Este café está delicioso!')

# class HotDrinkFactory(ABC):
#     def prepare(self, amount):
#         pass

# class TeaFactory(HotDrinkFactory):
#     def prepare(self, amount):
#         print(f'Coloque um pacote de chá no copo, ferva a água, derrame {amount}ml, e aproveite!')
#         return Tea()


# class CoffeeFactory(HotDrinkFactory):
#     def prepare(self, amount):
#         print(f'Coloque o café expresso no copo, ferva a água, derrame {amount}ml, e aproveite!')
#         return Coffee()




# def make_drink(type):
#     if type == 'tea':
#         return TeaFactory().prepare(200)
#     elif type == 'coffee':
#         return CoffeeFactory().prepare(50)
#     else:
#         return None


# if __name__ == '__main__':
#     entry = input('What kind of drink would you like?')
#     drink = make_drink(entry)
#     drink.consume()

"""
Percebemos que até aqui, não usamos a classe abstrata. Então podemos melhorar o código:
"""

class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class TeaFactory:
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory:
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))


    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)



if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
