from abc import ABC, abstractmethod

class Repositorio(ABC):

  @abstractmethod
  def insert(self, dado) -> None:
    pass

  @abstractmethod
  def deletar(self, dado) -> None:
    pass