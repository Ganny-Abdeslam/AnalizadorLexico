from modelo.token import Token
from modelo.categoria import Categoria

class Hexadecimal:
    def __init__(self) -> None:
        pass

    # Metodo para comprobar que las cadenas Hexadecimales sean los correctos
    # y no contenga caracteres que no pertenezcan al operador. 

    def comprobacion(self, text) -> str:

        # En el primer caso, si la cadena es vacia, retorna vacia.
        # En el segundo caso, si la cadena es un caracter, retorna ese caracter.
        # En el tercero caso, valida que la cadena tenga una "h" y retorna la cadena.

        if len(text) <= 0 :
            return ""
        
        if text[0] in 'ABCDEF' or text[0].isdigit() :
            return text[0] + self.comprobacion(text[1:])
        
        if text[0] == 'h':
            return text[0]

        return ""
    
    # Metodo para generar el token y comprobar que tipo de token es.
    
    def generacionToken(self, text) -> Token:
        var = self.comprobacion(text)

        if not('h' in var) :
            return Token("", Categoria.NO_RECONOCIDO)
    
        return Token(var, Categoria.HEXADECIMAL)
