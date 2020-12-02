from entorno.Entorno import Entorno
from abc import ABC, abstractmethod
class Instruccion(ABC):
    @abstractmethod
    def ejecutar(self, ent = Entorno()): pass