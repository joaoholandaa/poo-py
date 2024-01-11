from typing import Type
from db.interface import Repositorio
from db.mongo_repositorio import MongoRepositorio
from db.mysql_repositorio import MySqlRepositorio

class Usuario:

  def __init__(self, repositorio: Type[Repositorio]) -> None:
    self.__repositorio = repositorio

  def armazenar_dado(self, dado: any) -> None:
    self.__repositorio.insert(dado)

  def remover_dado(self, dado: any) -> None:
    self.__repositorio.deletar(dado)

usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dado(23)

usuario = Usuario(MongoRepositorio())
usuario.armazenar_dado(23)