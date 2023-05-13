from modelo.token import Token
from modelo.categoria import Categoria

class Hexadecimal:
    def __init__(self) -> None:
        pass

    def comprobacion(self, text) -> str:

        if len(text) <= 0 :
            return ""
        
        if text[0] in 'ABCDEF' or text[0].isdigit() :
            return text[0] + self.comprobacion(text[1:])
        
        if text[0] == 'h':
            return text[0]

        return ""
    
    def generacionToken(self, text) -> Token:
        var = self.comprobacion(text)

        if not('h' in var) :
            return Token("", Categoria.NO_RECONOCIDO)
    
        return Token(var, Categoria.HEXADECIMAL)
