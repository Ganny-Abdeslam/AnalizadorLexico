from modelo.token import Token
from modelo.categoria import Categoria

class Aritmeticos:
    def __init__(self) -> None:
        pass

    def generacionToken(self,text) -> Token:
        var = text[0]

        return Token(var, Categoria.OPERADOR_ARITMETICO)