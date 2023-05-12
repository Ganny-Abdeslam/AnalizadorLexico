from modelo.token import Token
from modelo.categoria import Categoria

class Identificardor():
    def __init__(self) -> None:
        pass
    
    def comprobacion(self, text, count) -> str:

        if len(text) <= 0 or count > 10 :
            return ""
        
        if text[0].isalpha() or text[0].isdigit() or text[0] == '_' :
            count += 1
            return text[0] + self.comprobacion(text[1:], count)

        return ""
    
    def generacionToken(self, text) -> Token:
        var = self.comprobacion(text, 0)

        return Token(var, Categoria.IDENTIFICADOR)
