from modelo.token import Token
from modelo.categoria import Categoria


class OperadorRelacional:
    def __init__(self) -> None:
        pass


    def comprobacion(self, num) -> str:

        if len(num) <= 1:
            return num[0]
            
        if num[1] == '=':
            return num[0:2]
            
        return num[0]
    
    def generacionToken(self, text) -> Token:
        var = self.comprobacion(text)

        if var == "!" or var == "~" or var == '=':
            return Token("", Categoria.NO_RECONOCIDO)
         
        return Token(var, Categoria.OPERADOR_RELACIONAL)
            