from modelo.token import Token
from modelo.categoria import Categoria

# Clase del token del separador
class Separador:

    # Metodo para comprobar que el fin de sentencia sea el correcto
    # y no contenga caracteres que no pertenezcan al operador. 
    # Simbolo: ,

    def __init__(self) -> None:
        pass

    # Metodo para generar el token y comprobar que tipo de token es.

    def generacionToken(self,text) -> Token:
        var = text[0]

        return Token(var, Categoria.SEPARADOR)
