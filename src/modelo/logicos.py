from modelo.token import Token
from modelo.categoria import Categoria

# Clase del token de los operadores lógicos
class Logicos:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:

        # Comprobación si texto esté vacio o sólo tiene un caracter
        if len(text) <= 1:
            return text[0]
        
        # Comprobación si el caracter de la posición actual es un !
        if text[0] == '!':
            return text[0]
        
        # Comprobación si el caracter de la siguiente posición es un |
        if text[1] == '|':
            return text[0:2]

        return text[0]
    

    # Metodo para generar el token y comprobar que tipo de token es.

    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.OPERADOR_LOGICO)