from typing import Type

class Animal:

  def comer(self):
    print('O animal está comendo')

  def dormir(self):
    print('O animal está dormindo')

  def andar(self):
    print('O animal está andando na jaula')

class Aves(Animal):

  def __init__(self):
    super().__init__()

  def cantar(self):
    print('A ave está cantando')

class Pinguins(Aves):
  
  def __init__(self):
    super().__init__()

  def escorregar(self):
    print('O Pinguim está escorregando no gelo')

class Pessoa:

  def observar(self, animal: Type[Animal]):
    animal.comer()

joao = Pessoa()
pinguim = Aves()
joao.observar(pinguim)