from modelo.token import Token
from modelo.categoria import Categoria

class CadenaCaracteres:
    def __init__(self) -> None:
        pass

    # Metodo para comprobar que las cadenas de caracteres sea los correctos
    # y no contenga caracteres que no pertenezcan al operador. 
    # Simbolo: $ text $

    def comprobacion(self,text) -> str:

        
        # En el primer if valida el tamaño de la cadena si se cumple retorna una cadena vacia. 
        if len(text) <= 0:
            return ""
        
        #Que el ultimo caracter sea un "$"  
        if text[0] == '$':
            return text[0]
        
        # Retorna la cadena en la posicion cero y una llamada recursiva con el resto de la cadena.
        return text[0] + self.comprobacion(text[1:])

    # Metodo para generar el token y comprobar que tipo de token es.
    def generacionToken(self,text) -> Token:
        if len(text) <= 1:
            return Token("", Categoria.NO_RECONOCIDO)
        
        var = self.comprobacion(text[1:])

        if not(var[len(var)-1] == '$'):
            return Token("", Categoria.NO_RECONOCIDO)

        return Token("$" + var, Categoria.CADENA_CARACTERES)