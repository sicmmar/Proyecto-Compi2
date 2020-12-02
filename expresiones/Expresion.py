from abc import ABC, abstractmethod
import sys
sys.path.append("/home/sicmmar/Documents/Compi2/Ejemplo2/entorno/")
from Entorno import Entorno

class Expresion(ABC):
    @abstractmethod
    def obtenerValor(self, ent = Entorno()): pass

    @abstractmethod
    def ejecutar(self, ent = Entorno()): pass