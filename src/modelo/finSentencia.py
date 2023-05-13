from modelo.token import Token
from modelo.categoria import Categoria

# Clase del token de fin de sentencia (¬)
class FinSentencia:
    def __init__(self) -> None:
        pass

    def generacionToken(self,text) -> Token:
        var = text[0]

        return Token(var, Categoria.FIN_SENTENCIA)
