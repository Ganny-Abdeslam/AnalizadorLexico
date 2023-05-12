from modelo.token import Token
from modelo.categoria import Categoria

class OperadorAsignacion:
    def __init__(self) -> None:
        pass

    def comprobacion(self,text) -> str:

        if len(text) <= 1:
            return text[0]
        
        if text[1] == '=':
            return text[0:2]
            
        return text[0]
    
    def generacionToken(self,text) -> Token:
        var = self.comprobacion(text)

        if var == ":":
            return Token("", Categoria.NO_RECONOCIDO)

        return Token(var, Categoria.OPERADOR_ASIGNACION)


