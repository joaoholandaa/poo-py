from .interface import Repositorio

class MongoRepositorio(Repositorio):

  def insert(self, dado) -> None:
    print('Inserindo {} no banco Mongo'.format(dado))

  def deletar(self, dado) -> None:
    print('Removendo {} no banco Mongo'.format(dado))