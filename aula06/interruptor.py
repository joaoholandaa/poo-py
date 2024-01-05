from typing import Type

class Interruptor:

  def __init__(self, comodo: str):
    self.__comodo = comodo

  def acender(self):
    print('acendendo {}'.format(self.__comodo))

  def apagar(self):
    print('apagando {}'.format(self.__comodo))

class Pessoa:

  def acender_luz(self, interruptor: Type[Interruptor]):
    interruptor.acender()

  def apagar_luz(self, interruptor: Type[Interruptor]):
    interruptor.apagar()

  def dormir(self):
    print('Fui dormir...')

joao = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()
joao.acender_luz(interruptor_quarto)