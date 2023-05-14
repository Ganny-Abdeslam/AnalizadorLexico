from modelo.token import Token
from modelo.categoria import Categoria

# Clase de los operadores de incremento y decremento
class IncrementoDecremento:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:
        
        # Comprobación si la cadena está vacio o sólo tiene un caracter
        if len(text) <= 1:
            return ""
        
        # Comprobación si lo que se encuentra en la siguiente posición de la cadena es un signo +
        if text[1] == '+':
            return text[0:2]
        
        # Comprobación si lo que se encuentra en la siguiente posición de la cadena es un signo -
        if text[1] == '-':
            return text[0:2]

        return ""
    
    # Metodo para generar el token y comprobar que tipo de token es.

    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        return Token(var, Categoria.OPERADOR_INCREMENTODECREMENTO)