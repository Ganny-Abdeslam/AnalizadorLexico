from modelo.token import Token
from modelo.categoria import Categoria

class IncrementoDecremento:
    def __init__(self) -> None:
        pass

def comprobacion(self,text) -> str:
    if len(text) <= 1:
        return ""
        
    if text[1] == '+':
        return text[0:2]
        
    if text[1] == '-':
        return text[0:2]

    return ""

def generacionToken(self,text) -> Token:
    var = self.comprobacion(text)

    return Token(var, Categoria.OPERADOR_INCREMENTO_DECREMENTO)