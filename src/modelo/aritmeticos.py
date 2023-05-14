from modelo.token import Token
from modelo.categoria import Categoria

# Clase del token de operador aritmético
class Aritmeticos:

    # Metodo para comprobar que el operador aritmetico sea el correcto 
    # y no contenga caracteres que no pertenezcan al operador. 
    # Simbolo: +, -, *, /, %, ^

    def __init__(self) -> None:
        pass

    # Metodo para generar el token y comprobar que tipo de token es.

    def generacionToken(self,text) -> Token:
        var = text[0]

        return Token(var, Categoria.OPERADOR_ARITMETICO)