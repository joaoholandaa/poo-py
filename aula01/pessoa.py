'''
------------------------------------
| Pessoa                           |
------------------------------------
|+nome:string                      |
|+idade:number                     |
|-cpf:string                       |
------------------------------------
|+correr():None                    |
|+beber(bebida:string):None        |
|-apresentar_documento():None      |
------------------------------------
'''

class Pessoa:

  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.__cpf = cpf

  def correr(self):
    print('Estou correndo')

  def beber(self, bebida):
    if bebida == 'cerveja':
      self.__apresentar_documento()
    print('bebendo...')

  def __apresentar_documento(self):
    print(self.__cpf)

joao = Pessoa('Joao', 21, '12345678')
joao.beber('cerveja')