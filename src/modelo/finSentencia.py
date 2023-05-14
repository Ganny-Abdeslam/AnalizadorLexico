
from modelo.token import Token
from modelo.categoria import Categoria

class FinSentencia:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:

        if text[0] == '¬':
            return '¬'

        return ""

    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.FIN_SENTENCIA)