class Mae:

  def __init__(self, endereco) -> None:
    self.endereco = endereco 
    self.sobrenome = 'Silva'

  def comer(self) -> None:
    print('Estou comendo')

  def estudar(self) -> None:
    print('Estou estudando')

class Filha(Mae):

  def __init__(self, endereco):
    super().__init__(endereco)

  def brincar(self, brinquedo: str) -> None:
    print('Estou brincando com {}'.format(brinquedo))

maria = Mae('Rua do Balão')
clara = Filha('Rua do Bolo')
clara.brincar('boneca')
clara.estudar()

print(maria.endereco)
print(clara.endereco)