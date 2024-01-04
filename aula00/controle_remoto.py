'''
------------------------------------
| ControleRemoto                   |
------------------------------------
|+televisao:string                 |
|+comodo:string                    |
------------------------------------
|+avancar_canal():None             |
|+voltar_canal():None              |
|+escolher_canal(canal:int):None   |
------------------------------------
'''

class ControleRemoto:
  
  def __init__(self, televisao, comodo):
    self.televisao = televisao
    self.comodo = comodo

  def avancar_canal(self):
    print('Canal Avançado')
  
  def voltar_canal(self):
    print('Voltar canal')

  def escolher_canal(self, canal):
    print('Alterado para o canal: {}'.format(canal))

controle_sala = ControleRemoto('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(25)