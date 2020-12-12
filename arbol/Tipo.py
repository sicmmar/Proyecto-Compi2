from enum import Enum

class Tipo(Enum):
    SIMPLE = 1, #asi como decimal, cadena, int, etc
    FUNCION = 2, #funciones como abs(), sin(), cos(), avg(), sum(), etc
    PATRON = 3, #'cadena' like '%patron' OR 'cadena' not like '%patron'
    TIME_INTERVAL = 4 #timestap / interval